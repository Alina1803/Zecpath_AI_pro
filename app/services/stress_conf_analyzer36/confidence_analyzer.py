from app.config.constants36 import FILLER_WORDS, UNCERTAINTY_PHRASES
from utils.text_cleaner import clean_text

def calculate_confidence(text, duration):
    text = clean_text(text)
    words = text.split()
    total_words = len(words)

    # Hesitation
    filler_count = sum(text.count(word) for word in FILLER_WORDS)

    # Uncertainty
    uncertainty_count = sum(text.count(p) for p in UNCERTAINTY_PHRASES)

    # Repetition
    repetition_count = len(words) - len(set(words))

    # Pause (speech rate)
    speech_rate = total_words / max(duration, 1)
    optimal_rate = 2.5  # words/sec
    pause_penalty = abs(speech_rate - optimal_rate)

    # Normalize each (0–1)
    hesitation_score = min(filler_count / 5, 1)
    uncertainty_score = min(uncertainty_count / 5, 1)
    repetition_score = min(repetition_count / total_words if total_words else 0, 1)
    pause_score = min(pause_penalty / 5, 1)

    # Weighted confidence (inverse because these reduce confidence)
    confidence = 1 - (
        0.35 * hesitation_score +
        0.25 * uncertainty_score +
        0.20 * repetition_score +
        0.20 * pause_score
    )

    confidence = max(0, min(confidence, 1))

    return {
        "confidence_score": round(confidence * 100, 2)
    }