from fastapi import FastAPI
from app.services.final_polish_65.ai_core.final_production_system import (
    FinalProductionSystem,
)

app = FastAPI()


@app.post("/final-run")
async def final_run(data: dict):

    return FinalProductionSystem.process(data)
