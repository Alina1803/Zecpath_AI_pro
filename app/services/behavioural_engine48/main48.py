from fastapi import FastAPI

from app.models.model48 import BehaviorRequest

from app.services.behavioural_engine48.scoring_engine import behavioral_pipeline

app = FastAPI(title="Behavioral AI API")


@app.get("/")
def home():

    return {"message": "Behavioral AI System Running"}


@app.post("/analyze")
def analyze_behavior(data: BehaviorRequest):

    result = behavioral_pipeline(data)

    return result
