from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Screening System")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Screening System is running"}