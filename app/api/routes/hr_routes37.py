from fastapi import APIRouter, HTTPException
from app.services.interview_ai_37.hr_scoring_engine import hr_scoring_pipeline
from app.api.schemas.hr_schema37 import HRRequest

import os
import json
from datetime import datetime

router = APIRouter()


def save_output(data):
    os.makedirs("data/processed/output_37", exist_ok=True)

    filename = f"hr_output_37_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    path = os.path.join("data/processed", filename)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    return path


@router.post("/score")
async def score_candidate(request: HRRequest):

    if not request.answers:
        raise HTTPException(status_code=400, detail="Answers cannot be empty")

    result = hr_scoring_pipeline(
        answers=[a.dict() for a in request.answers],
        candidate_type=request.candidate_type
    )

    output = {
        "candidate_id": request.candidate_id,
        **result
    }

    save_output(output)

    return output