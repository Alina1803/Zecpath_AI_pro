from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_screen():
    response = client.post("/screen", json={"features": [2, 3]})
    assert response.status_code == 200
    assert "selected" in response.json()