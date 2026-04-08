def generate_fairness_report(candidates):
    """
    Generate fairness health report.
    """
    normalized_scores = [
        c["scores"]["normalized_score"]
        for c in candidates
    ]

    avg_score = round(sum(normalized_scores) / len(normalized_scores), 2)

    return {
        "total_candidates": len(candidates),
        "average_normalized_score": avg_score,
        "score_range": {
            "min": min(normalized_scores),
            "max": max(normalized_scores)
        }
    }