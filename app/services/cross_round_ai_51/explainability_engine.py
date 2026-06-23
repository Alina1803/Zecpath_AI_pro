# -----------------------------------
# Explainable AI Layer
# -----------------------------------


def explain_scores(scores):

    explanation = {}

    if scores["ats"] >= 70:
        explanation["ats"] = "Strong resume-job alignment"

    else:
        explanation["ats"] = "Weak ATS compatibility"

    if scores["technical"] >= 80:
        explanation["technical"] = "Excellent technical capability"

    else:
        explanation["technical"] = "Technical skills require improvement"

    if scores["machine_test"] >= 75:
        explanation["machine_test"] = "Strong practical implementation"

    else:
        explanation["machine_test"] = "Practical execution below expectations"

    return explanation
