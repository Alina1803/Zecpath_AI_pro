# -----------------------------------
# Score Normalization
# -----------------------------------


def normalize_scores(scores):

    normalized = {}

    for k, v in scores.items():

        normalized[k] = max(min(v, 100), 0)

    return normalized
