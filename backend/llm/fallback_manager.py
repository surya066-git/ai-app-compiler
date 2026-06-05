import asyncio
import time
from typing import List, Dict, Any, Optional

from config.settings import settings
from llm.base_provider import BaseProvider
from utils.logger import app_logger

class FallbackManager:
    def __init__(self, providers: List[BaseProvider]):
        self.providers = providers
        self.disabled_until = {}
        self.metrics = {
            "attempts": 0,
            "fallbacks": 0,
            "provider_switches": 0,
            "quota_failures": 0,
            "timeout_failures": 0,
            "fallback_events": [],
            "provider_latency": {},
            "provider_failures": {},
            "provider_successes": {},
            "last_provider": None,
        }

    async def generate(self, system_prompt: str, user_prompt: str, response_format: str = "text") -> str:
        """
        Provider-compatible generation entrypoint.

        The compiler can pass this manager anywhere a provider is expected; it
        will try Gemini/Groq/OpenAI first when configured and then fall back to
        the deterministic local provider.
        """
        last_exception = None

        for index, provider in enumerate(self.providers):
            provider_name = getattr(provider, "name", provider.__class__.__name__)
            if self._is_disabled(provider_name):
                self.metrics["fallback_events"].append({
                    "from": provider_name,
                    "to": self._next_provider_name(index),
                    "reason": "provider_cooldown",
                    "skipped": True,
                })
                continue

            app_logger.info(f"Attempting generation with provider: {provider_name}")
            self.metrics["attempts"] += 1
            start_time = time.time()
            try:
                result = await asyncio.wait_for(
                    provider.generate(system_prompt, user_prompt, response_format=response_format),
                    timeout=settings.PROVIDER_TIMEOUT_SECONDS,
                )
                latency = time.time() - start_time
                self._record_latency(provider_name, latency)
                self.metrics["provider_successes"][provider_name] = self.metrics["provider_successes"].get(provider_name, 0) + 1
                if self.metrics["last_provider"] and self.metrics["last_provider"] != provider_name:
                    self.metrics["provider_switches"] += 1
                self.metrics["last_provider"] = provider_name
                app_logger.info(f"Generation succeeded with {provider_name} in {latency:.2f}s")
                return result
            except asyncio.TimeoutError as e:
                latency = time.time() - start_time
                self._record_latency(provider_name, latency)
                self.metrics["timeout_failures"] += 1
                self.metrics["provider_failures"][provider_name] = self.metrics["provider_failures"].get(provider_name, 0) + 1
                self._cooldown(provider_name, "timeout")
                app_logger.warning(f"Provider {provider_name} timed out in {latency:.2f}s.")
                last_exception = e
                self._record_fallback_event(provider_name, index, "timeout")
            except Exception as e:
                latency = time.time() - start_time
                self._record_latency(provider_name, latency)
                self.metrics["provider_failures"][provider_name] = self.metrics["provider_failures"].get(provider_name, 0) + 1
                reason = self._failure_reason(str(e))
                if reason == "quota":
                    self.metrics["quota_failures"] += 1
                    self._cooldown(provider_name, reason)
                app_logger.warning(f"Provider {provider_name} failed in {latency:.2f}s. Error: {str(e)}")
                last_exception = e
                self._record_fallback_event(provider_name, index, reason)

        app_logger.error("All providers failed in fallback chain.")
        raise last_exception or Exception("All LLM providers failed.")
        
    async def generate_with_fallback(self, prompt: str, schema: Optional[Dict] = None) -> str:
        """
        Attempts generation using the ordered list of providers.
        Falls back to the next provider on timeout, quota error, or failure.
        """
        response_format = "json" if schema else "text"
        return await self.generate("", prompt, response_format=response_format)

    def snapshot_metrics(self) -> Dict[str, Any]:
        return {
            **self.metrics,
            "provider_health": self.provider_health_scores(),
        }

    def provider_health_scores(self) -> Dict[str, int]:
        scores = {}
        provider_names = [getattr(provider, "name", provider.__class__.__name__) for provider in self.providers]
        for name in provider_names:
            successes = self.metrics["provider_successes"].get(name, 0)
            failures = self.metrics["provider_failures"].get(name, 0)
            total = successes + failures
            scores[name] = 100 if total == 0 else int((successes / total) * 100)
        return scores

    def _record_latency(self, provider_name: str, latency: float) -> None:
        self.metrics["provider_latency"].setdefault(provider_name, []).append(latency)

    def _record_fallback_event(self, provider_name: str, index: int, reason: str) -> None:
        next_provider = self._next_provider_name(index)
        if next_provider:
            self.metrics["fallbacks"] += 1
            self.metrics["fallback_events"].append({
                "from": provider_name,
                "to": next_provider,
                "reason": reason,
                "skipped": False,
            })

    def _next_provider_name(self, current_index: int) -> Optional[str]:
        for provider in self.providers[current_index + 1:]:
            name = getattr(provider, "name", provider.__class__.__name__)
            if not self._is_disabled(name):
                return name
        return None

    def _is_disabled(self, provider_name: str) -> bool:
        disabled_until = self.disabled_until.get(provider_name, 0)
        if disabled_until <= time.time():
            self.disabled_until.pop(provider_name, None)
            return False
        return True

    def _cooldown(self, provider_name: str, reason: str) -> None:
        if provider_name == "local_deterministic":
            return
        self.disabled_until[provider_name] = time.time() + settings.PROVIDER_COOLDOWN_SECONDS
        self.metrics["fallback_events"].append({
            "from": provider_name,
            "to": None,
            "reason": f"{reason}_cooldown_started",
            "skipped": True,
        })

    def _failure_reason(self, error: str) -> str:
        lowered = error.lower()
        if "quota" in lowered or "429" in lowered or "rate limit" in lowered:
            return "quota"
        if "timeout" in lowered or "timed out" in lowered:
            return "timeout"
        return "error"
