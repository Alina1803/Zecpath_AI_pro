def generate_backlog(mismatches):
    backlog = []

    for mismatch in mismatches:
        backlog.append({
            "issue": "Decision mismatch",
            "details": mismatch
        })

    return backlog