from fastapi import APIRouter
from app.services.unified_scoring_engine_41.pipeline.unified_pipeline import unified_pipeline

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Unified Scoring Engine API Running"}

@router.post("/score")
def score_candidate(data: dict):
    result = unified_pipeline(
        candidate_id=data["candidate_id"],
        ats=data["ats"],
        screening=data["screening"],
        hr=data["hr"],
        role=data.get("role", "fresher")
    )
    return result