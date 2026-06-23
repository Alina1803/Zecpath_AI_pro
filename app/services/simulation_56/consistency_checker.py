class ConsistencyChecker:

    @staticmethod
    def check(scores):

        issues = []

        if scores["ats"] > 85 and scores["technical"] < 50:
            issues.append("High ATS but poor technical performance")

        if scores["technical"] > 90 and scores["hr"] < 50:
            issues.append("Strong technical but weak HR")

        if scores["behavior_risk"] == "High" and scores["final_score"] > 80:
            issues.append("High risk candidate recommended")

        return issues
