import re
from exceptions.generation_exceptions import ValidationException

def validate_security(files: dict):
    """Ensures no hardcoded dangerous defaults or path traversals."""
    for filepath in files.keys():
        if ".." in filepath or filepath.startswith("/"):
            raise ValidationException(f"Security error: Invalid path traversal in filename {filepath}")
            
    # Check for hardcoded weak passwords in env examples
    env_content = files.get(".env.example", "")
    if "password123" in env_content:
        raise ValidationException("Security error: Weak default password found in environment template.")
        
    return True
