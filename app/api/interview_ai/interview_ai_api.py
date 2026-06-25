from fastapi import APIRouter
from pydantic import BaseModel

from app.services.interview_ai import (
    evaluate_interview,
)

router = APIRouter(
    prefix="/interview",
    tags=["Interview AI"],
)


class InterviewRequest(BaseModel):
    transcript: str


@router.post("/evaluate")
async def evaluate_interview_api(
    request: InterviewRequest,
):

    try:

        result = evaluate_interview(request.transcript)

        return {
            "status": "success",
            "data": result,
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e),
        }
