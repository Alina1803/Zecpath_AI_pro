def compute_confidence(sentiment, hesitation):
    score = (sentiment * 0.7) + ((1 - hesitation) * 0.3)
    return round(score * 10, 2)