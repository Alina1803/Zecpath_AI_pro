from fastapi.testclient import TestClient
from app.services.demo_45.main import app

# -----------------------------------
# Create Test Client
# -----------------------------------
client = TestClient(app)


# -----------------------------------
# Test Root Endpoint
# -----------------------------------
def test_root():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "HR AI Running"
    assert data["status"] == "Production Ready"


# -----------------------------------
# Test Health Endpoint
# -----------------------------------
def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "OK"
    assert data["system"] == "HR Interview AI"


# -----------------------------------
# Test Demo API
# -----------------------------------
def test_demo_api():

    payload = {
        "candidate_id": "C1001",
        "answers": [
            {
                "question": "Tell me about yourself",
                "answer": "I am a Python developer"
            }
        ]
    }

    response = client.post(
        "/api/v1/demo",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert "final_score" in data["data"]
    assert "decision" in data["data"]


# -----------------------------------
# Test Report API
# -----------------------------------
def test_report_api():

    response = client.get("/api/v1/report/C1001")

    assert response.status_code == 200

    data = response.json()

    assert data["candidate_id"] == "C1001"
    assert data["status"] == "Completed"


# -----------------------------------
# Test Invalid Payload
# -----------------------------------
def test_invalid_demo_payload():

    payload = {
        "candidate": "WrongField"
    }

    response = client.post(
        "/api/v1/demo",
        json=payload
    )

    # FastAPI validation error
    assert response.status_code == 422