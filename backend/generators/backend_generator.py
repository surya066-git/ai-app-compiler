from contracts.app_ir_schema import AppIR
from llm.base_provider import BaseProvider
from generators.auth_generator import generate_auth_routes, generate_security_file
from generators.database_generator import generate_database_schema
from templates.fastapi_templates import MAIN_PY_TEMPLATE, REQUIREMENTS_TXT
import re

async def generate_backend_system(ir: AppIR, provider: BaseProvider) -> dict:
    """Generates the full FastAPI backend based on IR."""
    files = {}
    
    # Auth & Security
    security_files = generate_security_file()
    files["backend/security.py"] = security_files["security.py"]
    jwt_secret = security_files["jwt_secret"]
    files["backend/auth.py"] = generate_auth_routes()
    
    # DB
    tables = [t.name for t in ir.tables]
    db_files = await generate_database_schema(tables, provider)
    files["backend/database.py"] = db_files["database.py"]
    files["backend/models.py"] = db_files["models.py"]
    
    # Routers
    router_imports = ""
    router_includes = ""
    files["backend/routers/__init__.py"] = ""
    seen_route_modules = set()
    for endpoint in ir.endpoints:
        method = endpoint.method.lower()
        if method not in {"get", "post", "put", "patch", "delete"}:
            method = "get"
        route_slug = _safe_identifier(f"{method}_{endpoint.path.strip('/').replace('/', '_')}")
        if not route_slug:
            continue
        route_path = endpoint.path if endpoint.path.startswith("/") else f"/{endpoint.path}"
        function_args = _path_function_args(route_path)
        files[f"backend/routers/{route_slug}.py"] = f"""
from fastapi import APIRouter
router = APIRouter()

@router.{method}("{route_path}")
def handle_{route_slug}({function_args}):
    return {{"message": "{endpoint.description}", "route": "{route_path}"}}
"""
        if route_slug not in seen_route_modules:
            seen_route_modules.add(route_slug)
            router_imports += f"from routers import {route_slug}\n"
            router_includes += f"app.include_router({route_slug}.router, tags=['{route_slug}'])\n"
            
    # main.py
    files["backend/main.py"] = MAIN_PY_TEMPLATE.replace("{app_name}", ir.app_name).replace("{router_imports}", router_imports).replace("{router_includes}", router_includes)
    files["backend/requirements.txt"] = REQUIREMENTS_TXT
    
    return files, jwt_secret


def _safe_identifier(value: str) -> str:
    identifier = re.sub(r"[^a-zA-Z0-9_]", "_", value.strip().lower())
    identifier = re.sub(r"_+", "_", identifier).strip("_")
    if not identifier:
        return "route"
    if identifier[0].isdigit():
        identifier = f"route_{identifier}"
    return identifier


def _path_function_args(route_path: str) -> str:
    args = []
    for name in re.findall(r"{([^{}]+)}", route_path):
        clean_name = _safe_identifier(name)
        arg_type = "int" if clean_name == "id" or clean_name.endswith("_id") else "str"
        args.append(f"{clean_name}: {arg_type}")
    return ", ".join(args)
