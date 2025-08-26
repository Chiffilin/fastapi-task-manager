import os
from typing import ClassVar, List
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field


class Settings(BaseSettings):
    # Database
    POSTGRES_USER: str = "test_user"
    POSTGRES_PASSWORD: str = "test_password"
    POSTGRES_DB: str = "test_db"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    EXTERNAL_DB_PORT: int = 5433

    # Application
    APP_PORT: int = 8000
    SECRET_KEY: str = "default-secret-change-me"
    DEBUG: bool = False
    PROJECT_NAME: str = "FastAPI Task Manager"
    PROJECT_VERSION: str = "1.0.0"
    LOG_LEVEL: str = "INFO"

    # Features
    ENABLE_SWAGGER: bool = True
    ENABLE_DEBUG_TOOLBAR: bool = False
    TESTING: bool = False

    # CORS
    CORS_ORIGINS: ClassVar[List[str]] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]

    # Правильный порядок загрузки env файлов
    model_config = SettingsConfigDict(
        env_file=(
            f".env.{os.getenv('ENV', 'dev')}",  # .env.test или .env.dev
            ".env",  # Базовый .env
        ),
        case_sensitive=False,
        extra="ignore",
    )

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        # Если задана переменная DATABASE_URL, используем ее
        if os.getenv("DATABASE_URL"):
            return os.getenv("DATABASE_URL")
        # Иначе создаем из компонентов
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @computed_field
    @property
    def EXTERNAL_DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@localhost:{self.EXTERNAL_DB_PORT}/{self.POSTGRES_DB}"


settings = Settings()
