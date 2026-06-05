import asyncio
import os
import time
from runtime.process_manager import process_manager
from runtime.health_checker import check_http_status
from utils.logger import app_logger

async def run_frontend(project_dir: str, port: int) -> dict:
    """Installs dependencies and runs the frontend to validate execution."""
    frontend_dir = os.path.join(project_dir, "frontend")
    
    if not os.path.exists(frontend_dir):
        return {"success": False, "error": "Frontend directory not found"}
        
    start_time = time.time()
    
    try:
        app_logger.info("Installing frontend dependencies...")
        install_proc = await asyncio.create_subprocess_shell(
            "npm install --no-audit --no-fund",
            cwd=frontend_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        try:
            await asyncio.wait_for(install_proc.wait(), timeout=120)
        except asyncio.TimeoutError:
            install_proc.kill()
            await install_proc.wait()
            return {"success": False, "error": "npm install timed out after 120 seconds"}
        
        if install_proc.returncode != 0:
            stdout, stderr = await install_proc.communicate()
            return {"success": False, "error": f"npm install failed: {stderr.decode(errors='replace')[-1500:]}\n{stdout.decode(errors='replace')[-500:]}"}

        build_proc = await asyncio.create_subprocess_shell(
            "npm run build",
            cwd=frontend_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        try:
            await asyncio.wait_for(build_proc.wait(), timeout=120)
        except asyncio.TimeoutError:
            build_proc.kill()
            await build_proc.wait()
            return {"success": False, "error": "npm run build timed out after 120 seconds"}

        if build_proc.returncode != 0:
            stdout, stderr = await build_proc.communicate()
            return {"success": False, "error": f"npm run build failed: {stderr.decode(errors='replace')[-1500:]}\n{stdout.decode(errors='replace')[-1500:]}"}

        app_logger.info(f"Starting frontend preview on port {port}...")
        run_proc = await asyncio.create_subprocess_shell(
            f"npm run preview -- --host 127.0.0.1 --port {port} --strictPort",
            cwd=frontend_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        process_manager.register_process(run_proc, f"frontend_{port}")
        
        is_up = await check_http_status(f"http://127.0.0.1:{port}/", timeout=60)
        
        if not is_up:
            try:
                if run_proc.returncode is not None:
                    stdout, stderr = await run_proc.communicate()
                    err_log = stderr.decode(errors="replace") + "\\n" + stdout.decode(errors="replace")
                else:
                    err_log = "Process hung."
            except Exception:
                err_log = "Failed to capture logs."
            return {"success": False, "error": f"Frontend failed health check. Logs: {err_log[-1500:]}"}
            
        return {
            "success": True,
            "startup_time": time.time() - start_time,
            "port": port,
            "url": f"http://127.0.0.1:{port}",
        }
        
    except Exception as e:
        return {"success": False, "error": f"Frontend validation failed: {str(e)}"}
