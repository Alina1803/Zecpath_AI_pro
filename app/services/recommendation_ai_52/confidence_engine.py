def calculate_confidence(scores):

    if not scores:
        return 0

    variance = max(scores) - min(scores)

    confidence = max(100 - variance, 50)

    return round(confidence, 2)
