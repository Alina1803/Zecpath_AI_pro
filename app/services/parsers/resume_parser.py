import re

# -----------------------------
# 🔧 BASIC TEXT CLEANER
# -----------------------------
def clean_text(text: str) -> str:
    return text.lower().replace("\n", " ").strip()


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
        "ledger"
    ]

    skills_found = []

    for skill in skill_keywords:
        if skill in text:
            skills_found.append(skill)

    return list(set(skills_found))


# -----------------------------
# 📊 EXPERIENCE EXTRACTION
# -----------------------------
def extract_experience(text: str):
    """
    Extract years of experience from resume text
    Example: '3 years experience'
    """
    matches = re.findall(r'(\d+)\+?\s+years?', text)

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
        "icai"
    ]

    found = []

    for cert in cert_keywords:
        if cert in text:
            found.append(cert)

    return list(set(found))


# -----------------------------
# 📄 MAIN PARSER FUNCTION
# -----------------------------
def parse_resume(file_path: str) -> dict:
    """
    Parse resume file and extract structured data
    """

    try:
        # -----------------------------
        # 📥 READ FILE
        # -----------------------------
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            raw_text = f.read()

        text = clean_text(raw_text)

        # -----------------------------
        # 🧠 EXTRACT DATA
        # -----------------------------
        skills = extract_skills(text)
        experience = extract_experience(text)
        certifications = extract_certifications(text)

        # -----------------------------
        # 📤 OUTPUT
        # -----------------------------
        return {
            "skills": skills,
            "experience_years": experience,
            "certifications": certifications,
            "raw_text": text[:500]  # optional preview
        }

    except Exception as e:
        return {
            "skills": [],
            "experience_years": 0,
            "certifications": [],
            "error": str(e)
        }