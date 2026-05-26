THRESHOLDS = {
    "selected": 80,
    "hold": 60
}

def generate_decision(score):

    if score >= THRESHOLDS["selected"]:
        return "Selected"

    elif score >= THRESHOLDS["hold"]:
        return "Hold / Review"

    return "Rejected"