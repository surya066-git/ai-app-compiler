from repair.import_repair import attempt_import_repair
from repair.route_repair import attempt_route_repair
from repair.retry_engine import attempt_llm_retry
from llm.base_provider import BaseProvider
from evaluation.failure_taxonomy import tracker
from exceptions.generation_exceptions import RepairFailedException
import re

async def repair_project(files: dict, error: Exception, provider: BaseProvider, trace: list | None = None) -> dict:
    """Attempts to repair a project that failed validation or sandbox execution."""
    error_str = str(error)
    error_details = getattr(error, "details", {}) or {}
    repaired_files = files.copy()
    trace = trace if trace is not None else []
    
    # 1. Deterministic Import Repair
    if "import" in error_str.lower() or "not defined" in error_str:
        target_file = error_details.get("filepath") or _filepath_from_error(error_str)
        for filepath, content in repaired_files.items():
            if filepath.endswith(".py"):
                if target_file and filepath != target_file:
                    continue
                new_content = attempt_import_repair(filepath, content, error_str)
                if new_content != content:
                    trace.append({
                        "type": "import_repair",
                        "file": filepath,
                        "error": error_str,
                        "status": "applied",
                    })
                repaired_files[filepath] = new_content
                
    # 2. Deterministic Route Repair
    elif "404" in error_str or "route" in error_str.lower():
        if "backend/main.py" in repaired_files:
            missing_route = error_details.get("route", error_str)
            method = error_details.get("method", "get")
            repaired_files["backend/main.py"] = attempt_route_repair(
                "backend/main.py",
                repaired_files["backend/main.py"],
                missing_route,
                method,
            )
            trace.append({
                "type": "route_repair",
                "file": "backend/main.py",
                "error": error_str,
                "route": missing_route,
                "method": method,
                "status": "applied",
            })

    # 3. Deterministic Dependency Repair
    elif "requirements.txt" in error_str or "runtime dependencies" in error_str.lower():
        requirements = repaired_files.get("backend/requirements.txt", "")
        required = ["fastapi", "uvicorn"]
        missing = [package for package in required if package not in requirements]
        if missing:
            repaired_files["backend/requirements.txt"] = requirements.rstrip() + "\n" + "\n".join(missing) + "\n"
            trace.append({
                "type": "dependency_repair",
                "file": "backend/requirements.txt",
                "error": error_str,
                "packages_added": missing,
                "status": "applied",
            })

    # 4. Frontend/backend API configuration repair
    elif "frontend/backend inconsistency" in error_str.lower() or "vite_api_url" in error_str.lower():
        repaired_files["frontend/src/api.js"] = """
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
});

export default api;
"""
        trace.append({
            "type": "frontend_backend_consistency_repair",
            "file": "frontend/src/api.js",
            "error": error_str,
            "status": "applied",
        })

    # 5. Runtime missing package repair
    elif "modulenotfounderror" in error_str.lower() or "no module named" in error_str.lower():
        package = _package_for_missing_module(error_str)
        if package:
            requirements = repaired_files.get("backend/requirements.txt", "")
            if package not in requirements:
                repaired_files["backend/requirements.txt"] = requirements.rstrip() + f"\n{package}\n"
            trace.append({
                "type": "runtime_dependency_repair",
                "file": "backend/requirements.txt",
                "error": error_str,
                "packages_added": [package],
                "status": "applied",
            })
            
    # 6. LLM Retry Fallback
    else:
        # If we know exactly which file failed, we retry it. Otherwise, we might retry main.py
        # For this compiler, we simulate repairing the backend entrypoint as it's the most common failure point
        if "backend/main.py" in repaired_files:
            try:
                new_main = await attempt_llm_retry(repaired_files["backend/main.py"], error_str, provider)
                repaired_files["backend/main.py"] = new_main
                trace.append({
                    "type": "provider_retry",
                    "file": "backend/main.py",
                    "error": error_str,
                    "status": "applied",
                })
            except RepairFailedException:
                tracker.record("repair_failed")
                trace.append({
                    "type": "provider_retry",
                    "file": "backend/main.py",
                    "error": error_str,
                    "status": "failed",
                })
                raise
                
    return repaired_files


def _package_for_missing_module(error_str: str) -> str | None:
    lowered = error_str.lower()
    package_map = {
        "jose": "python-jose[cryptography]==3.3.0",
        "passlib": "passlib[bcrypt]==1.7.4",
        "sqlalchemy": "sqlalchemy==2.0.27",
        "multipart": "python-multipart==0.0.9",
        "pydantic": "pydantic==2.6.1",
        "fastapi": "fastapi==0.109.2",
        "uvicorn": "uvicorn==0.27.1",
    }
    for module, package in package_map.items():
        if module in lowered:
            return package
    return None


def _filepath_from_error(error_str: str) -> str | None:
    match = re.search(r"in\s+(backend/[A-Za-z0-9_./-]+\.py):", error_str)
    if match:
        return match.group(1)
    return None
