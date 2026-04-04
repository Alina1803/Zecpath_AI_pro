from fastapi import FastAPI
from app.api import education

app = FastAPI(title="ZecPath AI - Resume Parser")

app.include_router(education.router, prefix="/api")