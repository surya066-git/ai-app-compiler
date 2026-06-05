from llm.base_provider import BaseProvider
from llm.local_provider import LocalDeterministicProvider
from contracts.app_ir_schema import AppIR
from utils.helpers import extract_json_from_markdown, safe_json_loads
import json

async def plan_architecture(prompt: str, provider: BaseProvider) -> AppIR:
    """Converts a prompt into a deterministic AppIR representation."""
    
    schema_json = AppIR.model_json_schema()
    
    system_prompt = f"""
    You are a strict compiler planner. Convert the user's intent into the exact JSON schema below.
    JSON Schema: {json.dumps(schema_json)}
    Return ONLY a valid JSON object matching the AppIR schema. No markdown wrapping.
    """
    
    response = await provider.generate(system_prompt, prompt, response_format="json")
    response = extract_json_from_markdown(response)
    data = safe_json_loads(response, {})
    
    # Validate strictly with Pydantic. If a cloud provider returns valid JSON
    # that does not match the compiler contract, use the deterministic local
    # planner so the pipeline remains runnable.
    try:
        ir_model = AppIR(**data)
    except Exception:
        local_response = await LocalDeterministicProvider().generate(system_prompt, prompt, response_format="json")
        ir_model = AppIR(**safe_json_loads(local_response, {}))
    
    # Ensure baseline requirements
    if not any(t.name.lower() == "users" for t in ir_model.tables):
        from contracts.app_ir_schema import DBTable, DBField
        ir_model.tables.append(DBTable(
            name="users",
            fields=[
                DBField(name="id", type="Integer", is_primary_key=True),
                DBField(name="username", type="String"),
                DBField(name="hashed_password", type="String")
            ]
        ))
        
    return ir_model
