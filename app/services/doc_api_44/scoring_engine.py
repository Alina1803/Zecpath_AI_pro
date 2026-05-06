def calculate_score():
    relevance = 20
    communication = 20
    confidence = 20
    consistency = 18

    hr_score = relevance + communication + confidence + consistency

    ats = 75
    screening = 70

    final_score = (ats * 0.3) + (screening * 0.3) + (hr_score * 0.4)
    return int(final_score)