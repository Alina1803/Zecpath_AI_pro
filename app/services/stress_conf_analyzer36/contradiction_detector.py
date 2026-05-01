from app.config.constants36 import CONTRADICTIONS
from utils.text_cleaner import clean_text

def detect_contradiction(text):
    text = clean_text(text)

    contradiction_found = 0

    for a, b in CONTRADICTIONS:
        if a in text and b in text:
            contradiction_found = 1
            break

    return contradiction_found * 100  # 0 or 100