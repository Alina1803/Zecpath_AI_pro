import os
import json
import shutil
import requests

from fastapi import FastAPI, UploadFile, File, Form

app = FastAPI()

# =========================================================
# 📦 DAY 21 PIPELINE
# =========================================================
from app.services.eligibility_engine21.main_pipeline21 import (
    run_pipeline
)

# =========================================================
# 🧠 DAY 22 MODULES
# =========================================================
from app.services.hr_screening_22.validator import (
    validate
)

from app.services.hr_screening_22.question_generator import (
    generate_ca_questions
)

from app.services.hr_screening_22.ai_layer.question_objects import (
    build_question_object
)

# =========================================================
# ⚙️ CONFIG
# =========================================================
API_URL = "http://127.0.0.1:8000/process"

RESUME_FOLDER = "data/raw"

OUTPUT_FOLDER = (
    "data/processed/output_22"
)

QUESTIONS_PATH = (
    "app/services/hr_screening_22/"
    "dataset/ca_questions.json"
)

CATEGORY_MAPPING_PATH = (
    "app/services/hr_screening_22/"
    "dataset/category_mapping.json"
)

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)

# =========================================================
# 📦 LOAD JSON
# =========================================================
def load_json(path):

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception as e:

        print(f"JSON Load Error: {e}")

        return []


questions_data = load_json(
    QUESTIONS_PATH
)

category_mapping = load_json(
    CATEGORY_MAPPING_PATH
)

# =========================================================
# 🎯 ROLE DETECTION
# =========================================================
def detect_role_from_jd(jd_text):

    if not jd_text:
        return "default"

    jd_text = jd_text.lower()

    for role, data in category_mapping.items():

        keywords = data.get(
            "keywords",
            []
        )

        for keyword in keywords:

            if keyword.lower() in jd_text:

                return role

    return "default"

# =========================================================
# 💾 SAVE OUTPUT
# =========================================================
def save_output(
    file_name,
    data
):

    try:

        output_path = os.path.join(
            OUTPUT_FOLDER,
            file_name + ".json"
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"\n✅ Saved Output: "
            f"{output_path}"
        )

    except Exception as e:

        print(
            f"Save Output Error: {e}"
        )

# =========================================================
# 🧠 BUILD QUESTION SET
# =========================================================
def build_dynamic_questions(role):

    role_data = category_mapping.get(
        role,
        {}
    )

    role_skills = role_data.get(
        "skills",
        []
    )

    generated_questions = (
        generate_ca_questions(
            skills=role_skills
        )
    )

    return generated_questions

# =========================================================
# 🚀 HR SCREENING ENHANCEMENT
# =========================================================
def enhance_with_hr_screening(
    result,
    resume_file
):

    # =====================================================
    # BASIC SAFETY
    # =====================================================

    if not isinstance(result, dict):

        return {
            "error": "Invalid result format"
        }

    decision = result.get(
        "decision",
        {}
    )

    status = decision.get(
        "final_status",
        "rejected"
    ).lower()

    role = decision.get(
        "role_detected",
        "default"
    )

    # =====================================================
    # BUILD CANDIDATE OBJECT
    # =====================================================

    candidate = {

        "id": resume_file,

        "score": result.get(
            "ats_score",
            0
        ),

        "skills": result.get(
            "skills",
            []
        ),

        "experience": result.get(
            "experience",
            0
        )
    }

    # =====================================================
    # ROLE SKILL BOOST
    # =====================================================

    role_skills = category_mapping.get(
        role,
        {}
    ).get(
        "skills",
        []
    )

    candidate_skills = " ".join(
        candidate.get(
            "skills",
            []
        )
    ).lower()

    bonus = 0

    for skill in role_skills:

        if skill.lower() in candidate_skills:

            bonus += 5

    # =====================================================
    # APPLY BONUS
    # =====================================================

    candidate["score"] += bonus

    result["ats_score"] = (
        result.get("ats_score", 0)
        + bonus
    )

    result["skill_bonus"] = bonus

    # =====================================================
    # VALIDATION
    # =====================================================

    is_valid = validate(candidate)

    result["is_valid"] = is_valid

    # =====================================================
    # REJECTED / REVIEW
    # =====================================================

    if status in [
        "rejected",
        "review"
    ]:

        result["generated_questions"] = []

        result["ai_questions"] = []

        result["message"] = (
            f"Candidate {status.upper()}"
        )

        return result

    # =====================================================
    # GENERATE QUESTIONS
    # =====================================================

    generated_questions = (
        build_dynamic_questions(role)
    )

    ai_questions = []

    for question in questions_data:

        try:

            ai_questions.append(
                build_question_object(
                    question
                )
            )

        except Exception as e:

            print(
                f"Question Object Error: {e}"
            )

    # =====================================================
    # FINAL RESULT
    # =====================================================

    result["generated_questions"] = (
        generated_questions
    )

    result["ai_questions"] = (
        ai_questions
    )

    result["message"] = (
        "Candidate shortlisted "
        "for HR interview"
    )

    return result

