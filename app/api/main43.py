from fastapi import FastAPI
from app.api.v1.endpoints import ethics43

app = FastAPI(title="Zecpath AI - Ethics API")

app.include_router(ethics43.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Ethics AI API running "}