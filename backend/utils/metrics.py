import time
import json
import os
from typing import Dict, Any

class MetricsTracker:
    def __init__(self):
        self.metrics = {
            "start_time": time.time(),
            "end_time": None,
            "latency": None,
            "provider_fallbacks": 0,
            "repair_counts": 0,
            "validation_failures": 0,
            "runtime_failures": 0,
            "stages_completed": [],
            "provider_latency": {}
        }

    def record_stage(self, stage: str):
        self.metrics["stages_completed"].append(stage)
        
    def increment_fallback(self):
        self.metrics["provider_fallbacks"] += 1
        
    def increment_repair(self):
        self.metrics["repair_counts"] += 1

    def increment_validation_failure(self):
        self.metrics["validation_failures"] += 1
        
    def increment_runtime_failure(self):
        self.metrics["runtime_failures"] += 1
        
    def record_provider_latency(self, provider: str, latency: float):
        if provider not in self.metrics["provider_latency"]:
            self.metrics["provider_latency"][provider] = []
        self.metrics["provider_latency"][provider].append(latency)

    def finish(self) -> Dict[str, Any]:
        self.metrics["end_time"] = time.time()
        self.metrics["latency"] = self.metrics["end_time"] - self.metrics["start_time"]
        return self.metrics

    def save_metrics(self, output_path: str):
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.finish(), f, indent=4)
