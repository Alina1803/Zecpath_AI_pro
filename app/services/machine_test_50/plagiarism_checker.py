# --------------------------------------
# Plagiarism Detection Logic
# --------------------------------------


def plagiarism_risk(similarity):

    if similarity > 80:
        return "High Risk"

    elif similarity > 50:
        return "Moderate Risk"

    return "Low Risk"
