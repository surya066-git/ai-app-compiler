from contracts.app_ir_schema import AppIR

def generate_architecture_tree(ir: AppIR) -> dict:
    """Creates a virtual file tree based on the IR."""
    tree = {
        "backend": ["main.py", "database.py", "models.py", "auth.py", "security.py", "requirements.txt", "Dockerfile"],
        "backend/routers": [f"{route.path.strip('/')}.py" for route in ir.endpoints],
        "frontend": ["package.json", "vite.config.js", "tailwind.config.js", "postcss.config.js", "index.html", "Dockerfile"],
        "frontend/src": ["main.jsx", "App.jsx", "index.css", "api.js", "store.js"],
        "frontend/src/components": [f"{page.name}.jsx" for page in ir.pages] + ["Navbar.jsx", "Sidebar.jsx"],
        "root": ["docker-compose.yml", ".env.example", "README.md", ".gitignore"]
    }
    return tree
