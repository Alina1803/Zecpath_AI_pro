from fastapi import FastAPI

from app.api.resume_parser_api.resume_api import (
    router as resume_router,
)

app = FastAPI()

app.include_router(resume_router)
