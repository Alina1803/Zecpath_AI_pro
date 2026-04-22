def communication_strength(confidence, contradiction):
    score = confidence - (contradiction * 2)
    return max(round(score, 2), 0)