from llm.base_provider import BaseProvider
import json

async def generate_assumptions(prompt: str, ambiguities: dict, provider: BaseProvider) -> list:
    """Generates standard documented assumptions for underspecified features."""
    if not ambiguities.get("is_ambiguous", False) and not ambiguities.get("missing_details"):
        return []
        
    system_prompt = f"""
    Based on the missing details: {ambiguities.get('missing_details')}
    Generate a JSON list of string assumptions you are making to proceed deterministically.
    Example: ["Authentication assumed to be JWT", "PostgreSQL used for database"]
    Return ONLY a JSON list of strings.
    """
    
    try:
        response = await provider.generate(system_prompt, prompt, response_format="json")
        assumptions = json.loads(response)
        if isinstance(assumptions, list):
            return assumptions
        if isinstance(assumptions, dict) and "assumptions" in assumptions:
            return assumptions["assumptions"]
        return ["Using standard defaults for missing specifications."]
    except Exception:
        return ["Assumed standard JWT Auth and Postgres DB."]
