import re
import spacy
import pdfplumber
from app.config.ca_domain_config import SKILL_DATABASE, SKILL_SYNONYMS

nlp = spacy.load("en_core_web_sm")

SKILL_DATABASE = [
    "gst", "taxation", "tds", "tally", "sap fico",
    "financial reporting", "audit", "statutory audit",
    "internal audit", "bank reconciliation",
    "accounts payable", "accounts receivable",
    "mis reporting", "budgeting", "forecasting",
    "financial analysis", "ifrs", "gaap",
    "income tax", "roc filing", "compliance",
    "excel", "power bi", "cash flow",
    "cost accounting", "variance analysis"
]

def normalize_skills(text):
    text = text.lower()
    extracted = set()

    for skill in SKILL_DATABASE:
        if skill in text:
            extracted.add(skill)

        # 🔥 check synonyms
        if skill in SKILL_SYNONYMS:
            for synonym in SKILL_SYNONYMS[skill]:
                if synonym in text:
                    extracted.add(skill)

    return list(extracted)

# ----------------------------------------
# PDF TEXT EXTRACTION
# ----------------------------------------
def extract_text_from_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

    return text


# ----------------------------------------
# NAME EXTRACTION
# ----------------------------------------
def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return text.split("\n")[0] if text else None


# ----------------------------------------
# EMAIL EXTRACTION
# ----------------------------------------
def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group(0) if match else None


# ----------------------------------------
# PHONE EXTRACTION
# ----------------------------------------
def extract_phone(text):
    match = re.search(r'\+?\d[\d\s\-]{8,15}\d', text)
    return match.group(0) if match else None


# ----------------------------------------
# SKILL EXTRACTION
# ----------------------------------------
def extract_skills(text):
    text_lower = text.lower()
    found_skills = []

    for skill in SKILL_DATABASE:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return list(set(found_skills))


# ----------------------------------------
# EXPERIENCE EXTRACTION
# ----------------------------------------
def extract_experience(text):
    matches = re.findall(r'(\d+)\+?\s*years?', text.lower())

    if matches:
        return max([int(m) for m in matches])

    return 0


# ----------------------------------------
# EDUCATION EXTRACTION
# ----------------------------------------
def extract_education(text):
    education_keywords = [
        "bachelor", "master", "b.tech",
        "m.tech", "phd", "mba"
    ]

    text_lower = text.lower()
    found = []

    for edu in education_keywords:
        if re.search(r'\b' + re.escape(edu) + r'\b', text_lower):
            found.append(edu)

    return list(set(found))


# ----------------------------------------
# MAIN PARSER
# ----------------------------------------
def parse_resume(text):

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "experience": extract_experience(text),
        "education": extract_education(text)
    }