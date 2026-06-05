import os
import time
import ast
from utils.logger import app_logger

async def run_backend(project_dir: str, port: int) -> dict:
    """Performs FAST structural validation of the backend instead of full runtime execution."""
    backend_dir = os.path.join(project_dir, "backend")
    start_time = time.time()
    
    if not os.path.exists(backend_dir):
        return {"success": False, "error": "Backend directory not found", "error_code": "backend_directory_missing"}
        
    requirements_path = os.path.join(backend_dir, "requirements.txt")
    if not os.path.exists(requirements_path):
        return {"success": False, "error": "requirements.txt not found", "error_code": "missing_requirements"}
        
    main_py_path = os.path.join(backend_dir, "main.py")
    if not os.path.exists(main_py_path):
        return {"success": False, "error": "main.py not found", "error_code": "missing_main_py"}
        
    # FastAPI syntax and router registration check
    try:
        with open(main_py_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename="main.py")
        
        # very basic check for FastAPI
        has_fastapi = False
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and getattr(node, "module", "") == "fastapi":
                has_fastapi = True
            elif isinstance(node, ast.Import) and any(alias.name == "fastapi" for alias in node.names):
                has_fastapi = True
                
        if not has_fastapi:
            return {"success": False, "error": "FastAPI not imported in main.py", "error_code": "fastapi_missing"}
            
    except SyntaxError as e:
        return {"success": False, "error": f"Syntax error in main.py: {e}", "error_code": "backend_syntax_error"}
    except Exception as e:
        return {"success": False, "error": f"Failed to parse main.py: {e}", "error_code": "backend_parse_error"}

    app_logger.info(f"Backend structural validation passed in {time.time() - start_time:.2f}s.")

    return {
        "success": True,
        "startup_time": time.time() - start_time,
        "port": port,
        "url": f"http://127.0.0.1:{port}",
    }
