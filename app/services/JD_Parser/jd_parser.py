from rapidfuzz import fuzz
import re

from app.services.JD_Parser.text_cleaner import clean_text
from app.services.JD_Parser.skill_extractor import extract_skills
from app.services.JD_Parser.education_extractor import extract_education
from app.services.JD_Parser.experience_extractor import extract_experience
from app.services.JD_Parser.section_splitter import split_sections


# -------------------------------
# Role Detection (Fuzzy Matching)
# -------------------------------
def detect_roles(text, roles):
    detected = []

    for role in roles:
        score = fuzz.partial_ratio(role.lower(), text.lower())

        if score > 85:
            detected.append({
                "role": role,
                "confidence": score,
                "matched_keywords": [role]
            })

    return detected

# -------------------------------
# JD Parser (FINAL)
# -------------------------------
def parse_jd(jd_text, roles):
    text = clean_text(jd_text)

    # Split sections
    sections = split_sections(text)

    # Combine text for skill extraction
    skills_text = (
        sections.get("skills", "") +
        sections.get("experience", "") +
        sections.get("responsibilities", "") +
        text
    )

    skills = extract_skills(skills_text)

    # Extract other info
    education = extract_education(text)
    experience = extract_experience(text)

    # Detect roles
    detected_roles = detect_roles(text, roles)

    # -------------------------------
    # Fallback Logic (IMPORTANT)
    # -------------------------------
    role_summary = sections.get("role_summary")
    responsibilities = sections.get("responsibilities")
    qualifications = sections.get("qualification")

    if not role_summary:
        role_summary = jd_text[:200]

    if not responsibilities:
        responsibilities = jd_text

    if not qualifications:
        # smarter extraction
        qual_match = re.search(r"(must be.*|requirements?:.*)", jd_text.lower())
        qualifications = qual_match.group(0) if qual_match else jd_text

    # -------------------------------
    # Final Output
    # -------------------------------
    return {
        "roles": detected_roles,
        "skills": skills,
        "education": education,
        "experience": experience,
        "sections": sections,

        "role_summary": role_summary.strip(),
        "responsibilities": responsibilities.strip(),
        "qualifications": qualifications.strip()
    }