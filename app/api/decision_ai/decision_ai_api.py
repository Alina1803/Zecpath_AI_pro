from fastapi import APIRouter
from pydantic import BaseModel

from app.services.cross_round_ai_51.decision_engine import (
    hiring_decision,
)

router = APIRouter(
    prefix="/decision",
    tags=["Decision AI"],
)


# Request Model
class DecisionRequest(BaseModel):

    score: float


# Decision Endpoint
@router.post("/predict")
async def decision_api(
    request: DecisionRequest,
):

    try:

        result = hiring_decision(request.score)

        return {
            "status": "success",
            "decision": result,
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e),
        }
