from fastapi import APIRouter, Depends, UploadFile, File 
import os
import json
from flask import json
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.resume import Resume
from app.schemas.resume_schema import ResumeResponse
from app.services.section_segmenter import ResumeSectionSegmenter
from app.services.resume_parser import parse_resume
from typing import Dict

router = APIRouter()

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

os.makedirs(RAW_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(RAW_FOLDER, file.filename)

    # Save uploaded resume
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Parse resume
    parsed_data = parse_resume(file_path)

    # Save JSON
    json_path = os.path.join(PROCESSED_FOLDER, file.filename + ".json")

    with open(json_path, "w") as f:
        json.dump(parsed_data, f, indent=4)

    return {
        "message": "Resume uploaded and parsed successfully",
        "resume_file": file.filename,
        "parsed_file": json_path,
        "data": parsed_data
    }