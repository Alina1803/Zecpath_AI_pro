# -------------------------------
# Difficulty Normalization
# -------------------------------

def normalize_difficulty(score, difficulty):

    multipliers = {
        "basic": 1.0,
        "intermediate": 1.1,
        "advanced": 1.2
    }

    adjusted = score * multipliers.get(difficulty, 1.0)

    return min(round(adjusted, 2), 100)