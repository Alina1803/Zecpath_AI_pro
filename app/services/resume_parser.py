import re
import os
from typing import List, Dict
import PyPDF2

# Example skill database (expand later)
SKILL_DATABASE = [
    "python", "java", "c++", "javascript",
    "react", "node.js", "django", "flask",
    "postgresql", "mysql", "aws", "docker",
    "machine learning", "data analysis"
]


def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + " "
    return text.lower()


def extract_skills(text: str) -> List[str]:
    found_skills = []
    for skill in SKILL_DATABASE:
        if skill.lower() in text:
            found_skills.append(skill)
    return list(set(found_skills))


def extract_experience(text: str) -> int:
    # Matches: 3 years, 5+ years, 2 yrs
    match = re.search(r'(\d+)\+?\s*(years|yrs)', text)
    if match:
        return int(match.group(1))
    return 0


def parse_resume(file_path: str) -> Dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError("Resume file not found")

    text = extract_text_from_pdf(file_path)

    parsed_data = {
        "skills": extract_skills(text),
        "experience_years": extract_experience(text),
        "raw_text": text[:1000]  # optional truncation
    }

    return parsed_data