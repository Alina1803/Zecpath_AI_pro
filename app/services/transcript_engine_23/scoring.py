def score_ca_answer(skills_detected):
    score = len(skills_detected) * 2

    if "gst" in skills_detected:
        score += 2
    if "audit" in skills_detected:
        score += 2

    return min(score, 10)