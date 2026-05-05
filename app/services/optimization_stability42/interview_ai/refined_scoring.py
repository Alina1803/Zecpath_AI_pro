def normalize_scores(scores):
    if not scores:
        return []

    min_s = min(scores)
    max_s = max(scores)

    if max_s == min_s:
        return scores

    return [(s - min_s) / (max_s - min_s) * 100 for s in scores]


def reduce_bias(score, confidence):
    # Confidence-aware adjustment
    adjusted = score * 0.9 + confidence * 0.1
    return round(adjusted, 2)


def refined_score_pipeline(scores, confidence_scores):
    normalized = normalize_scores(scores)

    final_scores = []
    for s, c in zip(normalized, confidence_scores):
        final_scores.append(reduce_bias(s, c))

    return final_scores