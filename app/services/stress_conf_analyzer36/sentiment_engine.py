from app.config.constants36 import POSITIVE_WORDS, NEGATIVE_WORDS
from utils.text_cleaner import clean_text

def sentiment_score(text):
    text = clean_text(text)

    pos = sum(text.count(w) for w in POSITIVE_WORDS)
    neg = sum(text.count(w) for w in NEGATIVE_WORDS)

    total = pos + neg

    if total == 0:
        score = 0.5
    else:
        score = (pos - neg) / total  # -1 to 1
        score = (score + 1) / 2      # normalize to 0–1

    return {
        "sentiment_score": round(score * 100, 2)
    }