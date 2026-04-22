POSITIVE = ["confident", "clearly", "definitely", "accurate"]
NEGATIVE = ["not sure", "confused", "difficult", "maybe"]

def analyze_sentiment(text):
    text = text.lower()

    pos = sum(w in text for w in POSITIVE)
    neg = sum(w in text for w in NEGATIVE)

    score = (pos - neg) / max((pos + neg + 1), 1)

    return round((score + 1) / 2, 2)  # normalize 0–1