def test_database_connection():
    """Test that database connection works with SQLite"""
    from app.db.database import engine
    from sqlalchemy import text

    # Check that we are using SQLite
    assert "sqlite" in str(engine.url)

    # Check the connection
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        assert result.scalar() == 1
