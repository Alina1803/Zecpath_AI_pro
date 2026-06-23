from fastapi import FastAPI

from app.services.hiring_report_generator_53.hiring_report_pipeline import (
    HiringReportPipeline,
)

app = FastAPI(title="Zecpath Hiring Intelligence API", version="53.0")

pipeline = HiringReportPipeline()


@app.get("/")
def home():

    return {"message": "Day 53 Hiring Intelligence API Running"}


@app.post("/generate-report")
def generate_report(candidate_data: dict):

    result = pipeline.generate(candidate_data)

    return result
