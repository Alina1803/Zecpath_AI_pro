import os
import json

from app.utils.text_cleaner import clean_text
from app.utils.file_loader import load_file
from app.services.experience_engine.skill_extractor import extract_skills
from app.services.experience_engine.experience_parser import extract_experience
from app.services.experience_engine.relevance_engine import experience_relevance
from app.utils.constants import ROLE_KEYWORDS


def run_pipeline(resume_text: str, job_description: str):
    """
    Full pipeline:
    Resume → Clean → Skills → Experience → Relevance
    """

    # Step 1: Clean text
    cleaned_text = clean_text(resume_text)
    cleaned_jd = clean_text(job_description)

    # Step 2: Extract skills
    skills = extract_skills(cleaned_text)

    # Step 3: Extract experience
    experience_data = extract_experience(cleaned_text)

    # Step 4: Relevance scoring
    relevance_data = experience_relevance(experience_data, cleaned_jd)

    return {
        "skills": skills,
        "experience": experience_data,
        "relevance": relevance_data
    }


def is_relevant_role(role):
    role = role.lower()
    return any(r in role for r in ROLE_KEYWORDS)


def main():
    input_folder = "data/raw"
    output_folder = "data/processed/output_10"

    # ✅ Create output folder
    os.makedirs(output_folder, exist_ok=True)

    job_description = """
    Looking for Chartered Accountant with strong audit and taxation experience
    """

    processed_count = 0

    # ✅ Loop through ALL file types
    for file_name in os.listdir(input_folder):

        if file_name.endswith((".txt", ".pdf", ".docx")):

            input_path = os.path.join(input_folder, file_name)

            try:
                # ✅ Load file (TXT / PDF / DOCX)
                resume_text = load_file(input_path)

                if not resume_text.strip():
                    print(f" Empty content: {file_name}")
                    continue

                # ✅ Run pipeline
                result = run_pipeline(resume_text, job_description)

                # ✅ Output file name
                output_file = file_name.rsplit(".", 1)[0] + "_output.json"
                output_path = os.path.join(output_folder, output_file)

                # ✅ Save result
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