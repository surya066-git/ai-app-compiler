import json
import os
from config.settings import settings

class FailureTaxonomyTracker:
    def __init__(self):
        self.failures = {
            "syntax": 0,
            "consistency": 0,
            "execution": 0,
            "runtime": 0,
            "schema": 0,
            "security": 0,
            "repair_failed": 0,
            "ambiguity": 0
        }
        self.log_path = os.path.join(settings.STORAGE_DIR, "failure_report.json")
        
    def record(self, category: str):
        if category in self.failures:
            self.failures[category] += 1
            self._save()
            
    def _save(self):
        os.makedirs(settings.STORAGE_DIR, exist_ok=True)
        with open(self.log_path, "w") as f:
            json.dump(self.failures, f, indent=4)

    def snapshot(self):
        return dict(self.failures)
            
tracker = FailureTaxonomyTracker()
