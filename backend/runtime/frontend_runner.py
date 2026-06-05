import asyncio
import os
import time
from runtime.process_manager import process_manager
from runtime.health_checker import check_http_status
from utils.logger import app_logger


async def run_frontend(project_dir: str, port: int) -> dict:
    """Installs dependencies, builds, and runs the frontend to validate execution."""
    frontend_dir = os.path.join(project_dir, "frontend")

    if not os.path.exists(frontend_dir):
        return _fail("frontend_directory_missing", "Frontend directory not found")

    package_json = os.path.join(frontend_dir, "package.json")
    if not os.path.exists(package_json):
        return _fail("package_json_missing", "package.json not found in frontend directory")

    start_time = time.time()

    # ------------------------------------------------------------------
    # Step 1: Install dependencies
    # ------------------------------------------------------------------
    install_result = await _run_npm_step(
        label="npm install",
        command="npm install --no-audit --no-fund --loglevel=error",
        cwd=frontend_dir,
        timeout=180,
        failure_code="dependency_installation_failed",
    )
    if not install_result["success"]:
        return install_result

    # Verify node_modules was actually created
    node_modules = os.path.join(frontend_dir, "node_modules")
    if not os.path.isdir(node_modules):
        return _fail(
            "dependency_installation_failed",
            "npm install completed but node_modules directory was not created",
        )

    # Verify vite binary is available
    vite_bin = _find_vite_bin(frontend_dir)
    if not vite_bin:
        return _fail(
            "dependency_installation_failed",
            "npm install completed but vite binary not found in node_modules/.bin",
        )

    app_logger.info(f"Frontend dependencies installed ({time.time() - start_time:.1f}s)")

    # ------------------------------------------------------------------
    # Step 2: Build
    # ------------------------------------------------------------------
    build_result = await _run_npm_step(
        label="npm run build",
        command="npm run build",
        cwd=frontend_dir,
        timeout=180,
        failure_code="frontend_build_failed",
    )
    if not build_result["success"]:
        return build_result

    # Verify dist directory was produced
    dist_dir = os.path.join(frontend_dir, "dist")
    if not os.path.isdir(dist_dir):
        return _fail(
            "frontend_build_failed",
            "npm run build completed but dist/ directory was not created",
        )

    app_logger.info(f"Frontend build succeeded ({time.time() - start_time:.1f}s)")

    # ------------------------------------------------------------------
    # Step 3: Start preview server for health check
    # ------------------------------------------------------------------
    try:
        app_logger.info(f"Starting frontend preview on port {port}...")
        run_proc = await asyncio.create_subprocess_shell(
            f"npm run preview -- --host 127.0.0.1 --port {port} --strictPort",
            cwd=frontend_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        process_manager.register_process(run_proc, f"frontend_{port}")

        is_up = await check_http_status(f"http://127.0.0.1:{port}/", timeout=60)

        if not is_up:
            err_log = await _capture_process_output(run_proc)
            return _fail(
                "frontend_health_check_failed",
                f"Frontend failed health check on port {port}. Logs: {err_log[-1500:]}",
            )

        return {
            "success": True,
            "startup_time": time.time() - start_time,
            "port": port,
            "url": f"http://127.0.0.1:{port}",
        }

    except Exception as e:
        return _fail("frontend_preview_failed", f"Frontend preview server error: {e}")


# ======================================================================
# Helpers
# ======================================================================

async def _run_npm_step(
    *,
    label: str,
    command: str,
    cwd: str,
    timeout: int,
    failure_code: str,
) -> dict:
    """Run an npm command with proper timeout handling and error capture."""
    app_logger.info(f"Running: {label}...")
    try:
        proc = await asyncio.create_subprocess_shell(
            command,
            cwd=cwd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        try:
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        except asyncio.TimeoutError:
            proc.kill()
            await proc.wait()
            return _fail(failure_code, f"{label} timed out after {timeout} seconds")

        if proc.returncode != 0:
            stdout_text = stdout.decode(errors="replace")[-1500:] if stdout else ""
            stderr_text = stderr.decode(errors="replace")[-1500:] if stderr else ""
            return _fail(
                failure_code,
                f"{label} failed (exit code {proc.returncode}):\n{stderr_text}\n{stdout_text}",
            )

        return {"success": True}

    except FileNotFoundError:
        return _fail(failure_code, f"{label} failed: npm command not found. Ensure Node.js is installed.")
    except Exception as e:
        return _fail(failure_code, f"{label} failed with unexpected error: {e}")


def _find_vite_bin(frontend_dir: str) -> str | None:
    """Check if vite binary exists in node_modules/.bin."""
    bin_dir = os.path.join(frontend_dir, "node_modules", ".bin")
    if not os.path.isdir(bin_dir):
        return None
    # On Windows: vite.cmd, on Unix: vite
    for name in ("vite", "vite.cmd"):
        candidate = os.path.join(bin_dir, name)
        if os.path.exists(candidate):
            return candidate
    return None


async def _capture_process_output(proc: asyncio.subprocess.Process) -> str:
    """Safely capture output from a running or finished process."""
    try:
        if proc.returncode is not None:
            stdout, stderr = await proc.communicate()
            return stderr.decode(errors="replace") + "\n" + stdout.decode(errors="replace")
        else:
            return "Process is still running but not responding to health checks."
    except Exception:
        return "Failed to capture process logs."


def _fail(code: str, message: str) -> dict:
    """Return a structured failure result with a machine-readable error code."""
    app_logger.error(f"[{code}] {message}")
    return {"success": False, "error": message, "error_code": code}
