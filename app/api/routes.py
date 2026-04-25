from fastapi import APIRouter
from pydantic import BaseModel
from app.models.loader32 import load_model
from app.services.ai_screening_system_32.screening import screen_candidate

router = APIRouter()

# Load model once
model = load_model("app/models/model32.pkl")

class Candidate(BaseModel):
    features: list

@router.post("/screen")
def screen(candidate: Candidate):
    result = screen_candidate(candidate.features, model)
    return result