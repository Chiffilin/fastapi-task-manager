def test_simple():
    """Simple test to check that pytest works"""
    assert 1 + 1 == 2


# tests/test_simple.py
def test_imports():
    """Check that imports work"""
    import os

    os.environ["ENV"] = "test"  # Force test environment

    from app.core.config import settings

    print(f"Project name: {settings.PROJECT_NAME}")
    print(f"Debug mode: {settings.DEBUG}")

    # For tests, we just check that the settings are loaded
    assert hasattr(settings, "PROJECT_NAME")
    assert hasattr(settings, "DEBUG")
