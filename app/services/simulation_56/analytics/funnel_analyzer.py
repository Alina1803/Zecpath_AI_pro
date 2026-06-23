class FunnelAnalyzer:

    @staticmethod
    def generate(results):

        total = len(results)

        ats = len([x for x in results if x["ats"] >= 70])

        screening = len([x for x in results if x["screening"] >= 70])

        hr = len([x for x in results if x["hr"] >= 70])

        technical = len([x for x in results if x["technical"] >= 70])

        selected = len([x for x in results if x["decision"] == "Selected"])

        return {
            "applied": total,
            "ats_passed": ats,
            "screening_passed": screening,
            "hr_passed": hr,
            "technical_passed": technical,
            "selected": selected,
        }
