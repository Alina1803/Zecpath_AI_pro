def validate_prediction(candidate, expected_decision):
    predicted = candidate.get("decision", "UNKNOWN")

    return {
        "predicted": predicted,
        "expected": expected_decision,
        "match": predicted == expected_decision
    }