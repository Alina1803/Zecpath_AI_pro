from fastapi import FastAPI

from app.api.interview_ai.interview_ai_api import (
    router,
)

app = FastAPI()

app.include_router(router)


@app.get("/")
async def home():

    return {"status": "running"}
