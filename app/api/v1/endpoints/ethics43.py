from fastapi import APIRouter
from app.api.schemas.ethics_schema43 import CandidateRequest
from app.services.ethics_ai_43.main_pipeline import process_candidate

router = APIRouter()


@router.post("/evaluate")
def evaluate_candidate(candidate: CandidateRequest):

    result = process_candidate(candidate.dict())

    return {
        "status": "success",
        "result": result
    }