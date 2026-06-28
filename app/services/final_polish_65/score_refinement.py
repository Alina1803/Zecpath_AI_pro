def normalize_score(score):

    if score < 0:
        score = 0

    if score > 100:
        score = 100

    return round(score)
