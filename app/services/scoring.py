from app.services.feature_store import extract_features

def score_candidate(data):
    features = extract_features(data)

    score = 0
    score += features["skill_count"] * 10
    score += features["experience"] * 5

    return min(score, 100)

def calculate_score(data, jd_data=None):
    """
    Main ATS scoring function
    """

    features = extract_features(data)

    # Safe extraction (no crash)
    skill_count = features.get("skill_count", 0)
    experience = features.get("experience", 0)

    score = 0

    # Skill weight
    score += skill_count * 10

    # Experience weight
    score += experience * 5

    # Optional: JD matching boost
    if jd_data:
        jd_keywords = jd_data.get("keywords", [])
        matched = [k for k in jd_keywords if k in str(data).lower()]
        score += len(matched) * 5

    return min(score, 100)
