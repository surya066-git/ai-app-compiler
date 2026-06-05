import os
import json
from utils.security import ensure_safe_path

def write_project_files(project_dir: str, files: dict, metadata: dict) -> None:
    """
    Writes all files safely to disk and generates a project.json.
    """
    if not os.path.exists(project_dir):
        os.makedirs(project_dir, exist_ok=True)
        
    # Write all files
    for filepath, content in files.items():
        full_path = ensure_safe_path(project_dir, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
            
    # Write metadata
    metadata_path = ensure_safe_path(project_dir, "project.json")
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)
