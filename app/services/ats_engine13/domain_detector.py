import re

from app.config.ca_domain_config import (
    DOMAIN_NAME,
    DEFAULT_ROLES,
    SKILL_DATABASE,
    DOMAIN_KEYWORDS,
    MIN_CA_SKILL_MATCH,
    MIN_CA_MATCH_PERCENT,
)


def normalize(text):
    return str(text).lower().strip()


def safe_match(keyword, text):

    pattern = r"\b" + re.escape(normalize(keyword)) + r"\b"

    return re.search(pattern, normalize(text))


def detect_ca_domain(resume_data):

    skills = [normalize(skill) for skill in resume_data.get("skills", [])]

    resume_text = " ".join(
        [
            str(resume_data.get("summary", "")),
            str(resume_data.get("designation", "")),
            str(resume_data.get("education", "")),
            str(resume_data.get("experience_text", "")),
        ]
    ).lower()

    # --------------------------------------
    # Skill Matching
    # --------------------------------------
    domain_skills = set(normalize(skill) for skill in SKILL_DATABASE)

    matched_skills = list(set(skills).intersection(domain_skills))

    missing_skills = list(domain_skills - set(skills))

    # --------------------------------------
    # Role Matching
    # --------------------------------------
    matched_roles = [role for role in DEFAULT_ROLES if safe_match(role, resume_text)]

    # --------------------------------------
    # Keyword Matching
    # --------------------------------------
    matched_keywords = [
        keyword for keyword in DOMAIN_KEYWORDS if safe_match(keyword, resume_text)
    ]

    # --------------------------------------
    # Match %
    # --------------------------------------
    match_percentage = 0

    if domain_skills:

        match_percentage = (len(matched_skills) / len(domain_skills)) * 100

    # --------------------------------------
    # Final Decision
    # --------------------------------------
    domain_match = (
        len(matched_skills) >= MIN_CA_SKILL_MATCH
        or match_percentage >= MIN_CA_MATCH_PERCENT
        or len(matched_roles) >= 1
        or len(matched_keywords) >= 2
    )

    confidence_score = min(
        (len(matched_skills) * 5)
        + (len(matched_roles) * 10)
        + (len(matched_keywords) * 5),
        100,
    )

    return {
        "domain_match": domain_match,
        "domain_name": (DOMAIN_NAME if domain_match else "non_ca"),
        "confidence_score": confidence_score,
        "match_percentage": round(match_percentage, 2),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills),
        "matched_roles": matched_roles,
        "matched_keywords": matched_keywords,
    }
