def score_candidate(response):
    """
    Rule-based scoring function
    """
    score = 0
    text = response.lower()

    if len(text) > 20:
        score += 1
    if "experience" in text:
        score += 1
    if "skill" in text or "skills" in text:
        score += 1

    return score