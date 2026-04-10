from typing import Dict
from textblob import TextBlob

CONFIDENCE_KEYWORDS = {
    "high": [
        "led", "managed", "owned", "delivered", "achieved",
        "improved", "optimized", "increased", "reduced",
        "implemented", "developed", "executed", "driven",
        "spearheaded", "resolved", "handled independently"
    ],

    "medium": [
        "worked on", "assisted", "supported", "participated",
        "contributed", "involved in", "helped",
        "collaborated", "coordinated"
    ],

    "low": [
        "learned", "familiar with", "basic knowledge",
        "exposed to", "observed", "theoretical knowledge"
    ]
}


def calculate_sentiment_score(transcript: str) -> float:
    blob = TextBlob(transcript)
    polarity = blob.sentiment.polarity  # -1 to +1
    return (polarity + 1) / 2  # normalize to 0–1


def calculate_confidence_score(transcript: str) -> float:
    transcript = transcript.lower()
    count = sum(1 for word in CONFIDENCE_KEYWORDS if word in transcript)
    return min(count / 5, 1.0)


def calculate_communication_score(transcript: str) -> float:
    word_count = len(transcript.split())
    if word_count == 0:
        return 0
    avg_sentence_length = word_count / max(transcript.count("."), 1)
    return min(avg_sentence_length / 20, 1.0)


def score_interview(transcript: str) -> Dict:
    sentiment = calculate_sentiment_score(transcript)
    confidence = calculate_confidence_score(transcript)
    communication = calculate_communication_score(transcript)

    final_score = (0.4 * sentiment) + (0.3 * confidence) + (0.3 * communication)

    return {
        "sentiment_score": round(sentiment * 100, 2),
        "confidence_score": round(confidence * 100, 2),
        "communication_score": round(communication * 100, 2),
        "final_interview_score": round(final_score * 100, 2)
    }