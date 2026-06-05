import json
from llm.base_provider import BaseProvider
from llm.local_provider import LocalDeterministicProvider
from exceptions.generation_exceptions import IntentParsingError

async def parse_intent(prompt: str, provider: BaseProvider) -> dict:
    """Uses LLM to parse a natural language prompt into a structured architecture plan."""
    
    system_prompt = """
    You are an expert software architect. Analyze the user's prompt and design the architecture.
    Return ONLY a valid JSON object with the following schema:
    {
      "app_name": "Name of the app",
      "features": ["list", "of", "features"],
      "database_tables": ["users", "other_tables"],
      "pages": ["Dashboard", "Settings"]
    }
    Always include a 'users' table and a 'Dashboard' page at minimum.
    """
    
    try:
        response = await provider.generate(system_prompt, prompt, response_format="json")
        architecture = json.loads(response)
        if not isinstance(architecture, dict) or "database_tables" not in architecture or "pages" not in architecture:
            fallback = await LocalDeterministicProvider().generate(system_prompt, prompt, response_format="json")
            architecture = json.loads(fallback)
        
        # Ensure minimum requirements
        if "users" not in [t.lower() for t in architecture.get("database_tables", [])]:
            if "database_tables" not in architecture:
                architecture["database_tables"] = []
            architecture["database_tables"].append("users")
            
        return architecture
    except Exception as e:
        raise IntentParsingError(f"Failed to parse intent: {str(e)}")
