class RecruiterFormatter:

    def format(self, report):

        technical = report.get("technical_report", {})

        confidence = report.get("confidence_score", 0)

        integrity = report.get("integrity_risk", "Unknown")

        recommendation = technical.get("recommendation", "Unknown")

        decision = technical.get("decision", "Unknown")

        strengths = technical.get("strengths", [])

        weaknesses = technical.get("weaknesses", [])

        risks = technical.get("risks", [])

        return {
            "summary": {
                "recommendation": recommendation,
                "decision": decision,
                "confidence": confidence,
                "integrity": integrity,
            },
            "strengths": strengths,
            "weaknesses": weaknesses,
            "risks": risks,
        }