# =========================================================
# 🌐 FASTAPI ROUTE
# =========================================================
@app.post("/process")
async def process_resume_api(
    resume: UploadFile = File(...),
    jd: str = Form(...)
):

    try:

        # =================================================
        # SAVE TEMP FILE
        # =================================================

        os.makedirs(
            "temp",
            exist_ok=True
        )

        temp_path = os.path.join(
            "temp",
            resume.filename
        )

        with open(
            temp_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                resume.file,
                buffer
            )

        # =================================================
        # RUN DAY 21
        # =================================================

        result = run_pipeline(
            temp_path,
            jd
        )

        # =================================================
        # ROLE DETECTION
        # =================================================

        role = detect_role_from_jd(
            jd
        )

        if "decision" in result:

            result["decision"][
                "role_detected"
            ] = role

        # =================================================
        # DAY 22 ENHANCEMENT
        # =================================================

        final_result = (
            enhance_with_hr_screening(
                result,
                resume.filename
            )
        )

        return final_result

    except Exception as e:

        return {
            "error": str(e)
        }

# =========================================================
# ✅ DIRECT MODE
# =========================================================
def process_resumes_direct():

    print(
        "\n🚀 Running DAY 22 "
        "DIRECT PIPELINE\n"
    )

    jd_text = (
        "CA with GST and "
        "Income Tax experience"
    )

    role = detect_role_from_jd(
        jd_text
    )

    print(
        f"🎯 Role Detected: {role}"
    )

    for file in os.listdir(
        RESUME_FOLDER
    ):

        path = os.path.join(
            RESUME_FOLDER,
            file
        )

        if not os.path.isfile(path):
            continue

        try:

            # =============================================
            # DAY 21
            # =============================================

            result = run_pipeline(
                path,
                jd_text
            )

            # =============================================
            # ROLE INJECTION
            # =============================================

            if "decision" in result:

                result["decision"][
                    "role_detected"
                ] = role

            # =============================================
            # DAY 22
            # =============================================

            final_result = (
                enhance_with_hr_screening(
                    result,
                    file
                )
            )

            # =============================================
            # DEBUG
            # =============================================

            print(
                "\n======================"
            )

            print(
                f"Resume : {file}"
            )

            print(
                f"Status : "
                f"{final_result.get('decision', {})}"
                f".get('final_status')"
            )

            print(
                f"Message : "
                f"{final_result.get('message')}"
            )

            print(
                "======================"
            )

            print(
                json.dumps(
                    final_result,
                    indent=2
                )
            )

            # =============================================
            # SAVE OUTPUT
            # =============================================

            file_name = os.path.splitext(
                file
            )[0]

            save_output(
                file_name,
                final_result
            )

        except Exception as e:

            print(
                f"\n❌ Error Processing "
                f"{file}: {e}"
            )

# =========================================================
# 🌐 API MODE
# =========================================================
def process_resumes_api():

    print(
        "\n🌐 Running DAY 22 "
        "API MODE\n"
    )

    jd_text = (
        "CA with GST and "
        "Income Tax experience"
    )

    role = detect_role_from_jd(
        jd_text
    )

    for file in os.listdir(
        RESUME_FOLDER
    ):

        path = os.path.join(
            RESUME_FOLDER,
            file
        )

        if not os.path.isfile(path):
            continue

        try:

            with open(path, "rb") as f:

                response = requests.post(
                    API_URL,
                    files={
                        "resume": f
                    },
                    data={
                        "jd": jd_text
                    }
                )

            result = response.json()

            if "decision" in result:

                result["decision"][
                    "role_detected"
                ] = role

            final_result = (
                enhance_with_hr_screening(
                    result,
                    file
                )
            )

            print(
                "\n======================"
            )

            print(
                f"Resume : {file}"
            )

            print(
                f"Status : "
                f"{final_result.get('decision', {})}"
                f".get('final_status')"
            )

            print(
                "======================"
            )

            print(
                json.dumps(
                    final_result,
                    indent=2
                )
            )

            file_name = os.path.splitext(
                file
            )[0]

            save_output(
                file_name,
                final_result
            )

        except Exception as e:

            print(
                f"\n❌ API Error "
                f"for {file}: {e}"
            )

# =========================================================
# 🚀 ENTRY POINT
# =========================================================
if __name__ == "__main__":

    process_resumes_direct()

    # process_resumes_api()