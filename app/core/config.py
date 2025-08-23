from typing import ClassVar, List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    EXTERNAL_DB_PORT: int = 5433

    # Application
    APP_PORT: int = 8000  # ← Добавляем порт приложения
    SECRET_KEY: str = "default-secret-change-me"
    DEBUG: bool = False
    PROJECT_NAME: str = "FastAPI Task Manager"
    PROJECT_VERSION: str = "1.0.0"
    LOG_LEVEL: str = "INFO"

    # Computed DATABASE_URL (для приложения внутри Docker)
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # Computed EXTERNAL_DATABASE_URL (для внешних подключений)
    @property
    def EXTERNAL_DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@localhost:{self.EXTERNAL_DB_PORT}/{self.POSTGRES_DB}"

    # CORS (можно оставить в коде как константу)
    CORS_ORIGINS: ClassVar[List[str]] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]

    class Config:
        env_file = ".env"  # Теперь только один файл
        case_sensitive = False


settings = Settings()
