import re


def attempt_route_repair(filepath: str, content: str, missing_route: str, method: str = "get") -> str:
    """Injects a missing route stub into a FastAPI router file."""
    route_path = _route_path(missing_route)
    route_slug = route_path.strip("/").replace("/", "_").replace("{", "").replace("}", "") or "root"
    safe_function = re.sub(r"[^a-zA-Z0-9_]", "_", route_slug)
    method = method.lower() if method.lower() in {"get", "post", "put", "patch", "delete"} else "get"
    args = "id: int" if "{id}" in route_path else ""

    if filepath.endswith(".py") and "router = APIRouter" in content:
        stub = f"""
@router.{method}("{route_path}")
def auto_repaired_{safe_function}({args}):
    return {{"message": "Auto-repaired endpoint", "route": "{route_path}"}}
"""
        return content + stub
    if filepath.endswith(".py") and "app = FastAPI" in content:
        stub = f"""
@app.{method}("{route_path}")
def auto_repaired_{safe_function}({args}):
    return {{"message": "Auto-repaired endpoint", "route": "{route_path}"}}
"""
        return content + stub
    return content


def _route_path(message: str) -> str:
    match = re.search(r"(/[a-zA-Z0-9_/{}/.-]+)", message)
    if match:
        return match.group(1).rstrip(".")
    return "/health"
