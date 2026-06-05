from llm.base_provider import BaseProvider
from config.settings import settings
from exceptions.generation_exceptions import LLMProviderException
import json
try:
    from groq import AsyncGroq
except ImportError:
    AsyncGroq = None

class GroqProvider(BaseProvider):
    def __init__(self, model_name="llama-3.3-70b-versatile"):
        if not AsyncGroq:
            raise LLMProviderException("groq package is not installed.")
        if not settings.GROQ_API_KEY:
            raise LLMProviderException("GROQ_API_KEY is not set.")
            
        self.client = AsyncGroq(api_key=settings.GROQ_API_KEY)
        self.model = model_name

    async def generate(self, system_prompt: str, user_prompt: str, response_format: str = "text") -> str:
        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            
            kwargs = {
                "messages": messages,
                "model": self.model,
                "temperature": 0.2
            }
            if response_format == "json":
                kwargs["response_format"] = {"type": "json_object"}
                
            response = await self.client.chat.completions.create(**kwargs)
            result = response.choices[0].message.content
            
            if response_format == "json":
                result = result.strip()
                if result.startswith("```"):
                    first_newline = result.index("\n")
                    result = result[first_newline + 1:]
                if result.endswith("```"):
                    result = result[:-3]
                result = result.strip()
                json.loads(result)
                
            return result
        except Exception as e:
            raise LLMProviderException(f"Groq generation failed: {str(e)}")
