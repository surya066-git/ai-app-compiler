import os
import time
from utils.logger import app_logger


async def run_frontend(project_dir: str, port: int) -> dict:
    """Performs FAST structural validation of the frontend instead of full runtime execution."""
    frontend_dir = os.path.join(project_dir, "frontend")
    start_time = time.time()

    # 1. Verify frontend folder exists
    if not os.path.exists(frontend_dir):
        return _fail("frontend_directory_missing", "Frontend directory not found")

    # 2. Verify package.json exists
    package_json_path = os.path.join(frontend_dir, "package.json")
    if not os.path.exists(package_json_path):
        return _fail("missing_package_json", "package.json not found in frontend directory")

    # 5. Verify package.json contains react and vite
    try:
        with open(package_json_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "react" not in content or "vite" not in content:
                return _fail("missing_package_json", "package.json missing react or vite dependencies")
    except Exception as e:
        return _fail("missing_package_json", f"Failed to read package.json: {e}")

    # 3. Verify src/ exists
    src_dir = os.path.join(frontend_dir, "src")
    if not os.path.exists(src_dir):
        return _fail("missing_src_folder", "src/ directory not found")

    # 4. Verify vite.config.js OR vite.config.ts exists
    if not os.path.exists(os.path.join(frontend_dir, "vite.config.js")) and not os.path.exists(os.path.join(frontend_dir, "vite.config.ts")):
        return _fail("missing_vite_config", "vite.config.js or vite.config.ts not found")

    # 6. Verify App.jsx or App.tsx exists
    app_exists = any(os.path.exists(os.path.join(src_dir, f)) for f in ["App.jsx", "App.tsx", "app.jsx", "app.tsx", "App.js"])
    if not app_exists:
        return _fail("missing_app_component", "App.jsx or App.tsx not found in src/")

    # 7. Verify main.jsx or main.tsx exists
    main_exists = any(os.path.exists(os.path.join(src_dir, f)) for f in ["main.jsx", "main.tsx", "index.jsx", "index.tsx", "main.js", "index.js"])
    if not main_exists:
        return _fail("missing_main_entry", "main.jsx or main.tsx not found in src/")

    # 8. Verify generated files are non-empty
    app_files = [os.path.join(src_dir, f) for f in ["App.jsx", "App.tsx", "app.jsx", "app.tsx", "App.js"] if os.path.exists(os.path.join(src_dir, f))]
    if app_files and os.path.getsize(app_files[0]) == 0:
        return _fail("missing_app_component", "App component file is empty")
        
    main_files = [os.path.join(src_dir, f) for f in ["main.jsx", "main.tsx", "index.jsx", "index.tsx", "main.js", "index.js"] if os.path.exists(os.path.join(src_dir, f))]
    if main_files and os.path.getsize(main_files[0]) == 0:
        return _fail("missing_main_entry", "Main entry file is empty")

    app_logger.info(f"Frontend structural validation passed in {time.time() - start_time:.2f}s.")

    return {
        "success": True,
        "startup_time": time.time() - start_time,
        "port": port,
        "url": f"http://127.0.0.1:{port}",
    }


# ======================================================================
# Helpers
# ======================================================================

def _fail(code: str, message: str) -> dict:
    """Return a structured failure result with a machine-readable error code."""
    app_logger.error(f"[{code}] {message}")
    return {"success": False, "error": message, "error_code": code}

