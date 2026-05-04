def generate_explanation(scores):
    explanation = {}

    explanation["ats"] = (
        "Strong resume match and skill alignment"
        if scores["ats"] >= 75 else
        "Resume needs improvement"
    )

    explanation["screening"] = (
        "Good response quality but minor gaps"
        if scores["screening"] >= 70 else
        "Needs better responses"
    )

    explanation["hr"] = (
        "Strong communication and confidence"
        if scores["hr"] >= 80 else
        "Average interpersonal skills"
    )

    return explanation