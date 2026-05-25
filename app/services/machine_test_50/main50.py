from fastapi import FastAPI

from app.services.machine_test_50.models import MachineTestRequest

from app.services.machine_test_50.scoring_pipeline import (
    machine_test_pipeline
)

app = FastAPI(
    title="Machine Test AI System"
)


@app.get("/")
def home():

    return {
        "message": "Machine Test AI Running"
    }


@app.post("/evaluate")
def evaluate(data: MachineTestRequest):

    return machine_test_pipeline(data)