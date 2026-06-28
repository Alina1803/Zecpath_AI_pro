def build_report(
    candidate,
    score,
    decision,
):

    return {
        "candidate": candidate["name"],
        "score": score,
        "decision": decision,
        "summary": "Production review completed",
    }
