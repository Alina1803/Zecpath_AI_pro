# --------------------------------------
# Recruiter Report Generator
# --------------------------------------


def generate_report(candidate_id, final_score, breakdown):

    if final_score >= 80:
        decision = "Excellent"

    elif final_score >= 60:
        decision = "Good Performance"

    else:
        decision = "Needs Improvement"

    return {
        "candidate_id": candidate_id,
        "final_score": final_score,
        "decision": decision,
        "score_breakdown": breakdown,
    }
