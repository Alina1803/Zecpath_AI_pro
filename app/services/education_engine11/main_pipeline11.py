import os
import json

from app.utils.text_cleaner import clean_text
from app.utils.file_loader import load_file

from app.services.skill_engine9.skill_extractor import  SkillExtractor
from app.services.experience_engine.experience_parser import extract_experience

from app.services.education_engine11.education_parser import extract_education
from app.services.education_engine11.certification_parser import extract_certifications
from app.services.education_engine11.education_relevance import education_relevance


def run_pipeline(resume_text, job_description):
    """
    Full pipeline:
    Resume → Clean → Skills → Experience → Education → Relevance
    """

    cleaned_text = clean_text(resume_text)
    cleaned_jd = clean_text(job_description)

    # 🔹 Extraction
    extractor = SkillExtractor()
    skills = extractor.extract_skills(cleaned_text)
    experience = extract_experience(cleaned_text)

    education = extract_education(cleaned_text)
    certifications = extract_certifications(cleaned_text)

    # 🔹 Relevance
    edu_score = education_relevance(education, cleaned_jd)

    return {
        "skills": skills,
        "experience": experience,
        "education": education,
        "certifications": certifications,
        "education_relevance": edu_score
    }


def main():
    input_folder = "data/raw"
    output_folder = "data/processed/output_11"

    #  Create output folder
    os.makedirs(output_folder, exist_ok=True)

    job_description = """
    Looking for Chartered Accountant with strong audit and taxation experience
    """

    processed_count = 0

    # 🔥 Loop through all resumes
    for file_name in os.listdir(input_folder):

        if file_name.endswith((".txt", ".pdf", ".docx")):

            input_path = os.path.join(input_folder, file_name)

            try:
                # ✅ Load file (supports OCR via file_loader)
                resume_text = load_file(input_path)

                if not resume_text.strip():
                    print(f"⚠️ Empty file: {file_name}")
                    continue

                # ✅ Run pipeline
                result = run_pipeline(resume_text, job_description)

                # ✅ Output file name
                output_file = file_name.rsplit(".", 1)[0] + "_output.json"
                output_path = os.path.join(output_folder, output_file)

                #  Save JSON
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=4)

                processed_count += 1
                print(f" Processed: {file_name}")

            except Exception as e:
                print(f" Error processing {file_name}: {e}")

    print(f"\n Total processed: {processed_count}")
    print(" All resumes processed successfully!")


if __name__ == "__main__":
    main()