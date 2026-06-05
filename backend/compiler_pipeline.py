import json
import os
from typing import Any, Dict

from agents.export_agent import export_project
from agents.intent_agent import parse_intent
from agents.repair_agent import repair_project
from agents.validation_agent import validate_generated_project
from clarification.ambiguity_detector import detect_ambiguity
from clarification.assumption_engine import generate_assumptions
from config.settings import settings
from contracts.app_ir_schema import AppIR
from evaluation.quality_scorer import score_quality
from exceptions.generation_exceptions import RepairFailedException, ValidationException
from generators.backend_generator import generate_backend_system
from generators.docker_generator import generate_docker_setup
from generators.frontend_generator import generate_frontend_system
from generators.runtime_generator import generate_runtime_system
from history.memory_manager import MemoryManager
from llm.provider_router import get_provider_router
from planning.deterministic_planner import plan_architecture
from runtime.sandbox_runner import execute_sandbox
from utils.metrics import MetricsTracker


PIPELINE_STAGES = [
    "Intent Extraction",
    "Clarification",
    "Planning",
    "IR Generation",
    "Generation",
    "Validation",
    "Repair",
    "Runtime Launch",
    "Health Check",
    "Export",
    "Evaluation",
]


async def run_compiler_pipeline(
    prompt: str,
    *,
    run_runtime: bool = True,
    require_runtime_success: bool = True,
    raise_on_failure: bool = True,
) -> Dict[str, Any]:
    metrics = MetricsTracker()
    memory_manager = MemoryManager()
    provider_router = get_provider_router()
    stage_events = []
    repair_trace = []
    runtime_success = not run_runtime
    sandbox_res: Dict[str, Any] = {
        "success": not run_runtime,
        "skipped": not run_runtime,
        "errors": [],
        "health_report": {
            "success": not run_runtime,
            "skipped": not run_runtime,
            "checks": [],
        },
    }
    zip_path = None
    project_dir = None

    def record_stage(stage: str, status: str = "completed", details: Dict[str, Any] | None = None) -> None:
        metrics.record_stage(stage)
        stage_events.append({"stage": stage, "status": status, "details": details or {}})

    try:
        record_stage("Intent Extraction", "running")
        intent = await parse_intent(prompt, provider_router)
        stage_events[-1]["status"] = "completed"

        record_stage("Clarification", "running")
        ambiguity = await detect_ambiguity(prompt, provider_router)
        assumptions = await generate_assumptions(prompt, ambiguity, provider_router)
        stage_events[-1]["status"] = "completed"

        record_stage("Planning", "running")
        ir: AppIR = await plan_architecture(prompt, provider_router)
        stage_events[-1]["status"] = "completed"

        record_stage("IR Generation", "completed", {"tables": len(ir.tables), "endpoints": len(ir.endpoints), "pages": len(ir.pages)})
        generation_id = memory_manager.save_generation_metadata(prompt, ir.model_dump(), "fallback_chain")

        record_stage("Generation", "running")
        backend_files, jwt_secret = await generate_backend_system(ir, provider_router)
        frontend_files = await generate_frontend_system(ir, provider_router)
        runtime_files = generate_runtime_system(ir, jwt_secret)
        docker_files = generate_docker_setup()
        project_files = {**backend_files, **frontend_files, **runtime_files, **docker_files}
        project_files["assumptions.json"] = json.dumps(assumptions, indent=2)
        stage_events[-1]["status"] = "completed"
        stage_events[-1]["details"] = {"files_generated": len(project_files)}

        max_repairs = 3
        repair_count = 0
        while True:
            record_stage("Validation", "running", {"attempt": repair_count + 1})
            try:
                validate_generated_project(project_files, ir)
                stage_events[-1]["status"] = "completed"
                break
            except ValidationException as e:
                stage_events[-1]["status"] = "failed"
                metrics.increment_validation_failure()
                repair_trace.append({"type": "validation_failure", "error": str(e), "details": e.details})
                if repair_count >= max_repairs:
                    raise RepairFailedException("Failed to repair project within limits.")
                record_stage("Repair", "running", {"attempt": repair_count + 1, "error": str(e)})
                repair_count += 1
                metrics.increment_repair()
                project_files = await repair_project(project_files, e, provider_router, trace=repair_trace)
                stage_events[-1]["status"] = "completed"

        if repair_count == 0:
            record_stage("Repair", "skipped", {"reason": "No validation repair required"})

        # Runtime checks need files on disk. The ZIP is removed below if the
        # runtime gate fails, so a failed project is not exposed as a download.
        zip_path = await export_project(project_files, generation_id, ir.model_dump())
        project_dir = zip_path[:-4]

        if run_runtime:
            runtime_repair_attempts = 0
            max_runtime_repairs = 2
            while True:
                record_stage("Runtime Launch", "running", {"attempt": runtime_repair_attempts + 1})
                sandbox_res = await execute_sandbox(project_dir)
                runtime_success = bool(sandbox_res.get("success"))
                stage_events[-1]["status"] = "completed" if runtime_success else "failed"

                record_stage(
                    "Health Check",
                    "completed" if sandbox_res.get("health_report", {}).get("success") else "failed",
                    sandbox_res.get("health_report", {}),
                )

                if runtime_success:
                    break

                metrics.increment_runtime_failure()
                repair_trace.append({
                    "type": "runtime_failure",
                    "error": "; ".join(sandbox_res.get("errors", [])),
                    "health_report": sandbox_res.get("health_report", {}),
                    "attempt": runtime_repair_attempts + 1,
                })

                if runtime_repair_attempts >= max_runtime_repairs:
                    break

                record_stage("Repair", "running", {
                    "attempt": repair_count + 1,
                    "scope": "runtime",
                    "error": sandbox_res.get("errors", []),
                })
                runtime_repair_attempts += 1
                repair_count += 1
                metrics.increment_repair()
                project_files = await repair_project(
                    project_files,
                    RuntimeError("; ".join(sandbox_res.get("errors", []))),
                    provider_router,
                    trace=repair_trace,
                )
                validate_generated_project(project_files, ir)
                zip_path = await export_project(project_files, generation_id, ir.model_dump())
                project_dir = zip_path[:-4]
                stage_events[-1]["status"] = "completed"
        else:
            record_stage("Runtime Launch", "skipped", {"reason": "Benchmark quick mode"})
            record_stage("Health Check", "skipped", {"reason": "Benchmark quick mode"})
            _write_json(
                project_dir,
                "health_report.json",
                {"success": True, "skipped": True, "checks": [], "reason": "Benchmark quick mode"},
            )
            _write_json(
                project_dir,
                "runtime_metrics.json",
                {"success": True, "skipped": True, "reason": "Benchmark quick mode"},
            )

        if require_runtime_success and not runtime_success:
            if zip_path and os.path.exists(zip_path):
                os.remove(zip_path)
            record_stage("Export", "blocked", {"reason": "Runtime or health verification failed"})
        else:
            record_stage("Export", "completed", {"zip_path": zip_path})

        final_metrics = metrics.finish()
        provider_metrics = provider_router.snapshot_metrics()
        final_metrics["provider_fallbacks"] = provider_metrics["fallbacks"]
        final_metrics["provider_latency"] = provider_metrics["provider_latency"]

        score = score_quality(generation_id, repair_count, runtime_success, True)
        record_stage("Evaluation", "completed", {"score": score["score"], "grade": score["grade"]})

        result = {
            "success": runtime_success or not require_runtime_success,
            "generation_id": generation_id,
            "intent": intent,
            "architecture": ir.model_dump(),
            "assumptions": assumptions,
            "metrics": final_metrics,
            "provider_metrics": provider_metrics,
            "repair_count": repair_count,
            "repair_trace": repair_trace,
            "runtime": sandbox_res,
            "score": score,
            "stages": stage_events,
            "download_url": f"/download/{os.path.basename(zip_path)}" if zip_path and os.path.exists(zip_path) and (runtime_success or not require_runtime_success) else None,
        }

        if project_dir:
            _write_json(project_dir, "repair_report.json", {"repair_count": repair_count, "traces": repair_trace})
            _write_json(project_dir, "quality_score.json", score)
            _write_json(project_dir, "failure_report.json", tracker_snapshot())
            _write_json(project_dir, "pipeline_report.json", result)

        if require_runtime_success and not runtime_success and raise_on_failure:
            raise RuntimeError(f"Runtime validation failed: {sandbox_res.get('errors')}")

        return result
    except Exception:
        metrics.finish()
        raise


def _write_json(project_dir: str | None, filename: str, payload: Dict[str, Any]) -> None:
    if not project_dir:
        return
    os.makedirs(project_dir, exist_ok=True)
    with open(os.path.join(project_dir, filename), "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def tracker_snapshot() -> Dict[str, Any]:
    try:
        from evaluation.failure_taxonomy import tracker
        return tracker.snapshot()
    except Exception:
        return {}
