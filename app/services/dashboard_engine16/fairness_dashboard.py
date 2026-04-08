def fairness_metrics(candidates):
    normalized = [
        c["scores"].get("normalized_score", 0)
        for c in candidates
    ]

    return {
        "average_fair_score": round(sum(normalized) / len(normalized), 2),
        "highest_score": max(normalized),
        "lowest_score": min(normalized)
    }