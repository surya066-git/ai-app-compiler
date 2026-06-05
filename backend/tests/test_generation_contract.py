import pytest

from generators.backend_generator import generate_backend_system
from generators.frontend_generator import generate_frontend_system
from llm.local_provider import LocalDeterministicProvider
from planning.deterministic_planner import plan_architecture
from validators.syntax_validator import validate_syntax


@pytest.mark.asyncio
async def test_generated_frontend_imports_match_component_files():
    provider = LocalDeterministicProvider()
    ir = await plan_architecture("Build a todo app with users and tasks", provider)
    files = await generate_frontend_system(ir, provider)

    assert "\\nimport " not in files["frontend/src/App.jsx"]
    validate_syntax(files)


@pytest.mark.asyncio
async def test_generated_backend_route_modules_are_valid_python_identifiers():
    provider = LocalDeterministicProvider()
    ir = await plan_architecture("Build a weather app with city forecasts", provider)
    files, _ = await generate_backend_system(ir, provider)

    for path in files:
        if path.startswith("backend/routers/") and path.endswith(".py"):
            module_name = path.rsplit("/", 1)[-1][:-3]
            assert module_name.isidentifier()
    validate_syntax(files)
