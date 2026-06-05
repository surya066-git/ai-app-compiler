import asyncio
import json
import time
import urllib.request
import urllib.parse
from utils.logger import app_logger

async def wait_for_port(port: int, timeout: int = 15) -> bool:
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            reader, writer = await asyncio.open_connection('127.0.0.1', port)
            writer.close()
            await writer.wait_closed()
            return True
        except ConnectionRefusedError:
            await asyncio.sleep(0.5)
        except Exception:
            await asyncio.sleep(0.5)
    return False

async def check_http_status(url: str, timeout: int = 20) -> bool:
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            def _fetch():
                return urllib.request.urlopen(url, timeout=2).getcode()
            status = await asyncio.to_thread(_fetch)
            return True
        except urllib.error.HTTPError as e:
            # Server is up but returned 4xx/5xx, which still means it successfully bound and responds
            return True 
        except Exception:
            await asyncio.sleep(1)
    return False


async def fetch_text(url: str, timeout: int = 20) -> tuple[bool, str]:
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            def _fetch():
                with urllib.request.urlopen(url, timeout=3) as response:
                    return response.read().decode("utf-8", errors="replace")

            return True, await asyncio.to_thread(_fetch)
        except Exception:
            await asyncio.sleep(1)
    return False, ""


async def post_json(url: str, payload: dict, timeout: int = 10) -> tuple[bool, dict]:
    try:
        def _post():
            data = json.dumps(payload).encode("utf-8")
            request = urllib.request.Request(
                url,
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(request, timeout=timeout) as response:
                body = response.read().decode("utf-8", errors="replace")
                return response.getcode(), body

        status, body = await asyncio.to_thread(_post)
        parsed = json.loads(body) if body else {}
        return 200 <= status < 300, parsed
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(body) if body else {}
        except Exception:
            parsed = {"body": body}
        return False, {"status": e.code, "error": parsed}
    except Exception as e:
        return False, {"error": str(e)}


async def post_form(url: str, payload: dict, timeout: int = 10) -> tuple[bool, dict]:
    try:
        def _post():
            data = urllib.parse.urlencode(payload).encode("utf-8")
            request = urllib.request.Request(
                url,
                data=data,
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                method="POST",
            )
            with urllib.request.urlopen(request, timeout=timeout) as response:
                body = response.read().decode("utf-8", errors="replace")
                return response.getcode(), body

        status, body = await asyncio.to_thread(_post)
        parsed = json.loads(body) if body else {}
        return 200 <= status < 300, parsed
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(body) if body else {}
        except Exception:
            parsed = {"body": body}
        return False, {"status": e.code, "error": parsed}
    except Exception as e:
        return False, {"error": str(e)}
