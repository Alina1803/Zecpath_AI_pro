from app.services.stress_conf_analyzer36.confidence_analyzer import (
    calculate_confidence
)


class ConfidenceEngine:

    @staticmethod
    def analyze(answer, duration):

        return calculate_confidence(
            answer,
            duration
        )