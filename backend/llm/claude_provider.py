from llm.base_provider import BaseProvider
from config.settings import settings
from exceptions.generation_exceptions import LLMProviderException
import json
try:
    import anthropic
except ImportError:
    anthropic = None

class ClaudeProvider(BaseProvider):
    def __init__(self):
        if not anthropic:
            raise LLMProviderException("anthropic package is not installed.")
        if not settings.CLAUDE_API_KEY:
            raise LLMProviderException("CLAUDE_API_KEY is not set.")
            
        self.client = anthropic.AsyncAnthropic(api_key=settings.CLAUDE_API_KEY)
        self.model = "claude-3-opus-20240229"

    async def generate(self, system_prompt: str, user_prompt: str, response_format: str = "text") -> str:
        try:
            extra_args = {}
            if response_format == "json":
                # Claude doesn't have a strict JSON mode flag, we just prompt it and parse
                user_prompt += "\n\nPlease return ONLY a valid JSON object. No markdown wrapping."
                
            response = await self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.2
            )
            
            result = response.content[0].text
            if response_format == "json":
                result = result.strip()
                if result.startswith("```"):
                    first_newline = result.index("\n")
                    result = result[first_newline + 1:]
                if result.endswith("```"):
                    result = result[:-3]
                result = result.strip()
                json.loads(result) # Validate
                
            return result
        except Exception as e:
            raise LLMProviderException(f"Claude generation failed: {str(e)}")
