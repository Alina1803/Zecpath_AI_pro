class FalsePositiveAnalyzer:

    def analyze(self, score, communication, integrity):

        if score > 85 and communication < 40:

            return {
                "flag": "False Positive Risk",
                "reason": "High technical score but poor communication",
            }

        if integrity == "High Risk":

            return {"flag": "Integrity Concern"}

        return {"flag": "Safe"}
