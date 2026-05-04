def get_decision(score):
    if score >= 75:
        return "Hire"
    elif score >= 55:
        return "Consider"
    return "Reject"