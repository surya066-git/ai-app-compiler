from runtime.backend_runner import run_backend
from runtime.frontend_runner import run_frontend
from runtime.process_manager import process_manager
from runtime.health_checker import fetch_text, post_form, post_json
import asyncio
import json
import os
import time

async def execute_sandbox(project_dir: str) -> dict:
    """
    Coordinates the execution sandbox.
    Returns {"success": bool, "errors": list}
    """
    errors = []
    
    backend_port = process_manager.get_free_port()
    frontend_port = process_manager.get_free_port()
    
    try:
        # Run concurrently for speed
        backend_task = asyncio.create_task(run_backend(project_dir, backend_port))
        frontend_task = asyncio.create_task(run_frontend(project_dir, frontend_port))
        
        backend_res, frontend_res = await asyncio.gather(backend_task, frontend_task)
        
        if not backend_res.get("success"):
            errors.append(f"Backend Sandbox Error: {backend_res.get('error')}")
            
        if not frontend_res.get("success"):
            errors.append(f"Frontend Sandbox Error: {frontend_res.get('error')}")

        health_report = {
            "success": False,
            "checks": [],
            "backend_url": backend_res.get("url"),
            "frontend_url": frontend_res.get("url"),
        }

        if not errors:
            health_report = await _run_health_checks(project_dir, backend_res["url"], frontend_res["url"])
            if not health_report["success"]:
                errors.append("Health verification failed")
            
        metrics = {
            "backend_startup_time": backend_res.get("startup_time"),
            "frontend_startup_time": frontend_res.get("startup_time"),
            "success": len(errors) == 0,
            "backend_url": backend_res.get("url"),
            "frontend_url": frontend_res.get("url"),
            "health_success": health_report.get("success", False),
            "errors": errors,
        }
        
        try:
            with open(os.path.join(project_dir, "runtime_metrics.json"), "w") as f:
                json.dump(metrics, f, indent=2)
            with open(os.path.join(project_dir, "health_report.json"), "w") as f:
                json.dump(health_report, f, indent=2)
        except Exception:
            pass
            
        if errors:
            return {"success": False, "errors": errors, "health_report": health_report, "metrics": metrics}
            
        return {"success": True, "errors": [], "health_report": health_report, "metrics": metrics}
        
    finally:
        await process_manager.cleanup_all()


async def _run_health_checks(project_dir: str, backend_url: str, frontend_url: str) -> dict:
    checks = []

    async def add_check(name: str, success: bool, details=None):
        checks.append({"name": name, "success": bool(success), "details": details or {}})

    backend_ok, backend_body = await fetch_text(f"{backend_url}/", timeout=10)
    await add_check("backend_reachable", backend_ok and '"status"' in backend_body, {"url": f"{backend_url}/"})

    docs_ok, _ = await fetch_text(f"{backend_url}/docs", timeout=10)
    await add_check("backend_docs_reachable", docs_ok, {"url": f"{backend_url}/docs"})

    openapi_ok, openapi_body = await fetch_text(f"{backend_url}/openapi.json", timeout=10)
    registered_paths = []
    if openapi_ok:
        try:
            registered_paths = sorted(json.loads(openapi_body).get("paths", {}).keys())
        except Exception:
            registered_paths = []
    await add_check("api_routes_registered", bool(registered_paths), {"paths": registered_paths[:20]})

    username = f"demo_{int(time.time() * 1000)}"
    signup_ok, signup_body = await post_json(
        f"{backend_url}/auth/signup",
        {"username": username, "password": "CompilerDemo123!"},
    )
    await add_check("auth_signup_functional", signup_ok, {"response": signup_body})

    login_ok, login_body = await post_form(
        f"{backend_url}/auth/login",
        {"username": username, "password": "CompilerDemo123!"},
    )
    await add_check("auth_login_functional", login_ok and "access_token" in login_body, {"token_returned": "access_token" in login_body})

    frontend_ok, frontend_body = await fetch_text(f"{frontend_url}/", timeout=20)
    await add_check("frontend_reachable", frontend_ok and "root" in frontend_body, {"url": f"{frontend_url}/"})

    api_file = os.path.join(project_dir, "frontend", "src", "api.js")
    api_configured = False
    if os.path.exists(api_file):
        with open(api_file, "r", encoding="utf-8") as f:
            api_configured = "VITE_API_URL" in f.read()
    await add_check(
        "frontend_backend_communication_configured",
        api_configured and backend_ok,
        {"api_file": "frontend/src/api.js", "backend_url": backend_url},
    )

    return {
        "success": all(check["success"] for check in checks),
        "checks": checks,
        "backend_url": backend_url,
        "frontend_url": frontend_url,
    }
