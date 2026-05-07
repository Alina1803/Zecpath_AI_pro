def generate_summary(scores):
    """
    Generate final HR interview summary

    Parameters:
    - scores: dictionary containing interview scores

    Returns:
    - strengths
    - weaknesses
    - cultural fit
    """

    strengths = []
    weaknesses = []

    # -----------------------------------
    # Communication Analysis
    # -----------------------------------
    if scores["communication"] >= 75:
        strengths.append("Strong communication skills")
    else:
        weaknesses.append("Needs communication improvement")

    # -----------------------------------
    # Confidence Analysis
    # -----------------------------------
    if scores["confidence"] >= 70:
        strengths.append("Good confidence level")
    else:
        weaknesses.append("Low confidence detected")

    # -----------------------------------
    # Aptitude Analysis
    # -----------------------------------
    if scores["aptitude"] >= 75:
        strengths.append("Good problem-solving ability")
    else:
        weaknesses.append("Needs aptitude improvement")

    # -----------------------------------
    # Cultural Fit Analysis
    # -----------------------------------
    average_score = (
        scores["communication"] +
        scores["confidence"] +
        scores["aptitude"]
    ) / 3

    if average_score >= 75:
        cultural_fit = "Excellent"
    elif average_score >= 60:
        cultural_fit = "Good"
    else:
        cultural_fit = "Needs Improvement"

    # -----------------------------------
    # Final Summary Object
    # -----------------------------------
    summary = {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "cultural_fit": cultural_fit
    }

    return summary