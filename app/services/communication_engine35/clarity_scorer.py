class ClarityScorer:

    CONNECTORS = ["because", "therefore", "however", "for example", "thus"]

    def evaluate(self, text: str) -> float:
        text_lower = text.lower()

        hits = sum(1 for c in self.CONNECTORS if c in text_lower)

        if hits >= 2:
            return 90
        elif hits == 1:
            return 75
        return 60