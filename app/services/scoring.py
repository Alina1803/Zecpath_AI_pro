import re
from app.services.feature_store import extract_features


# -----------------------------
# 🔧 HELPER: Normalize Experience
# -----------------------------
def normalize_experience(exp):
    """
    Converts experience into integer safely
    """

    if isinstance(exp, int):
        return exp

    if isinstance(exp, str):
        match = re.search(r'\d+', exp)
        return int(match.group()) if match else 0

    if isinstance(exp, list):
        numbers = []
        for e in exp:
            match = re.search(r'\d+', str(e))
            if match:
                numbers.append(int(match.group()))
        return max(numbers) if numbers else 0

    return 0


# -----------------------------
# BASIC SCORER
# -----------------------------
def score_candidate(data):
    features = extract_features(data)

    skill_count = features.get("skill_count", 0)
    experience = normalize_experience(features.get("experience", 0))

    score = 0
    score += skill_count * 10
    score += experience * 5

    return min(score, 100)


# -----------------------------
# MAIN ATS SCORING
# -----------------------------
def calculate_score(data, jd_data=None):
    """
    Main ATS scoring function
    """

    features = extract_features(data)

    # ✅ Safe extraction
    skill_count = features.get("skill_count", 0)
    experience = normalize_experience(features.get("experience", 0))

    score = 0

    # -----------------------------
    # Skill weight
    # -----------------------------
    score += skill_count * 10

    # -----------------------------
    # Experience weight
    # -----------------------------
    score += experience * 5

    # -----------------------------
    # JD Matching Boost
    # -----------------------------
    if jd_data:
        jd_keywords = jd_data.get("keywords", [])

        matched = [
            k for k in jd_keywords
            if k in str(data).lower()
        ]

        score += len(matched) * 5

    return min(score, 100)