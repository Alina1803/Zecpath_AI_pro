from fastapi import FastAPI

from app.services.recommendation_ai_52.recommendation_pipeline import (
    recommendation_pipeline,
)

app = FastAPI()


@app.get("/generate_recommendation")
def generate():

    scores = {
        "technical": 88,
        "communication": 81,
        "behavior": 70,
        "integrity": 65,
        "final_score": 84,
    }

    result = recommendation_pipeline(
        candidate_id="C1001",
        scores=scores,
        behavior_risk="Low Risk",
        integrity_risk="Moderate Risk",
    )

    return result
