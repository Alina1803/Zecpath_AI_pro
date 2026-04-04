import re
import spacy

<<<<<<< HEAD
# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Skill database (keep same as job_parser for consistency)
=======
nlp = spacy.load("en_core_web_sm")

# You can expand this list
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
# NAME EXTRACTION
# -----------------------------
def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    # fallback (first line)
    return text.split("\n")[0]
# -----------------------------
# EMAIL EXTRACTION
# -----------------------------
def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group(0) if match else None

# -----------------------------
# PHONE EXTRACTION
# -----------------------------
def extract_phone(text):
    """
    Handles formats like:
    +91 9876543210
    98765-43210
    (987) 654-3210
    """
    match = re.search(r'(\+?\d{1,3}[\s-]?)?\d{10}', text)
    return match.group(0) if match else None
# -----------------------------
# SKILL EXTRACTION
# -----------------------------
=======

# -------------------------
# Personal Info Extraction
# -------------------------

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None


def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group() if match else None


def extract_phone(text):
    match = re.search(r'\+?\d[\d -]{8,}\d', text)
    return match.group() if match else None


# -------------------------
# Skills Extraction
# -------------------------

>>>>>>> f3c0930173c3eaf45f856e918e2731922b901711
def extract_skills(text):
    text_lower = text.lower()
    found_skills = []

    for skill in SKILL_DATABASE:
<<<<<<< HEAD
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return list(set(found_skills))
# -----------------------------
# EDUCATION EXTRACTION
# -----------------------------
=======
        if skill in text_lower:
            found_skills.append(skill)

    return list(set(found_skills))


# -------------------------
# Experience Extraction
# -------------------------

def extract_experience(text):
    matches = re.findall(r'(\d+)\+?\s*years?', text.lower())
    if matches:
        return max(matches) + " years"
    return None


# -------------------------
# Education Extraction
# -------------------------

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
            found.append(edu)

    return list(set(found))
# -----------------------------
# FULL RESUME PARSER
# -----------------------------
=======
        if edu in text_lower:
            found.append(edu)

    return list(set(found))


# -------------------------
# Main Parser Function
# -------------------------

>>>>>>> f3c0930173c3eaf45f856e918e2731922b901711
def parse_resume(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
<<<<<<< HEAD
        "education": extract_education(text)
    }
# -----------------------------
# TEST (Optional)
# -----------------------------
if __name__ == "__main__":
    sample_resume = """
    John Doe
    Email: john.doe@gmail.com
    Phone: +91 9876543210

    Skills:
    Python, Django, AWS, Docker

    Education:
    Bachelor of Technology in Computer Science
    """

    result = parse_resume(sample_resume)
    print(result)
=======
        "total_experience": extract_experience(text),
        "education": extract_education(text)
    }
>>>>>>> f3c0930173c3eaf45f856e918e2731922b901711
