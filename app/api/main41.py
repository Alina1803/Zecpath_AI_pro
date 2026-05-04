from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Unified Scoring Engine API")

app.include_router(router)