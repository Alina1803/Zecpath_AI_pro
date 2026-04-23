def score_answer(result: str):
    scores = {
        "good": 3,
        "average": 2,
        "poor": 1
    }
    return scores.get(result, 0)