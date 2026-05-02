def calculate_accuracy(results):
    matches = 0

    for r in results:
        if abs(r["ai_score"] - r["human_score"]) <= 5:
            matches += 1

    return round((matches / len(results)) * 100, 2)