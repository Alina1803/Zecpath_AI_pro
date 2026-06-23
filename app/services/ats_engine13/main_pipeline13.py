import os
import json
from datetime import datetime

from app.utils.file_loader import load_file
from app.utils.text_cleaner import clean_text
from app.services.skill_engine9.skill_extractor import extract_skills
from app.services.experience_engine.experience_parser import extract_experience
from app.services.experience_engine.relevance_engine import experience_relevance
from app.services.education_engine11.education_parser import extract_education
from app.services.education_engine11.certification_parser import extract_certifications
from app.services.education_engine11.education_relevance import education_relevance
from app.services.semantic_engine12.similarity_engine import semantic_similarity

from app.services.ats_engine13.ats_scorer import calculate_score


# ==========================================
# SAFE NUMBER HANDLER
# ==========================================
def safe_number(value):

    if isinstance(value, dict):

        return value.get("relevance_score", 0)

    if value is None:

        return 0

    return value


# ==========================================
# PIPELINE RUNNER
# ==========================================
def run_pipeline(resume_text, job_description, file_name="unknown"):

    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(job_description)

    skills = extract_skills(cleaned_resume)
    jd_skills = extract_skills(cleaned_jd)
    experience = extract_experience(cleaned_resume)
    exp_relevance = experience_relevance(experience, cleaned_jd)
    education = extract_education(cleaned_resume)
    certifications = extract_certifications(cleaned_resume)
    edu_relevance = education_relevance(education, cleaned_jd)

    semantic_raw = semantic_similarity(cleaned_resume, cleaned_jd)

    resume_data = {
        "skills": skills,
        "experience": safe_number(experience),
        "education": education,
        "certifications": certifications,
        # 🔥 NEW
        "summary": cleaned_resume[:1000],
        "experience_text": str(experience),
    }

    # --------------------------------------
    # STRUCTURED JD DATA
    # --------------------------------------
    jd_data = {
        "skills": jd_skills,
        "experience": safe_number(exp_relevance),
        "education": [],
        # 🔥 NEW
        "job_description": cleaned_jd,
    }

    # --------------------------------------
    # ATS SCORING
    # --------------------------------------
    ats_result = calculate_score(resume_data, jd_data, semantic_raw)

    # --------------------------------------
    # FINAL PIPELINE OUTPUT
    # --------------------------------------
    return {
        "metadata": {"file_name": file_name, "processed_at": str(datetime.now())},
        "extracted_data": {
            "skills": skills,
            "experience": experience,
            "education": education,
            "certifications": certifications,
        },
        "semantic_similarity": semantic_raw,
        "scores": ats_result,
    }


# ==========================================
# MAIN EXECUTION
# ==========================================
def main():

    input_folder = "data/raw"

    output_folder = "data/processed/output_13"

    os.makedirs(output_folder, exist_ok=True)

    # --------------------------------------
    # SAMPLE JD
    # --------------------------------------
    job_description = """

    Looking for Chartered Accountant with:

    - GST
    - Taxation
    - Audit
    - Financial Reporting
    - SAP FICO
    - Compliance
    - Excel

    """

    total_processed = 0

    # --------------------------------------
    # PROCESS FILES
    # --------------------------------------
    for file_name in os.listdir(input_folder):

        if not file_name.endswith((".txt", ".pdf", ".docx")):

            continue

        input_path = os.path.join(input_folder, file_name)

        try:

            # ----------------------------------
            # LOAD FILE
            # ----------------------------------
            resume_text = load_file(input_path)

            # ----------------------------------
            # EMPTY CHECK
            # ----------------------------------
            if not resume_text.strip():

                print(f"⚠ Empty File: {file_name}")

                continue

            # ----------------------------------
            # RUN PIPELINE
            # ----------------------------------
            result = run_pipeline(resume_text, job_description, file_name=file_name)

            # ----------------------------------
            # OUTPUT FILE
            # ----------------------------------
            output_file = file_name.rsplit(".", 1)[0] + "_output.json"

            output_path = os.path.join(output_folder, output_file)

            # ----------------------------------
            # SAVE RESULT
            # ----------------------------------
            with open(output_path, "w", encoding="utf-8") as f:

                json.dump(result, f, indent=4)

            print(f"✅ Processed: {file_name}")

            total_processed += 1

        except Exception as e:

            print(f"❌ Error: {file_name}")
            print(f"Reason: {e}")

    print("\n======================")

    print(f" Total Processed: " f"{total_processed}")

    print("======================")


if __name__ == "__main__":

    main()
