from datetime import datetime


class PredictiveHiring:

    def __init__(self):

        self.selection_threshold = 75
        self.review_threshold = 55

    # -------------------------------------

    def normalize(self, value):

        try:
            value = float(value)

        except Exception:
            value = 0

        return max(
            0,
            min(value, 100),
        )

    # -------------------------------------

    def calculate_score(
        self,
        metrics,
    ):

        if not metrics:

            return 0

        cleaned = []

        for v in metrics.values():

            cleaned.append(self.normalize(v))

        return round(
            sum(cleaned) / len(cleaned),
            2,
        )

    # -------------------------------------

    def predict(
        self,
        candidate_id,
        metrics,
    ):

        score = self.calculate_score(metrics)

        confidence = round(
            score / 100,
            2,
        )

        if score >= self.selection_threshold:

            decision = "Selected"

            probability = "High"

        elif score >= self.review_threshold:

            decision = "Review Required"

            probability = "Medium"

        else:

            decision = "Rejected"

            probability = "Low"

        return {
            "candidate_id": candidate_id,
            "hiring_score": score,
            "confidence": confidence,
            "selection_probability": probability,
            "decision": decision,
            "timestamp": str(datetime.now()),
        }


# -------------------------------------
# TEST
# -------------------------------------

if __name__ == "__main__":

    predictor = PredictiveHiring()

    result = predictor.predict(
        candidate_id="AI001",
        metrics={
            "communication": 82,
            "technical": 88,
            "confidence": 78,
            "emotion": 75,
            "video": 85,
        },
    )

    print()

    print("PREDICTIVE HIRING RESULT")

    print()

    print(result)
