def compare(ai_score, human_score):
    diff = abs(ai_score - human_score)

    if diff <= 5:
        return "Match"
    elif diff <= 10:
        return "Close"
    else:
        return "Mismatch"