from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "AI App Compiler"
    DEBUG: bool = False
    
    # AI Providers (Loaded from environment, none hardcoded)
    OPENAI_API_KEY: Optional[str] = None
    GEMINI_API_KEY: Optional[str] = None
    CLAUDE_API_KEY: Optional[str] = None
    GROQ_API_KEY: Optional[str] = None
    DEFAULT_LLM_PROVIDER: str = "gemini" # 'openai', 'gemini', 'claude'
    OFFLINE_DEMO_MODE: bool = False
    PROVIDER_TIMEOUT_SECONDS: int = 45
    PROVIDER_COOLDOWN_SECONDS: int = 120

    # Security
    JWT_SECRET_KEY: str = "super_secret_default_change_me"
    ALGORITHM: str = "HS256"

    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost/dbname"

    # Export paths
    EXPORT_DIR: str = "generated_projects"
    STORAGE_DIR: str = "storage"
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
