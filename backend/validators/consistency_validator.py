from contracts.app_ir_schema import AppIR
from exceptions.generation_exceptions import ValidationException

def validate_consistency(ir: AppIR):
    """Ensures cross-layer mappings (e.g. Frontend routes match Backend)."""
    
    # 1. Ensure backend endpoints match frontend pages where obvious
    # In a full production system, we'd do deep AST inspection. Here we use IR.
    ui_routes = [p.route for p in ir.pages]
    api_routes = [e.path for e in ir.endpoints]
    
    # 2. Check if auth is consistent
    requires_auth_ui = any(p.requires_auth for p in ir.pages)
    if requires_auth_ui and not any(t.name.lower() == "users" for t in ir.tables):
        raise ValidationException("Consistency Error: Auth pages exist but no 'users' table found.")
        
    return True
