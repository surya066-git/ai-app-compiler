from pydantic import ValidationError
from contracts.app_ir_schema import AppIR
from exceptions.generation_exceptions import ValidationException

def validate_schema(data: dict) -> AppIR:
    """Validates raw dict against the AppIR strict schema."""
    try:
        return AppIR(**data)
    except ValidationError as e:
        raise ValidationException(f"Schema validation failed: {str(e)}", details=e.errors())
