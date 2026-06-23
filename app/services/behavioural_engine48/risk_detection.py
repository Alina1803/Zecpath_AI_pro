# -----------------------------------
# Behavioral Risk Detection
# -----------------------------------


def detect_behavior_risk(score):

    if score < 50:
        return "High Risk"

    elif score < 70:
        return "Moderate Risk"

    return "Low Risk"
