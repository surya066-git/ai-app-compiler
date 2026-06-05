from llm.base_provider import BaseProvider
from config.settings import settings
from exceptions.generation_exceptions import LLMProviderException
import json
try:
    import google.generativeai as genai
except ImportError:
    genai = None

class GeminiProvider(BaseProvider):
    def __init__(self):
        if not genai:
            raise LLMProviderException("google-generativeai package is not installed.")
        if not settings.GEMINI_API_KEY:
            raise LLMProviderException("GEMINI_API_KEY is not set.")
            
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    async def generate(self, system_prompt: str, user_prompt: str, response_format: str = "text") -> str:
        try:
            # Gemini system instructions can be prepended or set in model init, 
            # but for simplicity we combine them if system_prompt is provided.
            prompt = f"System: {system_prompt}\n\nUser: {user_prompt}"
            
            # Use generate_content_async for async operations
            response = await self.model.generate_content_async(prompt)
            
            # Simple fallback to ensure we return a string
            result = response.text
            if response_format == "json":
                # Strip markdown code fences that models often wrap JSON in
                result = result.strip()
                if result.startswith("```"):
                    # Remove opening fence (with optional language tag)
                    first_newline = result.index("\n")
                    result = result[first_newline + 1:]
                if result.endswith("```"):
                    result = result[:-3]
                result = result.strip()
                # Validation check
                json.loads(result)
                
            return result
        except Exception as e:
            raise LLMProviderException(f"Gemini generation failed: {str(e)}")
