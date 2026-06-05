from llm.base_provider import BaseProvider
from templates.fastapi_templates import DATABASE_PY
import re

async def generate_database_schema(tables: list, provider: BaseProvider) -> dict:
    """Generates deterministic SQLAlchemy models based on IR tables."""
    clean_tables = list(dict.fromkeys([_safe_table_name(table) for table in tables if table]))
    if "users" not in [table.lower() for table in clean_tables]:
        clean_tables.insert(0, "users")

    models_code = [
        "from sqlalchemy import Column, DateTime, Integer, String, func",
        "from database import Base",
        "",
    ]

    for table in clean_tables:
        if table.lower() == "users":
            models_code.extend(
                [
                    "class User(Base):",
                    "    __tablename__ = 'users'",
                    "    id = Column(Integer, primary_key=True, index=True)",
                    "    username = Column(String, unique=True, index=True, nullable=False)",
                    "    hashed_password = Column(String, nullable=False)",
                    "    created_at = Column(DateTime(timezone=True), server_default=func.now())",
                    "",
                ]
            )
            continue

        class_name = _class_name(table)
        models_code.extend(
            [
                f"class {class_name}(Base):",
                f"    __tablename__ = '{table.lower()}'",
                "    id = Column(Integer, primary_key=True, index=True)",
                "    name = Column(String, index=True, nullable=False)",
                "    status = Column(String, default='active')",
                "    description = Column(String, default='')",
                "    created_at = Column(DateTime(timezone=True), server_default=func.now())",
                "",
            ]
        )

    return {
        "database.py": DATABASE_PY,
        "models.py": "\n".join(models_code),
    }


def _safe_table_name(table: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9_]", "_", table.strip().lower())
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "items"


def _class_name(table: str) -> str:
    singular = table[:-1] if table.endswith("s") and len(table) > 3 else table
    words = re.findall(r"[a-zA-Z0-9]+", singular)
    return "".join(word.capitalize() for word in words) or "Item"
