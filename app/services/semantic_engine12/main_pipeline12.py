import os
import json

from app.utils.text_cleaner import clean_text
from app.utils.file_loader import load_file

# 🔹 Skill + Experience
from app.services.skill_engine9.skill_extractor import SkillExtractor
from app.services.experience_engine.experience_parser import extract_experience

# 🔹 Education
from app.services.education_engine11.education_parser import extract_education
from app.services.education_engine11.certification_parser import extract_certifications
from app.services.education_engine11.education_relevance import education_relevance

# 🔹 Semantic Matching (Day 12)
from app.services.semantic_engine12.semantic_matcher import semantic_match


def run_pipeline(resume_text, job_description):
    """
    Full pipeline:
    Resume → Clean → Skills → Experience → Education → Semantic Matching
    """

    # 🔹 Clean
    cleaned_text = clean_text(resume_text)
    cleaned_jd = clean_text(job_description)

    # 🔹 Skills
    extractor = SkillExtractor()
    skills = extractor.extract_skills(cleaned_text)

    # 🔹 Experience
    experience = extract_experience(cleaned_text)

    # 🔹 Education
    education = extract_education(cleaned_text)
    certifications = extract_certifications(cleaned_text)

    # 🔹 Relevance
    edu_score = education_relevance(education, cleaned_jd)

    # 🔹 Semantic Matching
    semantic_score = semantic_match(cleaned_text, cleaned_jd)

    return {
        "skills": skills,
        "experience": experience,
        "education": education,
        "certifications": certifications,
        "education_relevance": edu_score,
        "semantic_match": semantic_score
    }


def main():
    input_folder = "data/raw"
    output_folder = "data/processed/output_12"

    os.makedirs(output_folder, exist_ok=True)

    job_description = """
    Looking for Chartered Accountant with strong audit, taxation,
    and financial analysis experience
    """

    all_results = []
    processed_count = 0

    for file_name in os.listdir(input_folder):

        if file_name.endswith((".txt", ".pdf", ".docx")):

            input_path = os.path.join(input_folder, file_name)

            try:
                # 🔥 Load file (supports OCR)
                resume_text = load_file(input_path)

                if not resume_text.strip():
                    print(f" Empty file: {file_name}")
                    continue

                # 🔥 Run pipeline
                result = run_pipeline(resume_text, job_description)

                # 🔹 Save output
                output_file = file_name.rsplit(".", 1)[0] + "_output.json"
                output_path = os.path.join(output_folder, output_file)

                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=4)

                all_results.append(result)
                processed_count += 1

                print(f" Processed: {file_name}")

            except Exception as e:
                print(f" Error processing {file_name}: {e}")

    print(f"\n Total processed: {processed_count}")
    print(" All resumes processed successfully!")


if __name__ == "__main__":
    main()