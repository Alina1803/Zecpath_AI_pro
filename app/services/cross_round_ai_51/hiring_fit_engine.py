# -----------------------------------
# Hiring Fit Classification
# -----------------------------------


def hiring_fit(score):

    if score >= 85:

        return "Excellent Fit"

    elif score >= 70:

        return "Strong Fit"

    elif score >= 55:

        return "Moderate Fit"

    return "Low Fit"
