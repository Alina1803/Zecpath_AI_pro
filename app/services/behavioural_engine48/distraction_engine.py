# -----------------------------------
# Distraction Detection
# -----------------------------------


def detect_distraction(value):

    if value > 0.7:
        return "Highly Distracted"

    elif value > 0.4:
        return "Moderately Distracted"

    return "Low Distraction"
