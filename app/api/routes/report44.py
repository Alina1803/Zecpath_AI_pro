from fastapi import APIRouter
from app.services.doc_api_44.scoring_engine import calculate_score

router = APIRouter()

@router.get("/report/{session_id}")
def get_report(session_id: str):
    score = calculate_score()

    return {
        "candidate_id": "C101",
        "final_score": score,
        "decision": "Strong Hire" if score > 75 else "Reject"
    }