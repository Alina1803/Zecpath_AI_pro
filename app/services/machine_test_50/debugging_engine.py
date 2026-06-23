# --------------------------------------
# Debugging Capability Engine
# --------------------------------------


def debugging_score(errors_fixed):

    if errors_fixed >= 8:
        return 1.0

    elif errors_fixed >= 5:
        return 0.7

    return 0.4
