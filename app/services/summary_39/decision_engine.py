def calculate_overall_score(hr_scores, communication, behavior):

    hr_avg = sum(x["final_score"] for x in hr_scores) / len(hr_scores) if hr_scores else 0

    return round(
        communication["communication_score"] * 0.3 +
        behavior["behavioral_score"] * 0.3 +
        hr_avg * 0.4,
        2
    )


def get_decision(score):

    if score >= 75:
        return "Strong Hire"
    elif score >= 55:
        return "Consider"
    return "Reject"

def build_recommendation(decision, score):
    return {
        "status": decision,
        "confidence": "Strong Hire" if score >= 75 else "Consider" if score >= 55 else "Reject"
    }