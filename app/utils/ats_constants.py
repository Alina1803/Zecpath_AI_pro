# ==============================
# 🎯 ATS WEIGHTS CONFIGURATION
# ==============================

# Default weights (must sum to 1.0)
WEIGHTS = {
    "skills": 0.30,
    "experience": 0.30,
    "education": 0.15,
    "semantic": 0.25
}


# ==============================
# 🎯 ROLE-BASED DYNAMIC WEIGHTS
# ==============================

ROLE_BASED_WEIGHTS = {
    "data scientist": {
        "skills": 0.40,
        "experience": 0.25,
        "education": 0.15,
        "semantic": 0.20
    },
    "software engineer": {
        "skills": 0.35,
        "experience": 0.30,
        "education": 0.10,
        "semantic": 0.25
    },
    "chartered accountant": {
        "skills": 0.25,
        "experience": 0.35,
        "education": 0.20,
        "semantic": 0.20
    }
}


# ==============================
# 🎯 SCORE THRESHOLDS
# ==============================

THRESHOLDS = {
    "excellent": 80,
    "good": 60,
    "average": 40,
    "poor": 0
}


# ==============================
# 🎯 MINIMUM REQUIREMENTS
# ==============================

MIN_REQUIREMENTS = {
    "min_skills_required": 2,
    "min_experience_months": 6
}


# ==============================
# 🎯 HELPER FUNCTION
# ==============================

def get_weights(job_description: str):
    """
    Return role-specific weights if detected,
    else return default weights.
    """
    jd = job_description.lower()

    for role, weights in ROLE_BASED_WEIGHTS.items():
        if role in jd:
            return weights

    return WEIGHTS


def classify_score(score: float):
    """
    Convert score into label
    """
    if score >= THRESHOLDS["excellent"]:
        return "Excellent"
    elif score >= THRESHOLDS["good"]:
        return "Good"
    elif score >= THRESHOLDS["average"]:
        return "Average"
    else:
        return "Poor"