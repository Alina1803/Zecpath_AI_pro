# -------------------------------
# Real World Applicability
# -------------------------------


def real_world_score(text):

    text = text.lower()

    if "production" in text or "real-world" in text:
        return 1.0

    elif "example" in text:
        return 0.7

    return 0.4
