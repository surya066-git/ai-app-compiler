from llm.base_provider import BaseProvider
import re

async def generate_ui_components(pages: list, provider: BaseProvider) -> dict:
    """Uses LLM to generate React Tailwind components for the specified pages."""
    
    ui_files = {}
    
    # 1. Generate Sidebar
    sidebar_prompt = f"""
    Generate a React Sidebar component using TailwindCSS and lucide-react icons.
    Links should be: {', '.join(pages)}.
    Return ONLY valid JSX code using react-router-dom Link.
    """
    try:
        sidebar_code = await provider.generate("You are an expert React UI developer.", sidebar_prompt, "text")
        ui_files["Sidebar.jsx"] = clean_code(sidebar_code)
    except:
        ui_files["Sidebar.jsx"] = "import React from 'react';\nexport default function Sidebar() { return <div className='w-64 bg-white shadow-md'>Sidebar</div>; }"

    # 2. Generate Navbar
    navbar_prompt = """
    Generate a simple React Navbar component with a title and a logout button using TailwindCSS.
    Return ONLY valid JSX code.
    """
    try:
        navbar_code = await provider.generate("You are an expert React UI developer.", navbar_prompt, "text")
        ui_files["Navbar.jsx"] = clean_code(navbar_code)
    except:
        ui_files["Navbar.jsx"] = "import React from 'react';\nexport default function Navbar() { return <nav className='bg-blue-600 p-4 text-white'>Navbar</nav>; }"

    # 3. Generate Pages
    for page in pages:
        page_name = component_name(page)
        page_prompt = f"""
        Generate a beautiful, responsive React Dashboard page for '{page_name}' using TailwindCSS.
        Include some generic cards, a table or chart placeholder.
        Return ONLY valid JSX code.
        """
        try:
            page_code = await provider.generate("You are an expert React UI developer.", page_prompt, "text")
            ui_files[f"{page_name}.jsx"] = clean_code(page_code)
        except:
            ui_files[f"{page_name}.jsx"] = f"import React from 'react';\nexport default function {page_name}() {{ return <div className='p-6'><h1 className='text-2xl font-bold'>{page_name}</h1></div>; }}"

    return ui_files


def component_name(value: str) -> str:
    words = re.findall(r"[A-Za-z0-9]+", value or "")
    return "".join(word[:1].upper() + word[1:] for word in words) or "Dashboard"

def clean_code(code: str) -> str:
    code = code.strip()
    if code.startswith("```jsx"):
        code = code[6:]
    elif code.startswith("```javascript"):
        code = code[14:]
    elif code.startswith("```js"):
        code = code[5:]
    elif code.startswith("```"):
        code = code[3:]
    if code.endswith("```"):
        code = code[:-3]
    return code.strip()
