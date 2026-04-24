def evaluate(results):
    correct = 0

    for r in results:
        if r['status'] == "Accepted":
            correct += 1

    accuracy = correct / len(results)
    return accuracy