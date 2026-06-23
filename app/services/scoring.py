import re
from app.services.feature_store import extract_features


# -----------------------------
# 🔧 HELPER: Normalize Experience
# -----------------------------
def normalize_experience(exp):
    """
    Converts experience into integer safely.
    """

    if isinstance(exp, int):
        return exp

    if isinstance(exp, str):
        match = re.search(r"\d+", exp)
        return int(match.group()) if match else 0

    if isinstance(exp, list):
        numbers = []

        for e in exp:
            match = re.search(r"\d+", str(e))

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

    score = skill_count * 10 + experience * 5

    return min(score, 100)


# -----------------------------
# MAIN ATS SCORING
# -----------------------------
def calculate_score(data, jd_data=None):
    """
    Main ATS scoring function
    """

    features = extract_features(data)

    print("\n========== ATS FEATURES ==========")
    print(features)

    skill_count = features.get(
        "skill_count",
        0,
    )

    experience = normalize_experience(
        features.get(
            "experience",
            0,
        )
    )

    score = 0

    # -----------------------------
    # Skills Weight
    # -----------------------------
    score += skill_count * 10

    # -----------------------------
    # Experience Weight
    # -----------------------------
    score += experience * 5

    matched_keywords = []

    # -----------------------------
    # JD Matching Weight
    # -----------------------------
    if jd_data:

        jd_keywords = jd_data.get("keywords", [])

        resume_text = str(data).lower()

        matched_keywords = [
            keyword for keyword in jd_keywords if keyword.lower() in resume_text
        ]

        score += len(matched_keywords) * 5

    final_score = min(score, 100)

    print("\n========== ATS DEBUG ==========")
    print("Skill Count:", skill_count)
    print("Experience:", experience)
    print("Matched Keywords:", matched_keywords)
    print("Final ATS Score:", final_score)

    return {
        "overall_score": final_score,
        "skill_count": skill_count,
        "experience": experience,
        "matched_keywords": matched_keywords,
    }
