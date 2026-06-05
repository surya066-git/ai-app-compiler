from contracts.app_ir_schema import AppIR
from llm.base_provider import BaseProvider
from generators.ui_generator import generate_ui_components
from templates.react_templates import *
from utils.security import sanitize_filename
import re

async def generate_frontend_system(ir: AppIR, provider: BaseProvider) -> dict:
    """Generates the full React Vite frontend based on IR."""
    app_name_slug = sanitize_filename(ir.app_name.lower().replace(" ", "-"))
    
    files = {}
    files["frontend/vite.config.js"] = VITE_CONFIG
    files["frontend/package.json"] = PACKAGE_JSON.replace("{app_name_slug}", app_name_slug)
    files["frontend/index.html"] = INDEX_HTML.replace("{app_name}", ir.app_name)
    files["frontend/tailwind.config.js"] = TAILWIND_CONFIG
    files["frontend/postcss.config.js"] = POSTCSS_CONFIG
    files["frontend/src/main.jsx"] = MAIN_JSX
    files["frontend/src/index.css"] = INDEX_CSS
    files["frontend/src/api.js"] = API_JS
    files["frontend/src/store.js"] = STORE_JS
    
    pages_list = [p.name for p in ir.pages]
    ui_files = await generate_ui_components(pages_list, provider)
    
    for filename, content in ui_files.items():
        files[f"frontend/src/components/{filename}"] = content
        
    # App.jsx routing
    route_defs = [(_component_name(page.name), _route_path(page.route, page.name)) for page in ir.pages]
    imports = "\n".join([f"import {component} from './components/{component}.jsx';" for component, _ in route_defs])
    routes = []
    if route_defs:
        first_component = route_defs[0][0]
        routes.append(f"            <Route path='/' element={{<{first_component} />}} />")
    routes.extend([f"            <Route path='{route}' element={{<{component} />}} />" for component, route in route_defs])
    routes_jsx = "\n".join(routes)
    files["frontend/src/App.jsx"] = APP_JSX_TEMPLATE.replace("{imports}", imports).replace("{routes}", routes_jsx)
    
    return files


def _component_name(value: str) -> str:
    words = re.findall(r"[A-Za-z0-9]+", value or "")
    return "".join(word[:1].upper() + word[1:] for word in words) or "Dashboard"


def _route_path(route: str, fallback_name: str) -> str:
    route = (route or "").strip()
    if not route:
        route = "/" + re.sub(r"[^a-z0-9]+", "-", fallback_name.lower()).strip("-")
    if not route.startswith("/"):
        route = f"/{route}"
    return route
