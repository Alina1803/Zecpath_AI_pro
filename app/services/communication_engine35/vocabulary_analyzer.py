class VocabularyAnalyzer:

    def evaluate(self, text: str) -> float:
        words = text.lower().split()
        if not words:
            return 0.0

        unique_words = set(words)
        diversity = len(unique_words) / len(words)

        score = min(diversity * 120, 100)  # boost factor

        return round(score, 2)