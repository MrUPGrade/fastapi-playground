from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_read_main():
    response = client.get("/health/echo")
    assert response.status_code == 200
    assert response.json() == {"message": "hi"}
