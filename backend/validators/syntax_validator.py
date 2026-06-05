import ast
import re
from exceptions.generation_exceptions import ValidationException

def validate_syntax(files: dict) -> dict:
    """Validates Python AST and basic structural integrity for React files."""
    for filepath, content in files.items():
        if filepath.endswith(".py"):
            try:
                tree = ast.parse(content)
            except SyntaxError as e:
                raise ValidationException(f"Syntax error in {filepath}: {str(e)}", details={"filepath": filepath, "error": str(e)})

            _validate_common_missing_imports(filepath, tree)
        
        if filepath.endswith((".jsx", ".js")):
            # Simple heuristic check for unclosed tags/brackets
            if content.count("{") != content.count("}"):
                raise ValidationException(f"Mismatched braces in {filepath}")

            if "\\nimport " in content or "/>\\n" in content:
                raise ValidationException(
                    f"Escaped newline found in generated JavaScript module {filepath}",
                    details={"filepath": filepath},
                )

    _validate_frontend_import_paths(files)
    return files


def _validate_common_missing_imports(filepath: str, tree: ast.AST) -> None:
    imported_names = set()
    used_names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_names.update(alias.asname or alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported_names.update(alias.asname or alias.name for alias in node.names)
        elif isinstance(node, ast.Name):
            used_names.add(node.id)

    required_imports = {
        "os": "os",
        "json": "json",
        "FastAPI": "FastAPI",
        "APIRouter": "APIRouter",
        "Depends": "Depends",
        "HTTPException": "HTTPException",
        "BaseModel": "BaseModel",
    }
    for used_name, import_name in required_imports.items():
        if used_name in used_names and import_name not in imported_names:
            raise ValidationException(
                f"Missing import in {filepath}: name '{used_name}' is not defined",
                details={"filepath": filepath, "missing_import": used_name},
            )


def _validate_frontend_import_paths(files: dict) -> None:
    for filepath, content in files.items():
        if not filepath.endswith((".jsx", ".js")):
            continue
        for ref in re.findall(r"from\s+['\"](\./components/[^'\"]+)['\"]", content):
            component_ref = ref.replace("./components/", "")
            candidates = [f"frontend/src/components/{component_ref}"]
            if not component_ref.endswith((".jsx", ".js")):
                candidates.extend([
                    f"frontend/src/components/{component_ref}.jsx",
                    f"frontend/src/components/{component_ref}.js",
                ])
            if not any(candidate in files for candidate in candidates):
                raise ValidationException(
                    f"Frontend import target missing in {filepath}: {ref}",
                    details={"filepath": filepath, "import": ref},
                )
