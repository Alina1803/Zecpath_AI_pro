def detect_contradiction(text):
    contradictions = ["but", "however", "although"]

    count = sum(word in text.lower() for word in contradictions)

    return min(count / 3, 1.0)