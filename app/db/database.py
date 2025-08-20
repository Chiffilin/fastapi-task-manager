# app/db/database.py
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.models.task_model import Base

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

if not all(
    [POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_HOST, POSTGRES_PORT]
):
    raise ValueError("One or more PostgreSQL environment variables are not set.")

# String for ASYNCHRONOUS connection (for FastAPI)
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# String for SYNCHRONOUS connection (for migrations)
SQLALCHEMY_SYNC_DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)


# Asynchronous engine and session for the main application
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


# NEW: A function for synchronous table creation
def create_tables_sync():
    """
    Creates all tables synchronously.
    This function is intended to be called during the application's
    startup via the 'migrate' service in docker-compose.
    """
    sync_engine = create_engine(SQLALCHEMY_SYNC_DATABASE_URL)
    Base.metadata.create_all(bind=sync_engine)
    sync_engine.dispose()


# Dependency for asynchronous DB session
def get_db_session():
    db_session: AsyncSession = AsyncSessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
