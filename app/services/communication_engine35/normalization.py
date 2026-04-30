class Normalizer:

    def normalize(self, score: float) -> float:
        return round(min(max(score, 0), 100), 2)