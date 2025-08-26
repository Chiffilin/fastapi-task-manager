# tests/test_debug.py
from fastapi.testclient import TestClient
from app.main import app


def test_debug_routes():
    """Debug all available routes"""
    client = TestClient(app)

    print("=== ALL REGISTERED ROUTES ===")
    for route in app.routes:
        path = getattr(route, "path", "N/A")
        methods = getattr(route, "methods", ["N/A"])
        print(f"{path} - {methods}")

    print("\n=== TESTING PATHS ===")
    test_paths = ["/", "/health", "/docs", "/api/tasks", "/tasks"]
    for path in test_paths:
        try:
            response = client.get(path)
            print(f"GET {path} -> {response.status_code}")
        except Exception as e:
            print(f"GET {path} -> ERROR: {e}")


if __name__ == "__main__":
    test_debug_routes()
