import json

def attempt_schema_repair(raw_output: str) -> dict:
    """Attempts to fix badly formatted JSON from LLM."""
    cleaned = raw_output.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
        
    try:
        data = json.loads(cleaned.strip())
    except json.JSONDecodeError:
        return None

    if not isinstance(data, dict):
        return None

    data.setdefault("app_name", "Generated Application")
    data.setdefault("description", "Generated application")
    data.setdefault("tables", [])
    data.setdefault("endpoints", [])
    data.setdefault("pages", [])
    data.setdefault("roles", ["user"])
    data.setdefault("assumptions", [])

    if isinstance(data["roles"], str):
        data["roles"] = [data["roles"]]
    if isinstance(data["assumptions"], str):
        data["assumptions"] = [data["assumptions"]]

    if all(isinstance(table, str) for table in data["tables"]):
        data["tables"] = [
            {
                "name": table,
                "fields": [
                    {"name": "id", "type": "Integer", "is_primary_key": True},
                    {"name": "name", "type": "String"},
                ],
            }
            for table in data["tables"]
        ]

    if all(isinstance(page, str) for page in data["pages"]):
        data["pages"] = [
            {
                "name": page,
                "route": "/" + page.lower().replace(" ", "-"),
                "description": f"{page} page",
                "requires_auth": False,
            }
            for page in data["pages"]
        ]

    return data
