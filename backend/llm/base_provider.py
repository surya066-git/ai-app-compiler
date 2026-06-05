from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    async def generate(self, system_prompt: str, user_prompt: str, response_format: str = "text") -> str:
        """
        Generates a response from the LLM.
        
        Args:
            system_prompt (str): The system prompt setting the context.
            user_prompt (str): The user's input prompt.
            response_format (str): The expected response format (e.g., 'text' or 'json').
            
        Returns:
            str: The raw generated response from the model.
        """
        pass
