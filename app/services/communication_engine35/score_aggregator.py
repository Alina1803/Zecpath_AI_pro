class ScoreAggregator:

    WEIGHTS = {
        "fluency": 0.2,
        "grammar": 0.25,
        "vocabulary": 0.15,
        "clarity": 0.15,
        "filler": 0.15,
        "structure": 0.10
    }

    def aggregate(self, scores: dict) -> float:
        total = 0

        for key, value in scores.items():
            total += value * self.WEIGHTS.get(key, 0)

        return round(total, 2)