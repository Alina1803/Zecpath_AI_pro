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


# =========================================================
# 🔥 CORE PIPELINE FUNCTION
# =========================================================
def run_pipeline(resume_path: str, jd_text: str):
    try:
        logging.info("[PIPELINE] Started")

        # -----------------------------
        # 📄 PARSING
        # -----------------------------
        parsed_resume = parse_resume(resume_path)
        parsed_jd = parse_jd(jd_text)

        logging.info("[PARSING DONE]")

        # -----------------------------
        # 🎯 SAFE EXTRACTION
        # -----------------------------
        skills = parsed_resume.get("skills", [])
        experience = parsed_resume.get("experience_years", 0)

        skills_text = " ".join(skills).lower()

        # -----------------------------
        # 🎯 SCORING LOGIC (FIXED)
        # -----------------------------
        score = 0

        if "gst" in skills_text:
            score += 25

        if "income tax" in skills_text:
            score += 25

        if "tally" in skills_text or "excel" in skills_text:
            score += 10

        if experience >= 2:
            score += 20

        if experience >= 5:
            score += 20

        # Cap score to 100
        score = min(score, 100)

        # -----------------------------
        # 🧾 BUILD CANDIDATE OBJECT (FIXED)
        # -----------------------------
        candidate = {
            "id": os.path.basename(resume_path),

            # 🔥 FORCE ROLE (IMPORTANT FIX)
            "role": "chartered_accountant",

            "score": score,
            "skills": skills,
            "experience": experience,
            "certifications": parsed_resume.get("certifications", [])
        }

        # -----------------------------
        # 🔍 DEBUG (VERY IMPORTANT)
        # -----------------------------
        print("\nDEBUG:")
        print("Score:", score)
        print("Skills:", skills)
        print("Experience:", experience)

        # -----------------------------
        # ⚡ DECISION ENGINE
        # -----------------------------
        decision = evaluate_candidate(candidate, rules)

        print("Final Status:", decision.get("final_status"))

        logging.info(f"[DECISION] Status: {decision.get('final_status')}")

        # -----------------------------
        # 💾 SAVE OUTPUT
        # -----------------------------
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(decision) + "\n")

        logging.info("[OUTPUT SAVED]")

        return {
            "ats_score": score,
            "decision": decision,
            "skills": skills,
            "experience": experience
        }

    except Exception as e:
        logging.error(f"[PIPELINE ERROR] {str(e)}")
        return {"error": str(e)}


# =========================================================
# 🚀 FASTAPI ENDPOINT
# =========================================================
@app.post("/process")
async def process(
    resume: UploadFile = File(...),
    jd: str = Form(...)
):
    try:
        logging.info(f"[API START] Processing file: {resume.filename}")

        # -----------------------------
        # 📁 SAVE FILE
        # -----------------------------
        file_path = os.path.join(UPLOAD_DIR, resume.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        logging.info(f"[FILE SAVED] {file_path}")

        # -----------------------------
        # 🔥 RUN PIPELINE
        # -----------------------------
        result = run_pipeline(file_path, jd)

        return {
            "message": "Processing successful",
            **result
        }

    except Exception as e:
        logging.error(f"[API ERROR] {str(e)}")
        return {"error": str(e)}