from fastapi import FastAPI
from app.api.routes.hr_routes37 import router

app = FastAPI(
    title="Zecpath AI - HR Scoring API",
    version="1.0"
)

app.include_router(router, prefix="/hr", tags=["HR Scoring"])


@app.get("/")
def home():
    return {"message": "HR Scoring API Running "}