from fastapi import FastAPI

from app.api.decision_ai.decision_ai_api import (
    router,
)

app = FastAPI()

app.include_router(router)


@app.get("/")
async def home():

    return {"status": "running"}
