# ==============================
# 🎯 NORMALIZED SCORING (0–100)
# ==============================
def safe_score(value):
    """Convert dict or None to numeric safely"""
    if isinstance(value, dict):
        return value.get("relevance_score", 0)
    if value is None:
        return 0
    return value

def calculate_skill_score(skills, job_description):
    jd = job_description.lower()
    matched = [s for s in skills if s.lower() in jd]

    if not skills:
        return 0.0

    return (len(matched) / len(skills)) * 100  # ✅ FIX


def calculate_experience_score(exp_relevance):
    return safe_score(exp_relevance)


def calculate_education_score(edu_score):
    return safe_score(edu_score)


def calculate_semantic_score(semantic_score):
    return safe_score(semantic_score)*100


# ==============================
# 🎯 FINAL ATS SCORE
# ==============================

def compute_ats_score(skill_score, exp_score, edu_score, semantic_score):

    final_score = (
        safe_score(skill_score) * 0.30 +
        safe_score(exp_score) * 0.25 +
        safe_score(edu_score) * 0.20 +
        safe_score(semantic_score) * 0.25
    )

    return round(final_score, 2)


# ==============================
# 🎯 BREAKDOWN
# ==============================

def generate_breakdown(skill_score, exp_score, edu_score, semantic_score):
    return {
        "skills": round(safe_score(skill_score), 2),
        "experience": round(safe_score(exp_score), 2),
        "education": round(safe_score(edu_score), 2),
        "semantic": round(safe_score(semantic_score), 2),
    }