from fastapi import FastAPI

from app.api.monitoring_61.monitoring_api import (
    router,
)

app = FastAPI(
    title="Monitoring API",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
async def home():

    return {
        "status": "running",
        "module": "Monitoring",
    }
