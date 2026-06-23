def generate_explanation(scores):

    strengths = []
    weaknesses = []

    if scores.get("technical", 0) > 80:
        strengths.append("Strong technical skills")

    if scores.get("communication", 0) > 75:
        strengths.append("Good communication")

    if scores.get("behavior", 100) < 60:
        weaknesses.append("Behavioral concerns")

    if scores.get("integrity", 100) < 60:
        weaknesses.append("Integrity risks")

    return {"strengths": strengths, "weaknesses": weaknesses}
