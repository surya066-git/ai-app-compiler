import re

def attempt_import_repair(filepath: str, content: str, error_msg: str) -> str:
    """Attempts to deterministically fix missing Python imports."""
    missing_imports = {
        "name 'os' is not defined": "import os",
        "name 'json' is not defined": "import json",
        "name 'FastAPI' is not defined": "from fastapi import FastAPI",
        "name 'APIRouter' is not defined": "from fastapi import APIRouter",
        "name 'Depends' is not defined": "from fastapi import Depends",
        "name 'HTTPException' is not defined": "from fastapi import HTTPException",
        "name 'BaseModel' is not defined": "from pydantic import BaseModel",
    }
    for marker, import_line in missing_imports.items():
        if marker in error_msg and import_line not in content:
            return f"{import_line}\n{content}"
            
    return content
