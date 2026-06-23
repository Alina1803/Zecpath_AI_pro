# -----------------------------------
# Recruiter Reporting Engine
# -----------------------------------


def recruiter_summary(candidate_id, score):

    if score >= 80:
        summary = "Highly recommended candidate"

    elif score >= 65:
        summary = "Potential candidate with strong areas"

    else:
        summary = "Candidate requires improvement"

    return {"candidate_id": candidate_id, "recruiter_summary": summary}
