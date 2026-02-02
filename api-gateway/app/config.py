from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # Project
    PROJECT_NAME: str = "InterviewPilot API"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    
    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # Security
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 1440
    
    # Database
    DATABASE_URL: str
    
    # Redis
    REDIS_URL: str
    
    # Qdrant
    QDRANT_URL: str
    
    # Go Service
    GO_SERVICE_URL: str
    
    # OpenAI
    OPENAI_API_KEY: str
    MODEL_NAME: str = "gpt-4-turbo-preview"
    
    # Upload
    MAX_UPLOAD_SIZE_MB: int = 10
    UPLOAD_DIR: str = "uploads"
    
    # CORS
    ALLOWED_ORIGINS: list = ["http://localhost:3000", "http://localhost"]
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 60
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()