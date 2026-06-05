import asyncio
import os
import time
import sys
from config.settings import settings
from runtime.process_manager import process_manager
from runtime.health_checker import check_http_status
from utils.logger import app_logger

async def run_backend(project_dir: str, port: int) -> dict:
    """Attempts to run the backend in a subprocess and validates it starts."""
    backend_dir = os.path.join(project_dir, "backend")
    
    if not os.path.exists(backend_dir):
        return {"success": False, "error": "Backend directory not found"}
        
    start_time = time.time()
    
    try:
        # Install dependencies
        app_logger.info("Installing backend dependencies...")
        install_proc = await asyncio.create_subprocess_shell(
            f"{sys.executable} -m pip install --disable-pip-version-check --prefer-binary -r requirements.txt",
            cwd=backend_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        try:
            await asyncio.wait_for(install_proc.wait(), timeout=180)
        except asyncio.TimeoutError:
            install_proc.kill()
            await install_proc.wait()
            return {"success": False, "error": "pip install timed out after 180 seconds"}
        
        if install_proc.returncode != 0:
            stdout, stderr = await install_proc.communicate()
            return {"success": False, "error": f"pip install failed: {stderr.decode(errors='replace')[-1500:]}\n{stdout.decode(errors='replace')[-500:]}"}
        
        # Start uvicorn
        app_logger.info(f"Starting backend on port {port}...")
        run_proc = await asyncio.create_subprocess_shell(
            f"uvicorn main:app --port {port}",
            cwd=backend_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        process_manager.register_process(run_proc, f"backend_{port}")
        
        # Wait for health check
        is_up = await check_http_status(f"http://127.0.0.1:{port}/", timeout=15)
        
        if not is_up:
            # It failed to start or crashed. Get logs.
            try:
                # Give it a tiny bit to flush
                await asyncio.sleep(1)
                if run_proc.returncode is not None:
                    stdout, stderr = await run_proc.communicate()
                    err_log = stderr.decode(errors="replace") + "\\n" + stdout.decode(errors="replace")
                else:
                    err_log = "Process hung during startup without dying."
            except Exception:
                err_log = "Failed to capture logs."
            return {"success": False, "error": f"Backend failed health check. Logs: {err_log[-1500:]}"}
            
        return {
            "success": True,
            "startup_time": time.time() - start_time,
            "port": port,
            "url": f"http://127.0.0.1:{port}",
        }
        
    except Exception as e:
        return {"success": False, "error": str(e)}
