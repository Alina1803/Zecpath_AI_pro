def validate_input(text):
    issues = []

    if not text or text.strip() == "":
        return {
            "input": text,
            "status": "Rejected",
            "message": "Unable to process input"
        }

    if len(text.strip()) < 5:
        issues.append("too_short")

    return {
        "input": text,
        "issues_detected": issues,
        "status": "Processed"
    }