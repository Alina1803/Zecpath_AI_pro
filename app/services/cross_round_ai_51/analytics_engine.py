# -----------------------------------
# Candidate Analytics Engine
# -----------------------------------


def candidate_strength(scores):

    strongest = max(scores, key=scores.get)

    weakest = min(scores, key=scores.get)

    return {"strongest_area": strongest, "weakest_area": weakest}
