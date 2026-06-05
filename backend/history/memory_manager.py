import json
import os
from datetime import datetime
import uuid
from config.settings import settings

class MemoryManager:
    def __init__(self):
        self.storage_dir = settings.STORAGE_DIR
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir, exist_ok=True)

    def save_generation_metadata(self, prompt: str, architecture: dict, provider: str) -> str:
        """Saves generation metadata and returns a unique generation_id."""
        generation_id = str(uuid.uuid4())
        
        metadata = {
            "generation_id": generation_id,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "prompt": prompt,
            "architecture": architecture,
            "provider": provider,
            "version": "1.0.0"
        }
        
        file_path = os.path.join(self.storage_dir, f"{generation_id}.json")
        with open(file_path, "w") as f:
            json.dump(metadata, f, indent=4)
            
        return generation_id

    def load_generation_metadata(self, generation_id: str) -> dict:
        """Loads previous generation metadata."""
        file_path = os.path.join(self.storage_dir, f"{generation_id}.json")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Generation ID {generation_id} not found.")
            
        with open(file_path, "r") as f:
            return json.load(f)
