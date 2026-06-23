from fastapi import FastAPI

from app.services.cross_round_ai_51.models import AggregationRequest

from app.services.cross_round_ai_51.scoring_pipeline import aggregation_pipeline

app = FastAPI(title="Cross-Round Aggregation Engine")


@app.get("/")
def home():

    return {"message": "Cross-Round AI Running"}


@app.post("/aggregate")
def aggregate(data: AggregationRequest):

    return aggregation_pipeline(data)
