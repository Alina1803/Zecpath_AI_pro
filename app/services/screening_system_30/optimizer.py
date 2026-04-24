def optimize_threshold(results):
    best_threshold = 2
    best_accuracy = 0

    for t in range(1, 5):
        correct = 0
        for r in results:
            if r['score'] >= t:
                correct += 1

        acc = correct / len(results)

        if acc > best_accuracy:
            best_accuracy = acc
            best_threshold = t

    return best_threshold, best_accuracy