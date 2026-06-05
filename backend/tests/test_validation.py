import pytest

from agents.validation_agent import validate_and_repair
from exceptions.generation_exceptions import ValidationException
from repair.import_repair import attempt_import_repair
from repair.route_repair import attempt_route_repair
from repair.schema_repair import attempt_schema_repair
from validators.schema_validator import validate_schema

@pytest.mark.asyncio
async def test_validation_agent_success():
    """Test that valid python and frontend files pass validation."""
    valid_files = {
        "backend/main.py": "print('hello world')",
        "frontend/package.json": "{}"
    }
    
    validated = await validate_and_repair(valid_files)
    assert "backend/main.py" in validated
    assert "frontend/package.json" in validated

@pytest.mark.asyncio
async def test_validation_agent_syntax_error():
    """Test that invalid python raises an exception."""
    invalid_files = {
        "backend/main.py": "def invalid_func(:\n    pass",
        "frontend/package.json": "{}"
    }
    
    with pytest.raises(ValidationException, match="Syntax error"):
        await validate_and_repair(invalid_files)

@pytest.mark.asyncio
async def test_validation_agent_self_heal_markdown():
    """Test that it strips markdown tags during self-healing."""
    markdown_files = {
        "backend/main.py": "```python\nprint('hello')\n```",
        "frontend/package.json": "{}"
    }
    
    validated = await validate_and_repair(markdown_files)
    assert validated["backend/main.py"] == "print('hello')"

@pytest.mark.asyncio
async def test_validation_agent_missing_package_json():
    """Test that missing package.json raises an exception."""
    files = {
        "backend/main.py": "print('hello')"
    }
    
    with pytest.raises(ValidationException, match="Missing package.json in frontend"):
        await validate_and_repair(files)


def test_import_repair_adds_missing_standard_import():
    repaired = attempt_import_repair("backend/main.py", "VALUE = os.getenv('X')", "name 'os' is not defined")
    assert repaired.startswith("import os")


def test_route_repair_adds_missing_fastapi_route():
    content = "from fastapi import FastAPI\napp = FastAPI()\n"
    repaired = attempt_route_repair("backend/main.py", content, "/api/tasks/{id}", "GET")
    assert '@app.get("/api/tasks/{id}")' in repaired
    assert "id: int" in repaired


def test_schema_repair_normalizes_common_shape_drift():
    repaired = attempt_schema_repair(
        '{"app_name":"Demo","description":"Demo app","tables":["users"],"pages":["Dashboard"],"roles":"admin"}'
    )
    ir = validate_schema(repaired)
    assert ir.roles == ["admin"]
    assert ir.tables[0].name == "users"
    assert ir.pages[0].name == "Dashboard"
