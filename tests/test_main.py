from fastapi import status


def test_docs_endpoint(client):
    """Test that docs are available"""
    response = client.get("/docs")
    assert response.status_code == status.HTTP_200_OK
    assert "swagger-ui" in response.text
