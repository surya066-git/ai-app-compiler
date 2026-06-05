import json
from typing import Any

def safe_json_loads(data: str, default: Any = None) -> Any:
    """Safely parse JSON data, returning default if it fails."""
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return default or {}

def extract_json_from_markdown(text: str) -> str:
    """Extracts JSON block from markdown if present."""
    if "```json" in text:
        return text.split("```json")[1].split("```")[0].strip()
    if "```" in text:
        return text.split("```")[1].split("```")[0].strip()
    return text.strip()
