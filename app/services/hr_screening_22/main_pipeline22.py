import os
import json
import requests
from fastapi import FastAPI, UploadFile, File, Form
import shutil

app = FastAPI()

# -----------------------------
# 📦 DAY 21 PIPELINE
# -----------------------------
from app.services.eligibility_engine21.main_pipeline21 import run_pipeline

# -----------------------------
# 🧠 DAY 22 MODULES
# -----------------------------
from app.services.hr_screening_22.validator import validate
from app.services.hr_screening_22.question_generator import generate_ca_questions
from app.services.hr_screening_22.ai_layer.question_objects import build_question_object

# -----------------------------
# ⚙️ CONFIG
# -----------------------------
API_URL = "http://127.0.0.1:8000/process"
RESUME_FOLDER = "data/raw"
OUTPUT_FOLDER = "data/processed/output_22"

QUESTIONS_PATH = "app/services/hr_screening_22/dataset/ca_questions.json"
CATEGORY_MAPPING_PATH = "app/services/hr_screening_22/dataset/category_mapping.json"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.post("/process")
async def process_resume_api(
    resume: UploadFile = File(...),
    jd: str = Form(...)
):
    try:
        # -----------------------------
        # 📂 Save uploaded file temporarily
        # -----------------------------
        temp_path = os.path.join("temp", resume.filename)
        os.makedirs("temp", exist_ok=True)

        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        # -----------------------------
        # 🧠 Run Day 21 pipeline
        # -----------------------------
        result = run_pipeline(temp_path, jd)

        # -----------------------------
        # 🎯 Detect role
        # -----------------------------
        role = detect_role_from_jd(jd)

        if "decision" in result:
            result["decision"]["role_detected"] = role

        # -----------------------------
        # 🚀 Day 22 Enhancement
        # -----------------------------
        final_result = enhance_with_hr_screening(result, resume.filename)

        return final_result

    except Exception as e:
        return {"error": str(e)}

# =========================================================
# 📦 LOAD JSON
# =========================================================
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


questions_data = load_json(QUESTIONS_PATH)
category_mapping = load_json(CATEGORY_MAPPING_PATH)


# =========================================================
# 🎯 ROLE DETECTION (NEW)
# =========================================================
def detect_role_from_jd(jd_text):
    jd_text = jd_text.lower()

    for role, data in category_mapping.items():
        for keyword in data.get("keywords", []):
            if keyword in jd_text:
                return role

    return "default"


# =========================================================
# 💾 SAVE OUTPUT
# =========================================================
def save_output(file_name, data):
    output_path = os.path.join(OUTPUT_FOLDER, file_name + ".json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Saved: {output_path}")


# =========================================================
# 🧠 DAY 22 ENHANCEMENT (FIXED + BOOST ADDED)
# =========================================================
def enhance_with_hr_screening(result, resume_file):

    decision = result.get("decision", {})
    status = decision.get("final_status", "rejected").lower()

    # -----------------------------
    # 🧾 BUILD CANDIDATE
    # -----------------------------
    candidate = {
        "id": resume_file,
        "score": result.get("ats_score", 0),
        "skills": result.get("skills", []),
        "experience": result.get("experience", 0),
    }

    # -----------------------------
    # 🎯 ROLE BASED BOOST
    # -----------------------------
    role = decision.get("role_detected", "default")
    role_skills = category_mapping.get(role, {}).get("skills", [])

    candidate_skills = " ".join(candidate.get("skills", [])).lower()

    bonus = 0
    for skill in role_skills:
        if skill.lower() in candidate_skills:
            bonus += 5

    candidate["score"] += bonus
    result["ats_score"] += bonus

    # -----------------------------
    # ✅ VALIDATION
    # -----------------------------
    is_valid = validate(candidate)
    result["is_valid"] = is_valid

    # -----------------------------
    # ❌ REJECTED + REVIEW
    # -----------------------------
    if status in ["rejected", "review"]:
        result["generated_questions"] = []
        result["ai_questions"] = []
        result["message"] = f"Candidate {status.upper()}"

        return result

    # -----------------------------
    # ✅ ELIGIBLE
    # -----------------------------
    generated_questions = generate_ca_questions()
    ai_questions = [build_question_object(q) for q in questions_data]

    result["generated_questions"] = generated_questions
    result["ai_questions"] = ai_questions
    result["message"] = "Candidate shortlisted for interview"

    return result


# =========================================================
# ✅ DIRECT MODE (FIXED)
# =========================================================
def process_resumes_direct():
    print("\n Running in DIRECT mode (Day 22)\n")

    jd_text = "CA with GST and Income Tax experience"

    # 🔥 Detect role once
    role = detect_role_from_jd(jd_text)
    print(" Role Detected:", role)

    for file in os.listdir(RESUME_FOLDER):
        path = os.path.join(RESUME_FOLDER, file)

        try:
            # -----------------------------
            # Step 1: Day 21
            # -----------------------------
            result = run_pipeline(path, jd_text)

            # 🔥 Inject role into result
            if "decision" in result:
                result["decision"]["role_detected"] = role

            # -----------------------------
            # Step 2: Day 22
            # -----------------------------
            final_result = enhance_with_hr_screening(result, file)

            # -----------------------------
            # 🖨️ DEBUG OUTPUT
            # -----------------------------
            print("\n==============================")
            print(" Resume:", file)
            print(" Status:", final_result["decision"]["final_status"])
            print(" Message:", final_result.get("message"))
            print("==============================")

            print(json.dumps(final_result, indent=2))

            # -----------------------------
            # 💾 SAVE
            # -----------------------------
            file_name = os.path.splitext(file)[0]
            save_output(file_name, final_result)

        except Exception as e:
            print(f" Error processing {file}: {e}")


# =========================================================
# 🌐 API MODE
# =========================================================
def process_resumes_api():
    print("\n Running in API mode\n")

    jd_text = "CA with GST and Income Tax experience"
    role = detect_role_from_jd(jd_text)

    for file in os.listdir(RESUME_FOLDER):
        path = os.path.join(RESUME_FOLDER, file)

        try:
            with open(path, "rb") as f:
                response = requests.post(
                    API_URL,
                    files={"resume": f},
                    data={"jd": jd_text}
                )

            result = response.json()

            if "decision" in result:
                result["decision"]["role_detected"] = role

            final_result = enhance_with_hr_screening(result, file)

            print("\n==============================")
            print(" Resume:", file)
            print(" Status:", final_result["decision"]["final_status"])
            print("==============================")

            print(json.dumps(final_result, indent=2))

            file_name = os.path.splitext(file)[0]
            save_output(file_name, final_result)

        except Exception as e:
            print(f" API Error for {file}: {e}")
 

# =========================================================
# 🚀 ENTRY POINT
# =========================================================
if __name__ == "__main__":

    process_resumes_direct()
    # process_resumes_api()