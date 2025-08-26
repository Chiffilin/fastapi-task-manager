import pytest
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Set up test environment and SQLite BEFORE imports
os.environ["ENV"] = "test"
os.environ["DATABASE_URL"] = "sqlite:///:memory:"
os.environ["DEBUG"] = "True"

# Import and create the application
from app.main import app
from app.db.database import Base, get_db

# In-memory test database (SQLite)
engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    """Create and clear the database for each test"""
    # Explicitly import Base after setting up the environment
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db):
    """Test client with an overridden database"""

    def override_get_db():
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    # Explicitly import and attach routers from the correct directory
    from app.api.routers.tasks import router  # ← Fixed import!

    app.include_router(router, tags=["tasks"])

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture
def test_task_data():
    """Data for a test task"""
    return {"title": "Test Task", "description": "Test Description", "completed": False}
