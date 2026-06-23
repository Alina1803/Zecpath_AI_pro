from fastapi import FastAPI

from app.services.integrity_engine_49.models import IntegrityRequest

from app.services.integrity_engine_49.scoring_pipeline import integrity_pipeline

app = FastAPI(title="Integrity Detection API")


@app.get("/")
def home():

    return {"message": "Integrity Detection System Running"}


@app.post("/detect")
def detect_integrity(data: IntegrityRequest):

    return integrity_pipeline(data)
