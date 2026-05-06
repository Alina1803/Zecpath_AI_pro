from fastapi.testclient import TestClient
from app.services.doc_api_44.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "HR Interview AI Running"}


def test_start_interview():
    payload = {
        "candidate_id": "C101",
        "job_id": "J501",
        "role_type": "technical",
        "experience_level": "fresher"
    }

    response = client.post("/api/v1/start", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "session_id" in data
    assert "questions" in data
    assert isinstance(data["questions"], list)


def test_submit_answer():
    payload = {
        "session_id": "S123",
        "question_id": "Q1",
        "answer": "I have experience in Python",
        "duration": 5
    }

    response = client.post("/api/v1/answer", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert "follow_up" in data
    assert "next_question" in data


def test_get_report():
    response = client.get("/api/v1/report/S123")

    assert response.status_code == 200
    data = response.json()

    assert "final_score" in data
    assert "decision" in data