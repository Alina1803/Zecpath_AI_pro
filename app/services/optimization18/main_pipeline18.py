from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import shutil
import os
import uuid

# Services
from parsers.resume_parser import parse_resume
from app.utils.file_loader import load_file
from app.services.JD_Parser.jd_parser import parse_jd
from app.services.ats_engine13.ats_scorer import calculate_skill_score

# Optimization
from app.services.optimization18.performance_tracker import track_time
from app.services.optimization18.memory_manager import clear_memory

app = FastAPI()

UPLOAD_FOLDER = "data/raw"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".docx"}

DEFAULT_ROLES = [
    "Chartered Accountant", "Senior Chartered Accountant",
    "Tax Consultant", "Tax Manager", "Audit Manager",
    "Internal Auditor", "Financial Controller",
    "Finance Manager", "MIS Analyst", "FP&A Analyst",
    "Accounts Manager", "Cost Accountant",
    "Forensic Auditor", "Compliance Manager",
    "Treasury Manager", "Risk Analyst",
    "Financial Reporting Manager",
    "Business Finance Manager",
    "Virtual CFO", "Chief Financial Officer"
]

# ----------------------------------------
# 🛠️ Utility: Safe File Save
# ----------------------------------------
def save_file(file: UploadFile):
    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Only PDF/DOCX allowed")

    unique_name = f"{uuid.uuid4()}{ext}"
    file_path = os.path.join(UPLOAD_FOLDER, unique_name)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path


# ----------------------------------------
# 🚀 Single Resume Processing API
# ----------------------------------------
@app.post("/process")
@track_time
async def process_resume_api(
    file: UploadFile = File(...),
    jd_text: str = Form(...)
):
    try:
        file_path = save_file(file)

        resume_text = load_file(file_path)
        resume_data = parse_resume(resume_text)

        jd_data = parse_jd(jd_text, DEFAULT_ROLES)

        score = calculate_skill_score(resume_data, jd_data)

        return {
            "filename": file.filename,
            "score": score,
            "status": "success"
        }

    except Exception as e:
        print("PROCESS ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))


# ----------------------------------------
# ⚡ Batch Resume Processing API
# ----------------------------------------
@app.post("/process-batch")
@track_time
async def process_batch_api(
    files: list[UploadFile] = File(...),
    jd_text: str = Form(...)
):
    try:
        jd_data = parse_jd(jd_text, DEFAULT_ROLES)
        results = []

        for file in files:
            file_path = save_file(file)

            resume_text = load_file(file_path)
            resume_data = parse_resume(resume_text)

            score = calculate_skill_score(resume_data, jd_data)

            results.append({
                "filename": file.filename,
                "score": score
            })

        results = sorted(results, key=lambda x: x["score"], reverse=True)

        clear_memory()

        return {
            "total_resumes": len(results),
            "ranked_results": results,
            "status": "success"
        }

    except Exception as e:
        print("BATCH ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))


# ----------------------------------------
# ❤️ Health Check API
# ----------------------------------------
@app.get("/")
def health_check():
    return {"message": "ATS System Running Successfully 🚀"}