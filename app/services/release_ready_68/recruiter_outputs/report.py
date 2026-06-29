def generate_report(
    candidate,
    score,
    decision,
):

    return {
        "name": candidate["name"],
        "score": score,
        "decision": decision,
        "summary": "Validated output",
    }
