class ConsistencyEngine:

    def evaluate(self, ats, technical, hr):

        scores = [ats, technical, hr]

        gap = max(scores) - min(scores)

        adjustment = 0

        if gap > 40:
            adjustment = -10

        elif gap > 25:
            adjustment = -5

        final_score = round(
            sum(scores) / len(scores) + adjustment,
            2
        )

        return {

            "scores": {
                "ats": ats,
                "technical": technical,
                "hr": hr
            },

            "adjustment": adjustment,

            "final_score": final_score
        }