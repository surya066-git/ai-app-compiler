class GenerationException(Exception):
    """Base exception for all generation-related errors."""
    def __init__(self, message: str, details: dict = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

class IntentParsingError(GenerationException):
    """Raised when the AI fails to parse the user's intent."""
    pass

class ValidationException(GenerationException):
    """Raised when generated code fails validation checks."""
    pass

class RepairFailedException(GenerationException):
    """Raised when the self-healing system fails to repair code."""
    pass

class ExportException(GenerationException):
    """Raised when the project cannot be written or zipped."""
    pass

class LLMProviderException(GenerationException):
    """Raised when an AI provider fails to return a valid response."""
    pass
