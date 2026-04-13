import os
import json

# ✅ IMPORT FROM UTILS
from app.utils.file_loader import  load_file

# ------------------------------
# IMPORT SAME LOGIC (IMPORTANT)
# -----------------------------
from app.services.JD_Parser.jd_parser import (
    clean_text, extract_skills,
    extract_experience, extract_education, parse_jd
)
from app.services.semantic_engine12.semantic_matcher import (
    match_skills, match_experience,match_education)
    
from app.services.semantic_engine12.similarity_engine import semantic_similarity 

from app.services.scoring import calculate_score

ROLES=["python developer",
       "backend developer",
       "data scientist", 
       "software engineer" 
       ]
# -----------------------------
# MAIN PIPELINE
# -----------------------------
def process_pipeline(resume_path, jd_path):

    resume_raw = load_file(resume_path)
    jd_raw = load_file(jd_path)

    resume_clean = clean_text(resume_raw)

    # ✅ DEBUG BLOCK (ADD HERE)
    print("\n==============================")
    print(f" Processing: {os.path.basename(resume_path)}")
    print(" Resume Text Sample:\n", resume_clean[:300])
    print("==============================\n")

    # ✅ (Optional but VERY useful)
    print(" JD Sample:\n", jd_raw[:300])

    # Parse JD
    jd_data = parse_jd(jd_raw, ROLES)

    # Extract
    resume_skills = extract_skills(resume_clean)
    resume_exp = extract_experience(resume_clean)
    resume_edu = extract_education(resume_clean)

    # Matching
    skill_score = match_skills(resume_skills, jd_data["skills"])
    exp_score = match_experience(resume_exp, jd_data["experience"])
    edu_score = match_education(resume_edu, jd_data["education"])

    semantic_score = semantic_similarity(resume_clean, jd_raw)

    candidate_data = {
        "skills": resume_skills,
        "experience": resume_exp,
        "education": resume_edu,
        "text": resume_clean
    }

    # Final Score
    final_score = calculate_score(candidate_data,jd_data)

    return {
        "resume": os.path.basename(resume_path),
        "extracted": {
            "skills": resume_skills,
            "experience": resume_exp,
            "education": resume_edu
        },
        "scores": {
            "skill_score": round(skill_score * 100, 2),
            "experience_score": round(exp_score * 100, 2),
            "education_score": round(edu_score * 100, 2),
            "semantic_score": round(semantic_score * 100, 2),
            "final_score": round(final_score, 2)
        }
    }

# -----------------------------
# RUN PIPELINE
# -----------------------------
if __name__ == "__main__":
    resume_folder = "ATS_pipeline_Demo19/data/resumes"
    jd_file = "ATS_pipeline_Demo19/data/jd/jd1.txt"

    output_folder = "ATS_pipeline_Demo19/data/output"
    os.makedirs(output_folder, exist_ok=True)

    results = []

    for file in os.listdir(resume_folder):
        path = os.path.join(resume_folder, file)

        result = process_pipeline(path, jd_file)
        results.append(result)

    # Ranking
    ranked = sorted(
        results,
        key=lambda x: x["scores"]["final_score"],
        reverse=True
    )

    # Save output
    output_path = os.path.join(output_folder, "results.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(ranked, f, indent=4)

    print("\n===== FINAL RANKING =====\n")
    for r in ranked:
        print(r)

    print(f"\n Results saved to: {output_path}")