class FillerDetector:

    FILLERS = ["um", "uh", "like", "you know", "basically", "actually"]

    def evaluate(self, text: str) -> float:
        text_lower = text.lower()

        count = sum(text_lower.count(f) for f in self.FILLERS)
        word_count = max(len(text.split()), 1)

        ratio = count / word_count

        if ratio == 0:
            return 100
        elif ratio < 0.03:
            return 80
        elif ratio < 0.07:
            return 60
        return 40