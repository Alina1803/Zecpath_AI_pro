def assign_decision(score):
    """
    Assign shortlist decision based on score thresholds.
    """
    if score >= 80:
        return "SHORTLIST"
    elif score >= 60:
        return "REVIEW"
    return "REJECT"


def apply_shortlisting(candidates):
    """
    Add decision field to ranked candidates.
    """
    for candidate in candidates:
        score = candidate["scores"]["final_score"]
        candidate["decision"] = assign_decision(score)

    return candidates