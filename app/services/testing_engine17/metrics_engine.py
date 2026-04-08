def calculate_accuracy(results):
    if not results:
        return 0

    correct = sum(1 for r in results if r["match"])

    return round((correct / len(results)) * 100, 2)