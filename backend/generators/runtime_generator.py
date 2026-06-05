from contracts.app_ir_schema import AppIR
from templates.docker_templates import DOCKER_COMPOSE, DOCKERFILE_BACKEND, DOCKERFILE_FRONTEND
from templates.misc_templates import ENV_EXAMPLE, GITIGNORE, README_MD
from utils.security import sanitize_filename

def generate_runtime_system(ir: AppIR, jwt_secret: str) -> dict:
    """Generates Docker, Env, Git, and Readme based on IR."""
    app_name_slug = sanitize_filename(ir.app_name.lower().replace(" ", "-"))
    db_name = f"{app_name_slug}_db"
    
    files = {}
    files["docker-compose.yml"] = DOCKER_COMPOSE.replace("{db_name}", db_name).replace("{jwt_secret}", jwt_secret)
    files["backend/Dockerfile"] = DOCKERFILE_BACKEND
    files["frontend/Dockerfile"] = DOCKERFILE_FRONTEND
    
    files[".env.example"] = ENV_EXAMPLE.replace("{db_name}", db_name).replace("{jwt_secret}", jwt_secret)
    files[".gitignore"] = GITIGNORE
    files["README.md"] = README_MD.replace("{app_name}", ir.app_name)
    
    return files
