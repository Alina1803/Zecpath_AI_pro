import re


# -----------------------------
# 🔧 BASIC TEXT CLEANER
# -----------------------------
def clean_text(text: str) -> str:
    """
    Clean resume text while preserving original casing
    for better name extraction.
    """
    text = text.replace("\r", " ")
    text = text.replace("\n", "\n")
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# -----------------------------
# 🚫 WORDS THAT ARE NOT NAMES
# -----------------------------
INVALID_NAME_WORDS = {
    "django", "react", "fastapi", "python", "java",
    "accounting", "accountant", "chartered", "gst",
    "taxation", "audit", "developer", "engineer",
    "excel", "ledger", "compliance", "tally",
    "resume", "curriculum", "vitae", "email",
    "phone", "mobile", "contact", "address",
    "skills", "education", "experience"
}


# -----------------------------
# 👤 NAME EXTRACTION
# -----------------------------
def extract_name(raw_text: str):
    """
    Extract candidate name from resume top section.
    Prevents frameworks/libraries from being detected
    as names.
    """

    lines = [line.strip() for line in raw_text.split("\n") if line.strip()]

    # Only inspect top section
    for line in lines[:12]:

        # Remove symbols/numbers
        cleaned = re.sub(r"[^A-Za-z\s]", "", line).strip()

        # Normalize spaces
        cleaned = re.sub(r"\s+", " ", cleaned)

        words = cleaned.split()

        # Name usually has 2-4 words
        if not (2 <= len(words) <= 4):
            continue

        # Reject very long lines
        if len(cleaned) > 40:
            continue

        # All words should start uppercase
        if not all(word[0].isupper() for word in words):
            continue

        # Reject invalid keywords
        invalid = False

        for word in words:
            if word.lower() in INVALID_NAME_WORDS:
                invalid = True
                break

        if invalid:
            continue

        # Reject lines containing digits
        if re.search(r"\d", cleaned):
            continue

        return cleaned

    return "Unknown"


# -----------------------------
# 📧 EMAIL EXTRACTION
# -----------------------------
def extract_email(text: str):

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    matches = re.findall(pattern, text)

    return matches[0] if matches else "Not Found"


# -----------------------------
# 📱 PHONE EXTRACTION
# -----------------------------
def extract_phone(text: str):

    pattern = r"(\+91[\-\s]?)?[0]?(91)?[6789]\d{9}"

    matches = re.findall(pattern, text)

    if matches:
        # re.findall returns tuples because of groups
        numbers = re.finditer(pattern, text)

        for match in numbers:
            return match.group()

    return "Not Found"


# -----------------------------
# 🧠 SKILL EXTRACTION (CA DOMAIN)
# -----------------------------
def extract_skills(text: str):

    skill_keywords = [
        "accounting",
        "tally",
        "gst",
        "taxation",
        "income tax",
        "audit",
        "financial statements",
        "excel",
        "bank reconciliation",
        "compliance",
        "ledger",
        "bookkeeping",
        "payroll",
        "balance sheet",
        "cash flow"
    ]

    text_lower = text.lower()

    skills_found = []

    for skill in skill_keywords:

        if skill.lower() in text_lower:
            skills_found.append(skill)

    return sorted(list(set(skills_found)))


# -----------------------------
# 📊 EXPERIENCE EXTRACTION
# -----------------------------
def extract_experience(text: str):
    """
    Extract years of experience from resume text.

    Examples:
    - 3 years experience
    - 5+ years
    - 2 year experience
    """

    matches = re.findall(
        r'(\d+)\+?\s*(?:years?|yrs?)',
        text.lower()
    )

    if matches:
        return max([int(m) for m in matches])

    return 0


# -----------------------------
# 🎓 CERTIFICATION EXTRACTION
# -----------------------------
def extract_certifications(text: str):

    cert_keywords = [
        "ca",
        "chartered accountant",
        "b.com",
        "m.com",
        "cpa",
        "icai",
        "mba finance"
    ]

    text_lower = text.lower()

    found = []

    for cert in cert_keywords:

        if cert.lower() in text_lower:
            found.append(cert)

    return sorted(list(set(found)))


# -----------------------------
# 📄 MAIN PARSER FUNCTION
# -----------------------------
def parse_resume(file_path: str) -> dict:
    """
    Parse resume and extract structured data.
    """

    try:

        # -----------------------------
        # 📥 READ FILE
        # -----------------------------
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            raw_text = f.read()

        cleaned_text = clean_text(raw_text)

        # -----------------------------
        # 🧠 EXTRACT DATA
        # -----------------------------
        parsed_data = {
            "name": extract_name(raw_text),
            "email": extract_email(raw_text),
            "phone": extract_phone(raw_text),
            "skills": extract_skills(cleaned_text),
            "experience_years": extract_experience(cleaned_text),
            "certifications": extract_certifications(cleaned_text),
            "raw_text": cleaned_text[:500]
        }

        return parsed_data

    except Exception as e:

        return {
            "name": "Unknown",
            "email": "Not Found",
            "phone": "Not Found",
            "skills": [],
            "experience_years": 0,
            "certifications": [],
            "error": str(e)
        }