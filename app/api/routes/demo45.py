from fastapi import APIRouter
from app.models.schemas45 import DemoRequest
from app.services.demo_45.final_hr_engine import run_hr_interview

# Create router
router = APIRouter()


@router.post("/demo")
def run_demo(data: DemoRequest):
    """
    Run HR Interview AI Demo

    Input:
    - candidate_id
    - answers

    Output:
    - scores
    - final score
    - hiring decision
    """

    result = run_hr_interview(
        candidate_id=data.candidate_id,
        answers=data.answers
    )

    return {
        "status": "success",
        "message": "Demo interview processed successfully",
        "data": result
    }