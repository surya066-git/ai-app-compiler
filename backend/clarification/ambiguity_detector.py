from llm.base_provider import BaseProvider
import json

async def detect_ambiguity(prompt: str, provider: BaseProvider) -> dict:
    """Analyzes a prompt for vague or conflicting requirements."""
    system_prompt = """
    Analyze the user prompt for software generation.
    Return a JSON object with:
    {
        "is_ambiguous": boolean,
        "missing_details": ["list of missing details like auth method, database type, styling preferences"],
        "conflicts": ["list of conflicting requirements if any"]
    }
    """
    try:
        response = await provider.generate(system_prompt, prompt, response_format="json")
        return json.loads(response)
    except Exception:
        return {"is_ambiguous": True, "missing_details": ["General architecture specifics"], "conflicts": []}
