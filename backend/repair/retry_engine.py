from llm.base_provider import BaseProvider
from exceptions.generation_exceptions import RepairFailedException
import json

async def attempt_llm_retry(failed_content: str, error_msg: str, provider: BaseProvider, retries: int = 3) -> str:
    """Uses the LLM to rewrite a file that failed deterministic repair."""
    system_prompt = f"""
    The following code failed validation with this error: {error_msg}
    Please fix the code and return ONLY the corrected code without markdown wrappers.
    """
    
    for attempt in range(retries):
        try:
            response = await provider.generate(system_prompt, failed_content, response_format="text")
            cleaned = response.strip()
            if cleaned.startswith("```"):
                cleaned = "\n".join(cleaned.split("\n")[1:-1])
            if not _looks_like_code(cleaned, failed_content):
                continue
            return cleaned.strip()
        except Exception:
            continue
            
    raise RepairFailedException(f"LLM Retry engine failed after {retries} attempts.")


def _looks_like_code(candidate: str, original: str) -> bool:
    if not candidate:
        return False
    lowered = candidate.lower()
    if lowered.startswith("generated deterministically") or "return only the corrected code" in lowered:
        return False
    if "FastAPI" in original or "router" in original:
        return "FastAPI" in candidate or "APIRouter" in candidate or "router" in candidate
    if "import React" in original:
        return "import React" in candidate or "export default" in candidate
    return "\n" in candidate or "def " in candidate or "import " in candidate
