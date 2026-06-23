# --------------------------------------
# Time-Based Evaluation
# --------------------------------------


def time_score(time_taken, limit=30):

    ratio = time_taken / limit

    if ratio <= 0.5:
        return 1.0

    elif ratio <= 1.0:
        return 0.7

    return 0.4
