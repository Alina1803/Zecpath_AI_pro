from app.services.feature_store import extract_features

def score_candidate(data):
    features = extract_features(data)

    score = 0
    score += features["skill_count"] * 10
    score += features["experience"] * 5

    return min(score, 100)