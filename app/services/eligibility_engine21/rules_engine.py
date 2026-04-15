def normalize_text_list(items):
    """
    Normalize list of strings (lowercase + strip)
    """
    return [str(item).lower().strip() for item in items]


# -----------------------------
# ✅ 1. SCORE CHECK
# -----------------------------
def check_score(score: float, min_score: float) -> bool:
    return score >= min_score

 
# -----------------------------
# ✅ 2. EXPERIENCE CHECK
# -----------------------------
def check_experience(experience: float, min_experience: float) -> bool:
    return experience >= min_experience


# -----------------------------
# ✅ 3. MANDATORY SKILLS CHECK
# -----------------------------
def check_mandatory_skills(candidate_skills, mandatory_skills):
    candidate_skills = normalize_text_list(candidate_skills)
    mandatory_skills = normalize_text_list(mandatory_skills)

    missing_skills = [
        skill for skill in mandatory_skills if skill not in candidate_skills
    ]

    return len(missing_skills) == 0, missing_skills


# -----------------------------
# ✅ 4. CERTIFICATION CHECK (CA DOMAIN)
# -----------------------------
def check_certification(candidate, role):
    certifications = normalize_text_list(candidate.get("certifications", []))

    role = role.lower().strip().replace(" ", "_")

    # 🔥 Chartered Accountant
    if role == "chartered_accountant":
        keywords = ["ca", "chartered accountant", "aca", "icai"]

        return any(
            any(keyword in cert for keyword in keywords)
            for cert in certifications
        )

    # 🔥 Auditor
    elif role == "auditor":
        keywords = ["ca", "cpa", "audit"]

        return any(
            any(keyword in cert for keyword in keywords)
            for cert in certifications
        )

    # 🔥 Default → no strict certification required
    return True


# -----------------------------
# 🚀 MAIN VALIDATION ENGINE
# -----------------------------
def validate_candidate(candidate: dict, role: str, rule: dict) -> dict:
    """
    Unified validation engine:
    - Score
    - Experience
    - Skills
    - Certification
    """

    # Safe extraction
    score = candidate.get("score", 0)
    experience = candidate.get("experience", 0)
    skills = candidate.get("skills", [])

    # -----------------------------
    # Run Checks
    # -----------------------------
    score_ok = check_score(score, rule.get("min_score", 0))
    exp_ok = check_experience(experience, rule.get("min_experience", 0))

    skills_ok, missing_skills = check_mandatory_skills(
        skills,
        rule.get("mandatory_skills", [])
    )

    cert_ok = check_certification(candidate, role)

    # -----------------------------
    # Decision Logic
    # -----------------------------
    if score_ok and exp_ok and skills_ok and cert_ok:
        status = "Eligible"
    elif score_ok:
        status = "Review"
    else:
        status = "Rejected"

    # -----------------------------
    # Output
    # -----------------------------
    return {
        "status": status,
        "score": score,
        "missing_skills": missing_skills,
        "checks": {
            "score_ok": score_ok,
            "experience_ok": exp_ok,
            "skills_ok": skills_ok,
            "certification_ok": cert_ok
        }
    }