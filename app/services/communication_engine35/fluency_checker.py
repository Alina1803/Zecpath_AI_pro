import re

class FluencyChecker:

    def evaluate(self, text: str) -> float:
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if not sentences:
            return 0.0

        lengths = [len(s.split()) for s in sentences]
        avg_len = sum(lengths) / len(lengths)

        # Ideal sentence length range: 10–20 words
        if 10 <= avg_len <= 20:
            score = 90
        elif 7 <= avg_len < 10 or 20 < avg_len <= 25:
            score = 75
        else:
            score = 55

        return score