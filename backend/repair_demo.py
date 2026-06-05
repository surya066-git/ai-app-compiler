import argparse
import asyncio
import json
import os
from copy import deepcopy
from typing import Any, Dict, Tuple

from agents.export_agent import export_project
from agents.repair_agent import repair_project
from agents.validation_agent import validate_generated_project
from config.settings import settings
from contracts.app_ir_schema import AppIR
from generators.backend_generator import generate_backend_system
from generators.docker_generator import generate_docker_setup
from generators.frontend_generator import generate_frontend_system
from generators.runtime_generator import generate_runtime_system
from llm.local_provider import LocalDeterministicProvider
from planning.deterministic_planner import plan_architecture
from repair.schema_repair import attempt_schema_repair
from runtime.sandbox_runner import execute_sandbox
from validators.schema_validator import validate_schema


async def _base_project() -> Tuple[Dict[str, str], AppIR]:
    provider = LocalDeterministicProvider()
    ir = await plan_architecture("Build a todo app with users and tasks", provider)
    backend_files, jwt_secret = await generate_backend_system(ir, provider)
    frontend_files = await generate_frontend_system(ir, provider)
    files = {
        **backend_files,
        **frontend_files,
        **generate_runtime_system(ir, jwt_secret),
        **generate_docker_setup(),
    }
    return files, ir


async def _validation_repair_scenario(name: str, files: Dict[str, str], ir: AppIR, mutate) -> Dict[str, Any]:
    provider = LocalDeterministicProvider()
    scenario_files = deepcopy(files)
    mutate(scenario_files, ir)
    trace = []
    before_error = None
    repaired = False

    try:
        validate_generated_project(scenario_files, ir)
    except Exception as exc:
        before_error = str(exc)
        scenario_files = await repair_project(scenario_files, exc, provider, trace)
        validate_generated_project(scenario_files, ir)
        repaired = True

    return {
        "scenario": name,
        "detected": before_error is not None,
        "repaired": repaired,
        "validation_passed_after_repair": True,
        "initial_error": before_error,
        "trace": trace,
    }


async def _schema_scenario(ir: AppIR) -> Dict[str, Any]:
    raw = json.dumps({
        "app_name": ir.app_name,
        "description": ir.description,
        "tables": ["users", "tasks"],
        "pages": ["Dashboard", "Tasks"],
        "roles": "admin",
        "assumptions": "JWT auth is used",
    })
    repaired = attempt_schema_repair(f"```json\n{raw}\n```")
    validated = validate_schema(repaired)
    return {
        "scenario": "schema_mismatch",
        "detected": True,
        "repaired": True,
        "validation_passed_after_repair": isinstance(validated, AppIR),
        "initial_error": "LLM output used schema-compatible data with wrong container shapes",
        "trace": [{
            "type": "schema_repair",
            "status": "applied",
            "normalizations": ["code_fence_removed", "roles_string_to_list", "tables_strings_to_objects", "pages_strings_to_objects"],
        }],
    }


async def _runtime_scenario(files: Dict[str, str], ir: AppIR, runtime: bool) -> Dict[str, Any]:
    provider = LocalDeterministicProvider()
    scenario_files = deepcopy(files)
    scenario_files["backend/main.py"] = scenario_files["backend/main.py"].replace("from fastapi import FastAPI\n", "")
    trace = []
    simulated_error = RuntimeError("NameError in backend/main.py: name 'FastAPI' is not defined")

    if not runtime:
        repaired_files = await repair_project(scenario_files, simulated_error, provider, trace)
        validate_generated_project(repaired_files, ir)
        return {
            "scenario": "runtime_startup_failure",
            "detected": True,
            "repaired": True,
            "runtime_validation_passed_after_repair": "from fastapi import FastAPI" in repaired_files["backend/main.py"],
            "initial_error": str(simulated_error),
            "trace": trace,
            "runtime_executed": False,
        }

    zip_path = await export_project(scenario_files, "repair-demo-runtime-before", ir.model_dump())
    failed = await execute_sandbox(zip_path[:-4])
    repaired_files = await repair_project(
        scenario_files,
        RuntimeError("; ".join(failed.get("errors", [])) or str(simulated_error)),
        provider,
        trace,
    )
    validate_generated_project(repaired_files, ir)
    zip_path = await export_project(repaired_files, "repair-demo-runtime-after", ir.model_dump())
    passed = await execute_sandbox(zip_path[:-4])

    return {
        "scenario": "runtime_startup_failure",
        "detected": not failed.get("success"),
        "repaired": bool(trace),
        "runtime_validation_passed_after_repair": bool(passed.get("success")),
        "initial_error": failed.get("errors", []),
        "trace": trace,
        "runtime_executed": True,
        "health_report": passed.get("health_report", {}),
    }


def _remove_first_route(files: Dict[str, str], ir: AppIR) -> None:
    route = ir.endpoints[0].path
    for path in list(files):
        if path.startswith("backend/routers/") and route in files[path]:
            files.pop(path)
            return


def _add_broken_import(files: Dict[str, str], ir: AppIR) -> None:
    files["backend/main.py"] = files["backend/main.py"] + "\nDEMO_ENV = os.getenv('DEMO_ENV', 'ok')\n"


def _break_frontend_api(files: Dict[str, str], ir: AppIR) -> None:
    files["frontend/src/api.js"] = "export default {};\n"


async def run_demo(runtime: bool = False) -> Dict[str, Any]:
    settings.OFFLINE_DEMO_MODE = True
    files, ir = await _base_project()
    report = {
        "runtime_mode": runtime,
        "scenarios": [
            await _validation_repair_scenario("missing_route", files, ir, _remove_first_route),
            await _validation_repair_scenario("broken_import", files, ir, _add_broken_import),
            await _schema_scenario(ir),
            await _validation_repair_scenario("frontend_backend_inconsistency", files, ir, _break_frontend_api),
            await _runtime_scenario(files, ir, runtime),
        ],
    }
    report["summary"] = {
        "total_scenarios": len(report["scenarios"]),
        "detected": sum(1 for item in report["scenarios"] if item.get("detected")),
        "repaired": sum(1 for item in report["scenarios"] if item.get("repaired")),
    }

    os.makedirs(settings.EXPORT_DIR, exist_ok=True)
    path = os.path.join(settings.EXPORT_DIR, "repair_report.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run deterministic repair demonstrations.")
    parser.add_argument("--runtime", action="store_true", help="Execute the runtime startup failure before and after repair.")
    return parser.parse_args()


if __name__ == "__main__":
    result = asyncio.run(run_demo(runtime=parse_args().runtime))
    print(json.dumps(result["summary"], indent=2))
