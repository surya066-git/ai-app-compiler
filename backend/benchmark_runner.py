import argparse
import asyncio
import json
import os
from statistics import mean
from typing import Any, Dict, List

from compiler_pipeline import run_compiler_pipeline
from config.settings import settings
from evaluation.evaluation_report import generate_evaluation_report
from evaluation.failure_taxonomy import tracker


def _load_cases(filename: str) -> List[Dict[str, Any]]:
    path = os.path.join(os.path.dirname(__file__), "evaluation", filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


async def _run_case(case: Dict[str, Any], *, runtime: bool) -> Dict[str, Any]:
    case_id = case.get("id", "unknown")
    prompt = case["prompt"]
    try:
        result = await run_compiler_pipeline(
            prompt,
            run_runtime=runtime,
            require_runtime_success=runtime,
            raise_on_failure=False,
        )
        metrics = result.get("metrics", {})
        provider_metrics = result.get("provider_metrics", {})
        return {
            "id": case_id,
            "prompt": prompt,
            "issue": case.get("issue"),
            "success": bool(result.get("success")),
            "generation_id": result.get("generation_id"),
            "latency": metrics.get("latency", 0),
            "repair_counts": result.get("repair_count", metrics.get("repair_counts", 0)),
            "provider_fallbacks": provider_metrics.get("fallbacks", metrics.get("provider_fallbacks", 0)),
            "provider_switches": provider_metrics.get("provider_switches", 0),
            "quota_failures": provider_metrics.get("quota_failures", 0),
            "runtime_failures": metrics.get("runtime_failures", 0),
            "validation_failures": metrics.get("validation_failures", 0),
            "download_url": result.get("download_url"),
            "stage_statuses": [(stage["stage"], stage["status"]) for stage in result.get("stages", [])],
        }
    except Exception as exc:
        return {
            "id": case_id,
            "prompt": prompt,
            "issue": case.get("issue"),
            "success": False,
            "latency": 0,
            "repair_counts": 0,
            "provider_fallbacks": 0,
            "provider_switches": 0,
            "quota_failures": 0,
            "runtime_failures": 1 if runtime else 0,
            "validation_failures": 1,
            "error": str(exc),
        }


def _write_json(filename: str, payload: Dict[str, Any]) -> str:
    os.makedirs(settings.EXPORT_DIR, exist_ok=True)
    path = os.path.join(settings.EXPORT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    return path


async def run_benchmarks(args: argparse.Namespace) -> Dict[str, Any]:
    if args.offline:
        settings.OFFLINE_DEMO_MODE = True

    cases = []
    if args.include_prompts:
        cases.extend(_load_cases("prompts.json"))
    if args.include_edge_cases:
        cases.extend(_load_cases("edge_cases.json"))
    if args.limit:
        cases = cases[: args.limit]

    results = []
    for case in cases:
        results.append(await _run_case(case, runtime=args.runtime))

    evaluation_report = generate_evaluation_report(results)
    success_rate = evaluation_report.get("success_rate", 0)
    quality_score = {
        "score": round(success_rate),
        "grade": "A" if success_rate >= 90 else "B" if success_rate >= 80 else "C" if success_rate >= 70 else "F",
        "success_rate": success_rate,
        "average_latency_seconds": mean([r["latency"] for r in results]) if results else 0,
        "total_repairs": sum(r.get("repair_counts", 0) for r in results),
        "total_provider_fallbacks": sum(r.get("provider_fallbacks", 0) for r in results),
        "total_provider_switches": sum(r.get("provider_switches", 0) for r in results),
        "total_quota_failures": sum(r.get("quota_failures", 0) for r in results),
        "total_retries": sum(r.get("repair_counts", 0) + r.get("provider_fallbacks", 0) for r in results),
        "total_runtime_failures": sum(r.get("runtime_failures", 0) for r in results),
        "total_validation_failures": sum(r.get("validation_failures", 0) for r in results),
    }
    failure_report = {
        "taxonomy": tracker.snapshot(),
        "failed_runs": [r for r in results if not r.get("success")],
    }

    _write_json("quality_score.json", quality_score)
    _write_json("failure_report.json", failure_report)

    return {
        "evaluation_report": evaluation_report,
        "quality_score": quality_score,
        "failure_report": failure_report,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run AI App Compiler benchmark suite.")
    parser.add_argument("--runtime", action="store_true", help="Run full runtime validation for each case.")
    parser.add_argument("--offline", action="store_true", default=True, help="Use deterministic local provider for demo-safe runs.")
    parser.add_argument("--live-providers", action="store_false", dest="offline", help="Use configured cloud providers.")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of benchmark cases.")
    parser.add_argument("--include-prompts", action="store_true", default=True)
    parser.add_argument("--include-edge-cases", action="store_true", default=True)
    return parser.parse_args()


if __name__ == "__main__":
    report = asyncio.run(run_benchmarks(parse_args()))
    print(json.dumps({
        "success_rate": report["quality_score"]["success_rate"],
        "score": report["quality_score"]["score"],
        "grade": report["quality_score"]["grade"],
    }, indent=2))
