import json
import re
import os
import pypdf
import pdfplumber
from collections import defaultdict
import warnings
import logging

warnings.filterwarnings("ignore")
logging.getLogger("pdfminer").setLevel(logging.ERROR)
# ----------- Resume Parser -----------
def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


# ----------- Skill Extractor -----------
def extract_skills(text):

    text = text.lower()
    text = text.replace("-", " ")

    skills_master = [
        "python",
        "sql",
        "django",
        "machine learning",
        "data analysis",
        "excel",
        "inventory",
        "sales",
        "point of sale",
        "pos",
        "aws",
        "docker",
        "html",
        "css",
        "javascript"
    ]

    found_skills = []

    for skill in skills_master:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


# ----------- Pipeline -----------
def run_pipeline():

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    RAW_FOLDER = os.path.join(BASE_DIR, "data", "raw")
    PROCESSED_FOLDER = os.path.join(BASE_DIR, "data", "processed")

    os.makedirs(PROCESSED_FOLDER, exist_ok=True)

    print("Pipeline running...\n")

    for file in os.listdir(RAW_FOLDER):

        if file.endswith(".pdf"):

            file_path = os.path.join(RAW_FOLDER, file)

            print(f"Processing: {file}")

            text = extract_text_from_pdf(file_path)

            skills = extract_skills(text)

            result = {
                "file": file,
                "skills": skills,
                "raw_text": text[:500]
            }

            output_file = file.replace(".pdf", ".json")

            with open(os.path.join(PROCESSED_FOLDER, output_file), "w") as f:
                json.dump(result, f, indent=4)

            print("Saved:", output_file)

    print("\nPipeline completed")


# ----------- Run Script -----------
if __name__ == "__main__":
    run_pipeline()