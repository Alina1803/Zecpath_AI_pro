class TechnicalEvaluator:

    TECH_KEYWORDS = [
        "optimization",
        "scalability",
        "performance",
        "database",
        "architecture",
        "complexity",
    ]

    @classmethod
    def evaluate(cls, answer):

        score = 0

        if len(answer.split()) > 15:
            score += 4

        for word in cls.TECH_KEYWORDS:

            if word in answer.lower():
                score += 1

        if score >= 8:
            level = "strong"

        elif score >= 5:
            level = "moderate"

        elif score >= 3:
            level = "vague"

        else:
            level = "weak"

        return {"technical_score": min(score, 10), "quality": level}
