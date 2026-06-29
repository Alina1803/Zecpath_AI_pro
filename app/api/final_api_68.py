from fastapi import FastAPI

from app.services.release_ready_68.ai_core.release_ready_system import (
    ReleaseReadySystem,
)

app = FastAPI()


@app.post("/release-run")
async def release_run(data: dict):

    return ReleaseReadySystem.process(data)
