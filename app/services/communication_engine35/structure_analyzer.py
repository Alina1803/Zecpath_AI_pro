import re

class StructureAnalyzer:

    def evaluate(self, text: str) -> float:
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if len(sentences) >= 3:
            return 90
        elif len(sentences) == 2:
            return 75
        return 55