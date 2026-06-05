import asyncio
import socket
import subprocess
import os
from utils.logger import app_logger

class ProcessManager:
    def __init__(self):
        self.active_processes = []
        
    def get_free_port(self) -> int:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 0))
        port = s.getsockname()[1]
        s.close()
        return port

    def register_process(self, process: asyncio.subprocess.Process, name: str):
        self.active_processes.append({"proc": process, "name": name})
        
    async def cleanup_all(self):
        for p in self.active_processes:
            proc = p["proc"]
            if proc.returncode is None:
                app_logger.info(f"Cleaning up sandbox process: {p['name']} (PID: {proc.pid})")
                try:
                    if os.name == 'nt':
                        subprocess.call(['taskkill', '/F', '/T', '/PID', str(proc.pid)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    else:
                        proc.kill()
                    await asyncio.wait_for(proc.wait(), timeout=3)
                except Exception as e:
                    app_logger.warning(f"Failed to kill {p['name']}: {e}")
        self.active_processes = []

process_manager = ProcessManager()
