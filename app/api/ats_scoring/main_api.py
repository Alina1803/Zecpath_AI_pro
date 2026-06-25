import uvicorn
from fastapi import FastAPI

from app.api.ats_scoring.ats_scoring_api import (
    router as ats_router,
)

# ---------------------------------
# CREATE APP
# ---------------------------------

app = FastAPI(
    title="Zecpath AI API",
    version="1.0.0",
)

# ---------------------------------
# REGISTER ROUTER
# ---------------------------------

app.include_router(ats_router)

# ---------------------------------
# ROOT ENDPOINT
# ---------------------------------


@app.get("/")
async def home():

    return {
        "status": "running",
        "service": "ATS Scoring API",
    }


# ---------------------------------
# RUN SERVER
# ---------------------------------

if __name__ == "__main__":

    uvicorn.run(
        "main_api:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
