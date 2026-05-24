from fastapi import FastAPI

from app.services.technical_skill_ai_47.models import AnswerRequest
from app.services.technical_skill_ai_47.scoring_engine import (
    calculate_technical_score
)

import uvicorn

app = FastAPI(
    title="Technical Skill Scoring API"
)


# -------------------------------
# Home Route
# -------------------------------
@app.get("/")
def home():

    return {
        "message": "Technical Skill Scoring API Running"
    }


# -------------------------------
# Evaluation Route
# -------------------------------
@app.post("/evaluate")
def evaluate_answer(data: AnswerRequest):

    result = calculate_technical_score(
        answer=data.answer,
        difficulty=data.difficulty,
        is_correct=data.is_correct
    )

    return result


# -------------------------------
# Run Server
# -------------------------------
if __name__ == "__main__":

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )