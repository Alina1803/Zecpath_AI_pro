def evaluate_answer(answer: str):
    word_count = len(answer.split())

    if word_count > 6:
        return "good"
    elif word_count > 4:
        return "average"
    return "poor"