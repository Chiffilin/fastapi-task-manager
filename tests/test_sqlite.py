# tests/test_sqlite.py
from sqlalchemy import create_engine, text


def test_sqlite_connection():
    """Test that SQLite connection works"""
    # Create an in-memory SQLite engine
    engine = create_engine(
        "sqlite:///:memory:", connect_args={"check_same_thread": False}
    )

    # Check the connection
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        assert result.scalar() == 1
        print("SQLite connection successful!")
