# ----------------------------------------
# Recruiter Dashboard Payload
# ----------------------------------------


def recruiter_payload(candidate_id, score, risk, patterns, warnings):

    return {
        "candidate_id": candidate_id,
        "integrity_score": score,
        "risk_level": risk,
        "patterns_detected": patterns,
        "warnings": warnings,
    }
