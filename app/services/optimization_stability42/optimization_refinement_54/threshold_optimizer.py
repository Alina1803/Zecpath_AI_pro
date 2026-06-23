class ThresholdOptimizer:

    def optimize(self, score, integrity_risk):

        if integrity_risk == "High Risk":

            if score >= 80:
                return {
                    "decision": "Hold / Review",
                    "reason": "High integrity risk detected",
                }

        if score >= 85:
            return {"decision": "Strong Hire"}

        elif score >= 70:
            return {"decision": "Hire"}

        elif score >= 55:
            return {"decision": "Hold"}

        return {"decision": "Reject"}
