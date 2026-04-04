import re
import spacy

<<<<<<< HEAD
# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Predefined skill list (expand as needed)
=======
nlp = spacy.load("en_core_web_sm")

# Predefined skill list (you can expand this)
>>>>>>> f3c0930173c3eaf45f856e918e2731922b901711
SKILL_DATABASE = [
    "python", "java", "c++", "machine learning",
    "deep learning", "sql", "mongodb",
    "django", "flask", "fastapi",
    "aws", "docker", "kubernetes",
    "git", "linux", "excel", "power bi"
]

<<<<<<< HEAD
# -----------------------------
# SKILL EXTRACTION
# -----------------------------
=======
>>>>>>> f3c0930173c3eaf45f856e918e2731922b901711
def extract_skills(text):
    text_lower = text.lower()
    found_skills = []

    for skill in SKILL_DATABASE:
<<<<<<< HEAD
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
=======
        if skill in text_lower:
>>>>>>> f3c0930173c3eaf45f856e918e2731922b901711
            found_skills.append(skill)

    return list(set(found_skills))


<<<<<<< HEAD
# -----------------------------
# EXPERIENCE EXTRACTION
# -----------------------------
def extract_experience(text):
    """
    Extracts years of experience from job description.
    Examples:
    - 3 years
    - 5+ years
    - 2 yrs
    """
    text_lower = text.lower()
    match = re.search(r'(\d+)\+?\s*(years?|yrs?)', text_lower)

    return match.group(1) if match else None


# -----------------------------
# EDUCATION EXTRACTION
# -----------------------------
=======
def extract_experience(text):
    # Example: "3+ years", "5 years experience"
    match = re.search(r'(\d+)\+?\s*years?', text.lower())
    return match.group() if match else None


>>>>>>> f3c0930173c3eaf45f856e918e2731922b901711
def extract_education(text):
    education_keywords = [
        "bachelor", "master", "b.tech",
        "m.tech", "phd", "mba"
    ]

    text_lower = text.lower()
    found = []

    for edu in education_keywords:
<<<<<<< HEAD
        pattern = r'\b' + re.escape(edu) + r'\b'
        if re.search(pattern, text_lower):
=======
        if edu in text_lower:
>>>>>>> f3c0930173c3eaf45f856e918e2731922b901711
            found.append(edu)

    return list(set(found))


<<<<<<< HEAD
# -----------------------------
# JOB DESCRIPTION PARSER
# -----------------------------
=======
>>>>>>> f3c0930173c3eaf45f856e918e2731922b901711
def parse_job_description(text):
    return {
        "required_skills": extract_skills(text),
        "experience_required": extract_experience(text),
        "education_required": extract_education(text)
<<<<<<< HEAD
    }


# -----------------------------
# TEST (Optional)
# -----------------------------
if __name__ == "__main__":
    sample_jd = """
    We are looking for a Python developer with 3+ years of experience.
    Must have skills in Python, Django, and AWS.
    Bachelor's degree in Computer Science preferred.
    """

    result = parse_job_description(sample_jd)
    print(result)
=======
    }
>>>>>>> f3c0930173c3eaf45f856e918e2731922b901711
