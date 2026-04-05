def score_skill_confidence(skill, text):
    score = 0.5

    occurrences = text.lower().count(skill.lower())

    if occurrences >= 3:
        score += 0.3
    elif occurrences == 2:
        score += 0.2
    elif occurrences == 1:
        score += 0.1

    skill_sections = ["skills", "technical skills", "tools"]

    for section in skill_sections:
        if section in text.lower():
            score += 0.1
            break

    return min(score, 1.0)