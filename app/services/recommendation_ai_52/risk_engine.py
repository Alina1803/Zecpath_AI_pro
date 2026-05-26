def apply_risk_penalty(score, behavior_risk, integrity_risk):

    penalty = 0

    if behavior_risk == "High Risk":
        penalty += 10

    elif behavior_risk == "Moderate Risk":
        penalty += 5

    if integrity_risk == "High Risk":
        penalty += 15

    elif integrity_risk == "Moderate Risk":
        penalty += 7

    adjusted_score = max(score - penalty, 0)

    return adjusted_score