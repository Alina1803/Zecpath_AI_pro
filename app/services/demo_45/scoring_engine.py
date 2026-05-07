def calculate_scores(answers):
    """
    Calculate HR Interview Scores

    Parameters:
    - answers: list of interview answers

    Returns:
    - communication score
    - confidence score
    - aptitude score
    - HR score
    - ATS score
    - screening score
    """

    # -----------------------------------
    # Dummy AI Logic (Replace Later)
    # -----------------------------------

    communication_score = 80
    confidence_score = 75
    aptitude_score = 78

    # -----------------------------------
    # HR Score Calculation
    # -----------------------------------
    hr_score = (
        communication_score +
        confidence_score +
        aptitude_score
    ) / 3

    hr_score = round(hr_score, 2)

    # -----------------------------------
    # ATS & Screening Scores
    # -----------------------------------
    ats_score = 70
    screening_score = 75

    # -----------------------------------
    # Final Scores Object
    # -----------------------------------
    scores = {
        "communication": communication_score,
        "confidence": confidence_score,
        "aptitude": aptitude_score,
        "hr": hr_score,
        "ats": ats_score,
        "screening": screening_score
    }

    return scores