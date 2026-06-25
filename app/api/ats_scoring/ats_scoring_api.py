from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ats_scoring import (
    calculate_ats_score,
)

# ===================================
# ROUTER
# ===================================

router = APIRouter(
    prefix="/ats",
    tags=["ATS Scoring"],
)

# ===================================
# REQUEST MODEL
# ===================================


class ATSRequest(BaseModel):

    parsed_resume: dict
    job_requirements: dict


# ===================================
# ATS SCORE ENDPOINT
# ===================================


@router.post("/score")
async def ats_score_api(
    request: ATSRequest,
):

    try:

        result = calculate_ats_score(
            request.parsed_resume,
            request.job_requirements,
        )

        return {
            "status": "success",
            "data": result,
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e),
        }
