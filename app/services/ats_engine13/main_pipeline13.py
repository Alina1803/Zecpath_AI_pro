import os
import json

from app.utils.file_loader import load_file
from app.utils.text_cleaner import clean_text
from app.utils.ats_constants import WEIGHTS

# Engines
from app.services.skill_engine9.skill_extractor import extract_skills
from app.services.experience_engine.experience_parser import extract_experience
from app.services.experience_engine.relevance_engine import experience_relevance

from app.services.education_engine11.education_parser import extract_education
from app.services.education_engine11.certification_parser import extract_certifications
from app.services.education_engine11.education_relevance import education_relevance

from app.services.semantic_engine12.similarity_engine import semantic_similarity

# ATS
from app.services.ats_engine13.ats_scorer import (
    safe_score,
    generate_breakdown,
    compute_ats_score
)


def run_pipeline(resume_text, job_description):

    cleaned_text = clean_text(resume_text)
    cleaned_jd = clean_text(job_description)

    # -------- Extraction --------
    skills = extract_skills(cleaned_text)
    experience = extract_experience(cleaned_text)
    education = extract_education(cleaned_text)
    certifications = extract_certifications(cleaned_text)

    # -------- Scoring --------

    # ✅ Skill score (limit to 100)
    skill_score = min(len(skills) * 10, 100)

    # ✅ Experience score (FIXED)
    exp_data = experience_relevance(experience, cleaned_jd)  # CALL function
    exp_score = safe_score(exp_data)

    # ✅ Education score (SAFE)
    edu_data = education_relevance(education, cleaned_jd)
    edu_score = safe_score(edu_data)

    # ✅ Semantic score (SAFE + normalized)
    semantic_raw = semantic_similarity(cleaned_text, cleaned_jd)
    semantic_score = safe_score(semantic_raw) * 100

    # -------- ATS FINAL --------
    final_score = compute_ats_score(
        skill_score,
        exp_score,
        edu_score,
        semantic_score
    )

    # -------- Breakdown --------
    breakdown = generate_breakdown(
        skill_score,
        exp_score,
        edu_score,
        semantic_score
    )

    return {
        "skills": skills,
        "experience": experience,
        "education": education,
        "certifications": certifications,
        "scores": {
            "final_score": final_score,
            "breakdown": breakdown
        }
    }


def main():

    input_folder = "data/raw"
    output_folder = "data/processed/output_13"

    os.makedirs(output_folder, exist_ok=True)

    job_description = """
    Looking for Chartered Accountant with audit, taxation, and financial reporting skills
    """

    total = 0

    for file_name in os.listdir(input_folder):

        if file_name.endswith((".txt", ".pdf", ".docx")):

            input_path = os.path.join(input_folder, file_name)

            try:
                resume_text = load_file(input_path)

                if not resume_text.strip():
                    print(f"Empty: {file_name}")
                    continue

                result = run_pipeline(resume_text, job_description)

                output_file = file_name.rsplit(".", 1)[0] + "_output.json"
                output_path = os.path.join(output_folder, output_file)

                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=4)

                print(f"Processed: {file_name}")
                total += 1

            except Exception as e:
                print(f"Error: {file_name} → {e}")

    print(f"\nTotal processed: {total}")


if __name__ == "__main__":
    main()