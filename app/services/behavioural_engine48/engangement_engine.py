# -----------------------------------
# Engagement Detection
# -----------------------------------


def detect_engagement(level):

    if level > 0.8:
        return "Strong Engagement"

    elif level > 0.5:
        return "Moderate Engagement"

    return "Weak Engagement"
