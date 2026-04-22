from app.services.signal_engine_27.hesitation_detector import detect_hesitation
from app.services.signal_engine_27.sentiment_analyzer import analyze_sentiment
from app.services.signal_engine_27.confidence_analyzer import compute_confidence
from app.services.signal_engine_27.contradiction_checker import detect_contradiction
from app.services.signal_engine_27.communication_scorer import communication_strength


class SignalEngine:

    def evaluate(self, answer):

        hesitation = detect_hesitation(answer)
        sentiment = analyze_sentiment(answer)
        contradiction = detect_contradiction(answer)

        confidence = compute_confidence(sentiment, hesitation)
        comm_score = communication_strength(confidence, contradiction)

        flags = []
        if hesitation > 0.4:
            flags.append("hesitation_detected")
        if contradiction > 0.3:
            flags.append("contradiction_detected")

        return {
            "behavioral_confidence": confidence,
            "sentiment_score": sentiment,
            "hesitation_score": hesitation,
            "contradiction_score": contradiction,
            "communication_strength": comm_score,
            "flags": flags
        }