from llm.base_provider import BaseProvider
from generators.auth_generator import generate_auth_routes, generate_security_file
from generators.database_generator import generate_database_schema
from generators.ui_generator import generate_ui_components
from templates.react_templates import *
from templates.fastapi_templates import *
from templates.docker_templates import *
from templates.misc_templates import *
from utils.security import sanitize_filename
import re

async def generate_project(architecture: dict, provider: BaseProvider) -> dict:
    """Assembles all templates and generated code into a complete file map."""
    
    app_name = architecture.get("app_name", "GeneratedApp")
    app_name_slug = sanitize_filename(app_name.lower().replace(" ", "-"))
    db_name = f"{app_name_slug}_db"
    
    files = {}
    
    # --- Backend Generation ---
    security_files = generate_security_file()
    files["backend/security.py"] = security_files["security.py"]
    jwt_secret = security_files["jwt_secret"]
    
    files["backend/auth.py"] = generate_auth_routes()
    
    db_files = await generate_database_schema(architecture.get("database_tables", []), provider)
    files["backend/database.py"] = db_files["database.py"]
    files["backend/models.py"] = db_files["models.py"]
    
    # Generate main.py routes dynamically
    routes = architecture.get("pages", [])
    router_imports = ""
    router_includes = ""
    
    for route in routes:
        route_slug = _safe_identifier(route)
        # Basic stub routers for each page entity
        files[f"backend/routers/{route_slug}.py"] = f"""
from fastapi import APIRouter
router = APIRouter()
@router.get("/")
def get_{route_slug}():
    return {{"message": "{route_slug} endpoint"}}
"""
        router_imports += f"from routers import {route_slug}\n"
        router_includes += f"app.include_router({route_slug}.router, prefix='/{route_slug}', tags=['{route_slug}'])\n"
        
    # main.py
    files["backend/main.py"] = MAIN_PY_TEMPLATE.replace("{app_name}", app_name).replace("{router_imports}", router_imports).replace("{router_includes}", router_includes)
    
    # Requirements
    files["backend/requirements.txt"] = REQUIREMENTS_TXT
    
    
    # --- Frontend Generation ---
    files["frontend/vite.config.js"] = VITE_CONFIG
    files["frontend/package.json"] = PACKAGE_JSON.replace("{app_name_slug}", app_name_slug)
    files["frontend/index.html"] = INDEX_HTML.replace("{app_name}", app_name)
    files["frontend/tailwind.config.js"] = TAILWIND_CONFIG
    files["frontend/postcss.config.js"] = POSTCSS_CONFIG
    files["frontend/src/main.jsx"] = MAIN_JSX
    files["frontend/src/index.css"] = INDEX_CSS
    files["frontend/src/api.js"] = API_JS
    files["frontend/src/store.js"] = STORE_JS
    
    ui_files = await generate_ui_components(architecture.get("pages", []), provider)
    for filename, content in ui_files.items():
        files[f"frontend/src/components/{filename}"] = content
        
    # App.jsx routing
    route_defs = [(_component_name(p), "/" + _safe_identifier(p).replace("_", "-")) for p in routes]
    imports = "\n".join([f"import {component} from './components/{component}.jsx';" for component, _ in route_defs])
    routes_jsx = "\n".join([f"            <Route path='{route}' element={{<{component} />}} />" for component, route in route_defs])
    files["frontend/src/App.jsx"] = APP_JSX_TEMPLATE.replace("{imports}", imports).replace("{routes}", routes_jsx)
    
    # --- DevOps & Misc ---
    files["docker-compose.yml"] = DOCKER_COMPOSE.replace("{db_name}", db_name).replace("{jwt_secret}", jwt_secret)
    files["backend/Dockerfile"] = DOCKERFILE_BACKEND
    files["frontend/Dockerfile"] = DOCKERFILE_FRONTEND
    
    files[".env.example"] = ENV_EXAMPLE.replace("{db_name}", db_name).replace("{jwt_secret}", jwt_secret)
    files[".gitignore"] = GITIGNORE
    files["README.md"] = README_MD.replace("{app_name}", app_name)
    
    return files


def _safe_identifier(value: str) -> str:
    identifier = re.sub(r"[^a-zA-Z0-9_]", "_", str(value).strip().lower())
    identifier = re.sub(r"_+", "_", identifier).strip("_")
    if not identifier:
        return "route"
    if identifier[0].isdigit():
        identifier = f"route_{identifier}"
    return identifier


def _component_name(value: str) -> str:
    words = re.findall(r"[A-Za-z0-9]+", str(value))
    return "".join(word[:1].upper() + word[1:] for word in words) or "Dashboard"
