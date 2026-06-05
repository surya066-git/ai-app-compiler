from llm.base_provider import BaseProvider
from config.settings import settings
from exceptions.generation_exceptions import LLMProviderException
import json
try:
    import openai
except ImportError:
    openai = None

class OpenAIProvider(BaseProvider):
    def __init__(self):
        if not openai:
            raise LLMProviderException("openai package is not installed.")
        if not settings.OPENAI_API_KEY:
            raise LLMProviderException("OPENAI_API_KEY is not set.")
        
        # We use AsyncOpenAI for async support
        self.client = openai.AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = "gpt-4-turbo"

    async def generate(self, system_prompt: str, user_prompt: str, response_format: str = "text") -> str:
        try:
            kwargs = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.2
            }
            if response_format == "json":
                kwargs["response_format"] = {"type": "json_object"}

            response = await self.client.chat.completions.create(**kwargs)
            return response.choices[0].message.content
        except Exception as e:
            raise LLMProviderException(f"OpenAI generation failed: {str(e)}")
