import json
import os
from config.settings import settings

def generate_evaluation_report(metrics_list: list, output_filename: str = "evaluation_report.json"):
    """
    Generates an evaluation report aggregating multiple execution metrics.
    """
    total_runs = len(metrics_list)
    if total_runs == 0:
        return {}

    total_latency = sum(m.get("latency", 0) for m in metrics_list)
    total_fallbacks = sum(m.get("provider_fallbacks", 0) for m in metrics_list)
    total_provider_switches = sum(m.get("provider_switches", 0) for m in metrics_list)
    total_quota_failures = sum(m.get("quota_failures", 0) for m in metrics_list)
    total_repairs = sum(m.get("repair_counts", 0) for m in metrics_list)
    total_validation_failures = sum(m.get("validation_failures", 0) for m in metrics_list)
    total_runtime_failures = sum(m.get("runtime_failures", 0) for m in metrics_list)
    total_retries = total_repairs + total_fallbacks
    
    success_count = sum(1 for m in metrics_list if m.get("runtime_failures", 0) == 0 and m.get("latency", 0) > 0)

    report = {
        "total_evaluations": total_runs,
        "success_rate": (success_count / total_runs) * 100,
        "average_latency_seconds": total_latency / total_runs,
        "average_repairs_per_run": total_repairs / total_runs,
        "total_retries": total_retries,
        "total_provider_fallbacks": total_fallbacks,
        "total_provider_switches": total_provider_switches,
        "total_quota_failures": total_quota_failures,
        "total_validation_failures": total_validation_failures,
        "total_runtime_failures": total_runtime_failures,
        "runs": metrics_list
    }

    os.makedirs(settings.EXPORT_DIR, exist_ok=True)
    report_path = os.path.join(settings.EXPORT_DIR, output_filename)
    
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
        
    return report
