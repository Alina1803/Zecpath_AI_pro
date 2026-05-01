from app.config.constants36 import STRESS_WORDS
from utils.text_cleaner import clean_text

def stress_score(text):
    text = clean_text(text)

    stress_count = sum(text.count(word) for word in STRESS_WORDS)

    score = min(stress_count / 5, 1)

    return round(score * 100, 2)