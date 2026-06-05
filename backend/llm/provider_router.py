from config.settings import settings
from utils.logger import app_logger
from llm.fallback_manager import FallbackManager
from llm.local_provider import LocalDeterministicProvider

def get_provider_router() -> FallbackManager:
    """
    Returns a FallbackManager configured with Gemini -> Groq -> OpenAI -> local deterministic fallback.
    """
    if settings.OFFLINE_DEMO_MODE:
        app_logger.info("OFFLINE_DEMO_MODE enabled; using deterministic local provider only.")
        return FallbackManager([LocalDeterministicProvider()])

    providers = []
    
    try:
        from llm.gemini_provider import GeminiProvider
        providers.append(GeminiProvider())
    except Exception as e:
        app_logger.warning(f"Failed to load GeminiProvider: {e}")
        
    try:
        from llm.groq_provider import GroqProvider
        providers.append(GroqProvider())
    except Exception as e:
        app_logger.warning(f"Failed to load GroqProvider: {e}")
        
    try:
        from llm.openai_provider import OpenAIProvider
        providers.append(OpenAIProvider())
    except Exception as e:
        app_logger.warning(f"Failed to load OpenAIProvider: {e}")

    providers.append(LocalDeterministicProvider())
        
    return FallbackManager(providers)
