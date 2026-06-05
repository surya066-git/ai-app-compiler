from validators.syntax_validator import validate_syntax
from validators.execution_validator import validate_execution_readiness
from validators.security_validator import validate_security
from validators.consistency_validator import validate_consistency
from contracts.app_ir_schema import AppIR
from exceptions.generation_exceptions import ValidationException
from evaluation.failure_taxonomy import tracker
import re


async def validate_and_repair(files: dict) -> dict:
    """Compatibility validation helper used by older tests and demos."""
    if "frontend/package.json" not in files:
        raise ValidationException("Missing package.json in frontend")

    cleaned_files = {
        filepath: _strip_markdown_fence(content) if isinstance(content, str) else content
        for filepath, content in files.items()
    }
    validate_syntax(cleaned_files)
    return cleaned_files

def validate_generated_project(files: dict, ir: AppIR) -> bool:
    """Runs all validation pipelines in sequence."""
    try:
        validate_consistency(ir)
    except ValidationException as e:
        tracker.record("consistency")
        raise e
        
    try:
        validate_syntax(files)
    except ValidationException as e:
        tracker.record("syntax")
        raise e
        
    try:
        validate_execution_readiness(files)
    except ValidationException as e:
        tracker.record("execution")
        raise e

    try:
        _validate_routes_registered(files, ir)
    except ValidationException as e:
        tracker.record("execution")
        raise e
        
    try:
        validate_security(files)
    except ValidationException as e:
        tracker.record("security")
        raise e
        
    return True


def _strip_markdown_fence(content: str) -> str:
    cleaned = content.strip()
    if cleaned.startswith("```"):
        lines = cleaned.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        return "\n".join(lines).strip()
    return content


def _validate_routes_registered(files: dict, ir: AppIR) -> None:
    backend_source = "\n".join(
        content for filepath, content in files.items()
        if filepath.startswith("backend/") and filepath.endswith(".py")
    )
    for endpoint in ir.endpoints:
        route_path = endpoint.path if endpoint.path.startswith("/") else f"/{endpoint.path}"
        method = endpoint.method.lower()
        route_registered = re.search(rf"@(router|app)\.{re.escape(method)}\(\s*['\"]{re.escape(route_path)}['\"]", backend_source)
        if not route_registered:
            raise ValidationException(
                f"Missing backend route {endpoint.method.upper()} {route_path}",
                details={"route": route_path, "method": endpoint.method},
            )
