def normalize_scores(candidates):
    """
    Min-max normalize candidate final scores to 0–100.
    """
    scores = [
        c["scores"]["final_score"]
        for c in candidates
    ]

    min_score = min(scores)
    max_score = max(scores)

    for candidate in candidates:
        score = candidate["scores"]["final_score"]

        if max_score == min_score:
            normalized = 100
        else:
            normalized = (
                (score - min_score) /
                (max_score - min_score)
            ) * 100

        candidate["scores"]["normalized_score"] = round(normalized, 2)

    return candidates