import json
from exceptions.generation_exceptions import ValidationException

def validate_execution_readiness(files: dict):
    """Ensures necessary execution files are present and valid."""
    required_files = [
        "backend/main.py",
        "backend/requirements.txt",
        "backend/database.py",
        "backend/models.py",
        "backend/auth.py",
        "frontend/package.json",
        "frontend/src/main.jsx",
        "frontend/src/App.jsx",
        "frontend/src/api.js",
        "docker-compose.yml",
    ]
    for filepath in required_files:
        if filepath not in files:
            raise ValidationException(f"Missing required execution file: {filepath}")
    
    try:
        package_json = json.loads(files["frontend/package.json"])
    except json.JSONDecodeError:
        raise ValidationException("frontend/package.json is invalid JSON")

    scripts = package_json.get("scripts", {})
    if "dev" not in scripts or "build" not in scripts:
        raise ValidationException("frontend/package.json missing dev/build scripts")

    requirements = files["backend/requirements.txt"]
    if "fastapi" not in requirements or "uvicorn" not in requirements:
        raise ValidationException("backend/requirements.txt missing FastAPI runtime dependencies")

    main_py = files["backend/main.py"]
    if "app = FastAPI" not in main_py or '@app.get("/")' not in main_py:
        raise ValidationException("backend/main.py missing FastAPI app or root health route")

    api_js = files["frontend/src/api.js"]
    if "VITE_API_URL" not in api_js and "localhost:8000" not in api_js:
        raise ValidationException(
            "frontend/backend inconsistency: frontend API client is not configurable",
            details={"filepath": "frontend/src/api.js"},
        )
        
    return True
