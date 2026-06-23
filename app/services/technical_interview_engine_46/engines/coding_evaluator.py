class CodingEvaluator:

    @staticmethod
    def evaluate(code):

        score = 0

        if "for" in code:
            score += 2

        if "if" in code:
            score += 2

        if "def" in code:
            score += 3

        if "class" in code:
            score += 2

        return min(score, 10)
