# -------------------------------
# Logical Reasoning Engine
# -------------------------------


def logical_score(text):

    text = text.lower()

    if "first" in text and "then" in text:
        return 1.0

    elif len(text.split()) > 10:
        return 0.7

    return 0.4
