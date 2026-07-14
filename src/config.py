import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings from .env"""
    OPENAI_API_KEY: str = ""
    PRIMARY_MODEL: str = "gpt-3.5-turbo"
    SECONDARY_MODEL: str = "gpt-3.5-turbo"
    TEMPERATURE: float = 0.3
    MAX_TOKENS: int = 2048
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    EMBEDDING_DIMENSION: int = 384
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 100
    TOP_K_RETRIEVAL: int = 5
    RETRIEVAL_THRESHOLD: float = 0.3
    CHROMA_PERSIST_DIR: str = "./data/chroma_db"
    CHROMA_COLLECTION_NAME: str = "research_papers"
    MAX_PDF_SIZE_MB: int = 50
    APP_NAME: str = "ResearchMate AI"
    THEME: str = "dark"
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
