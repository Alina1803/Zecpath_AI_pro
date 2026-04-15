from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os
import json
import logging

# -----------------------------
# ⚙️ LOGGING CONFIG
# -----------------------------
logging.basicConfig(level=logging.INFO)

# -----------------------------
# 🚀 IMPORT SERVICES
# -----------------------------
from app.services.parsers.resume_parser import parse_resume
from app.services.parsers.jd_parser import parse_jd
from app.services.scoring import calculate_score

from app.services.eligibility_engine21.config_loader import load_rules
from app.services.eligibility_engine21.decision_engine import evaluate_candidate


# -----------------------------
# ⚙️ APP INIT
# -----------------------------
app = FastAPI()

UPLOAD_DIR = "data/raw"
OUTPUT_FILE = "data/processed/output_21/eligibility_results.json"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# Load rules once
rules = load_rules()


# -----------------------------
# 📌 MAIN API ENDPOINT
# -----------------------------
@app.post("/process")
async def process(
    resume: UploadFile = File(...),
    jd: str = Form(...)
):
    try:
        logging.info(f"[START] Processing file: {resume.filename}")

        # -----------------------------
        # 📁 SAVE FILE
        # -----------------------------
        file_path = os.path.join(UPLOAD_DIR, resume.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        logging.info(f"[FILE SAVED] {file_path}")

        # -----------------------------
        # 📄 PARSING
        # -----------------------------
        parsed_resume = parse_resume(file_path)
        parsed_jd = parse_jd(jd)

        logging.info("[PARSING DONE] Resume & JD parsed")

        # -----------------------------
        # 🧠 SCORING
        # -----------------------------
        score = calculate_score(parsed_resume, parsed_jd)

        logging.info(f"[SCORING DONE] ATS Score: {score}")

        # -----------------------------
        # 🧾 CANDIDATE
        # -----------------------------
        candidate = {
            "id": resume.filename,
            "role": parsed_jd.get("role", "default"),
            "score": score,
            "skills": parsed_resume.get("skills", []),
            "experience": parsed_resume.get("experience_years", 0),
            "certifications": parsed_resume.get("certifications", [])
        }

        # -----------------------------
        # ⚡ DECISION
        # -----------------------------
        decision = evaluate_candidate(candidate, rules)

        logging.info(f"[DECISION] Status: {decision.get('final_status')}")

        # -----------------------------
        # 💾 SAVE OUTPUT
        # -----------------------------
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(decision) + "\n")

        logging.info("[OUTPUT SAVED]")

        # -----------------------------
        # 📤 RESPONSE
        # -----------------------------
        return {
            "message": "Processing successful",
            "ats_score": score,
            "decision": decision
        }

    except Exception as e:
        logging.error(f"[ERROR] {str(e)}")
        return {"error": str(e)}