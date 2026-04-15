from rapidfuzz import fuzz
import re

from app.services.JD_Parser.text_cleaner import clean_text
from app.services.JD_Parser.skill_extractor import extract_skills
from app.services.JD_Parser.education_extractor import extract_education
from app.services.JD_Parser.experience_extractor import extract_experience
from app.services.JD_Parser.section_splitter import split_sections


# -------------------------------
# 🔥 DEFAULT ROLES (CA DOMAIN)
# -------------------------------
DEFAULT_ROLES = [
    "chartered_accountant","articleship","audit_associate","internal_auditor",
    "external_auditor","tax_consultant","tax_analyst",
    "gst_specialist","accountant","senior_accountant",
    "finance_executive","finance_manager","accounts_executive",
    "accounts_manager","payroll_specialist","compliance_officer",
    "risk_analyst","financial_analyst","cost_accountant"
]


# -------------------------------
# Role Detection (Fuzzy Matching)
# -------------------------------
def detect_roles(text, roles):
    detected = []

    for role in roles:
        score = fuzz.partial_ratio(role.replace("_", " "), text.lower())

        if score > 85:
            detected.append({
                "role": role,
                "confidence": score,
                "matched_keywords": [role]
            })

    return detected


# -------------------------------
# JD Parser (FINAL FIXED)
# -------------------------------
def parse_jd(jd_text, roles=None):
    """
    Parse job description with fallback-safe logic
    """

    # ✅ Fix: roles optional
    if roles is None:
        roles = DEFAULT_ROLES

    text = clean_text(jd_text)

    # -------------------------------
    # Sections
    # -------------------------------
    sections = split_sections(text)

    skills_text = (
        sections.get("skills", "") +
        sections.get("experience", "") +
        sections.get("responsibilities", "") +
        text
    )

    skills = extract_skills(skills_text)

    # -------------------------------
    # Extract structured data
    # -------------------------------
    education = extract_education(text)
    experience = extract_experience(text)

    # -------------------------------
    # Role Detection
    # -------------------------------
    detected_roles = detect_roles(text, roles)

    # 🔥 Pick best role for pipeline
    if detected_roles:
        primary_role = max(detected_roles, key=lambda x: x["confidence"])["role"]
    else:
        primary_role = "default"

    # -------------------------------
    # Fallback Logic
    # -------------------------------
    role_summary = sections.get("role_summary") or jd_text[:200]
    responsibilities = sections.get("responsibilities") or jd_text
    qualifications = sections.get("qualification")

    if not qualifications:
        qual_match = re.search(r"(must be.*|requirements?:.*)", jd_text.lower())
        qualifications = qual_match.group(0) if qual_match else jd_text

    # -------------------------------
    # Final Output
    # -------------------------------
    return {
        "role": primary_role,   # 🔥 IMPORTANT (for eligibility engine)
        "roles": detected_roles,

        "skills": skills,
        "education": education,
        "experience": experience,
        "sections": sections,

        "role_summary": role_summary.strip(),
        "responsibilities": responsibilities.strip(),
        "qualifications": qualifications.strip()
    }