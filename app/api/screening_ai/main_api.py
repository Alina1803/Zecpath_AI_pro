from fastapi import FastAPI

from app.api.screening_ai.screening_ai_api import router

app = FastAPI(
    title="Screening AI API",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
async def home():

    return {
        "status": "running",
        "service": "Screening AI",
    }


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
    )
