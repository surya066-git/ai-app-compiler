import os
import re
import secrets
import string

def sanitize_filename(filename: str) -> str:
    """Removes invalid characters from filenames to prevent path traversal and shell injection."""
    return re.sub(r'[^a-zA-Z0-9_\-\.]', '_', filename)

def generate_jwt_secret(length: int = 32) -> str:
    """Generates a secure random JWT secret for new projects."""
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def ensure_safe_path(base_dir: str, target_path: str) -> str:
    """Ensures a path does not resolve outside of the base directory (prevents path traversal)."""
    abs_base = os.path.abspath(base_dir)
    abs_target = os.path.abspath(os.path.join(base_dir, target_path))
    
    if os.path.commonpath([abs_base, abs_target]) != abs_base:
        raise ValueError(f"Path traversal detected: {target_path}")
        
    return abs_target
