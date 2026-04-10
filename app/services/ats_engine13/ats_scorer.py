# ==========================================
# 🎯 ATS SCORER (PRODUCTION READY)
# ==========================================

from app.config.ca_domain_config import SKILL_DATABASE

def normalize_list(data):
    """Convert list of dicts/strings → clean lowercase string list"""
    clean = []

    for item in data:
        if isinstance(item, dict):
            # Try common keys
            value = item.get("skill") or item.get("name") or str(item)
        else:
            value = str(item)

        clean.append(value.lower())

    return clean
# ==============================
# 🎯 SAFE VALUE HANDLER
# ==============================
def safe_score(value):
    if isinstance(value, dict):
        return value.get("relevance_score", 0)
    if value is None:
        return 0
    return value


# ==============================
# 🎯 SKILL SCORE (GLOBAL + JD)
# ==============================
def calculate_skill_score(resume_skills, jd_skills):

    resume_set = set(normalize_list(resume_skills))
    jd_set = set(normalize_list(jd_skills))
    domain_set = set(s.lower() for s in SKILL_DATABASE)

    if not resume_set:
        return 0.0

    jd_match = resume_set & jd_set
    domain_match = resume_set & domain_set

    jd_score = (len(jd_match) / len(jd_set)) * 100 if jd_set else 0
    domain_score = (len(domain_match) / len(domain_set)) * 100 if domain_set else 0

    return round((jd_score * 0.7) + (domain_score * 0.3), 2)

# ==============================
# 🎯 EXPERIENCE SCORE
# ==============================
def calculate_experience_score(resume_exp, jd_exp):

    # Normalize JD experience
    if isinstance(jd_exp, list):
        min_exp = min(jd_exp)
        max_exp = max(jd_exp)
    else:
        min_exp = max_exp = jd_exp

    # Normalize resume experience
    if isinstance(resume_exp, list):
        resume_exp = max(resume_exp)

    # Handle edge case
    if min_exp == 0:
        return 100

    # Scoring
    if resume_exp >= min_exp:
        if resume_exp <= max_exp:
            return 100   # perfect match
        return 90        # slightly overqualified
    else:
        return round((resume_exp / min_exp) * 100, 2)


# ==============================
# 🎯 EDUCATION SCORE
# ==============================
def calculate_education_score(resume_edu, jd_edu):
    resume_set = set(normalize_list(resume_edu))
    jd_set = set(normalize_list(jd_edu))

    if not jd_set:
        return 100

    return 100 if resume_set.intersection(jd_set) else 50


# ==============================
# 🎯 SEMANTIC SCORE
# ==============================
def calculate_semantic_score(semantic_score):
    return round(safe_score(semantic_score) * 100, 2)


# ==============================
# 🎯 FINAL ATS SCORE
# ==============================
def compute_ats_score(skill_score, exp_score, edu_score, semantic_score):
    final_score = (
        skill_score * 0.30 +
        exp_score * 0.25 +
        edu_score * 0.20 +
        semantic_score * 0.25
    )
    return round(final_score, 2)


# ==============================
# 🎯 BREAKDOWN + INSIGHTS
# ==============================
def generate_breakdown(resume_data, jd_data,
                       skill_score, exp_score, edu_score, semantic_score):

    resume_skills = set(normalize_list(resume_data.get("skills", [])))
    jd_skills = set(normalize_list(jd_data.get("skills", [])))

    matched_skills = list(resume_skills.intersection(jd_skills))
    missing_skills = list(jd_skills - resume_skills)

    return {
        "skills_score": skill_score,
        "experience_score": exp_score,
        "education_score": edu_score,
        "semantic_score": semantic_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }


# ==============================
# 🎯 MAIN ATS FUNCTION
# ==============================
def calculate_score(resume_data, jd_data, semantic_raw=None):

    # -------- Skills --------
    resume_skills = resume_data.get("skills", [])
    jd_skills = jd_data.get("skills", [])
    skill_score = calculate_skill_score(resume_skills, jd_skills)

    # -------- Experience --------
    resume_exp = resume_data.get("experience", 0)
    jd_exp = jd_data.get("experience", 0)
    exp_score = calculate_experience_score(resume_exp, jd_exp)

    # -------- Education --------
    resume_edu = resume_data.get("education", [])
    jd_edu = jd_data.get("education", [])
    edu_score = calculate_education_score(resume_edu, jd_edu)

    # -------- Semantic --------
    if semantic_raw is not None:
        semantic_score = calculate_semantic_score(semantic_raw)
    else:
        semantic_score = skill_score  # fallback

    # -------- Final Score --------
    final_score = compute_ats_score(
        skill_score,
        exp_score,
        edu_score,
        semantic_score
    )

    # -------- Breakdown --------
    breakdown = generate_breakdown(
        resume_data,
        jd_data,
        skill_score,
        exp_score,
        edu_score,
        semantic_score
    )

    return {
        "final_score": final_score,
        "breakdown": breakdown
    }