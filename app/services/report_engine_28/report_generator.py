class ReportGenerator:
    """
    Generates recruiter-ready screening reports
    from combined technical + behavioral evaluation data.
    """

    # -------------------------------
    # CONFIDENCE BAND
    # -------------------------------
    def _band(self, score):
        if score >= 8:
            return "High"
        elif score >= 5:
            return "Medium"
        return "Low"

    # -------------------------------
    # HIRING RECOMMENDATION
    # -------------------------------
    def _recommendation(self, score):
        if score >= 7:
            return "Strong Hire"
        elif score >= 5:
            return "Hold"
        return "Reject"

    # -------------------------------
    # STRENGTH EXTRACTION
    # -------------------------------
    def _extract_strengths(self, data):
        strengths = []

        if data.get("semantic_score", 0) > 7:
            strengths.append("Strong conceptual understanding")

        if data.get("communication_strength", 0) > 6:
            strengths.append("Good communication")

        if data.get("domain_score", 0) > 6:
            strengths.append("Good domain knowledge")

        return strengths

    # -------------------------------
    # GAP IDENTIFICATION
    # -------------------------------
    def _extract_gaps(self, data):
        gaps = []

        if data.get("domain_score", 0) < 5:
            gaps.append("Weak domain knowledge")

        if data.get("semantic_score", 0) < 5:
            gaps.append("Poor conceptual clarity")

        if data.get("communication_strength", 0) < 5:
            gaps.append("Weak communication")

        return gaps

    # -------------------------------
    # RISK ANALYSIS
    # -------------------------------
    def _generate_risks(self, data):
        risks = []

        if data.get("domain_score", 0) < 4:
            risks.append("High training requirement")

        if data.get("behavioral_confidence", 0) < 4:
            risks.append("Communication risk")

        if data.get("flags"):
            risks.append("Behavioral inconsistencies detected")

        return risks

    # -------------------------------
    # MISSING DATA CHECK
    # -------------------------------
    def _missing_data(self, data):
        missing = []

        if not data.get("salary_expectation"):
            missing.append("Salary expectation not provided")

        if not data.get("experience"):
            missing.append("Experience not mentioned")

        return missing

    # -------------------------------
    # OPTIONAL HIGHLIGHTS
    # -------------------------------
    def _extract_highlights(self, data):
        highlights = []

        if data.get("semantic_score", 0) > 7:
            highlights.append("Strong understanding of core concepts")

        if data.get("communication_strength", 0) > 6:
            highlights.append("Communicates ideas clearly")

        if data.get("behavioral_confidence", 0) > 6:
            highlights.append("Confident and stable responses")

        return highlights

    # -------------------------------
    # MAIN REPORT GENERATOR
    # -------------------------------
    def generate(self, combined_results):
        tech = combined_results.get("technical_confidence", 0)
        beh = combined_results.get("behavioral_confidence", 0)
        overall = combined_results.get("overall_confidence", 0)

        return {
            "candidate_id": combined_results.get("candidate_id", "UNKNOWN"),

            # -------------------------------
            # OVERALL SUMMARY
            # -------------------------------
            "overall_summary": {
                "final_score": combined_results.get("final_score", 0),
                "overall_confidence": overall,
                "confidence_band": self._band(overall),
                "recommendation": self._recommendation(overall)
            },

            # -------------------------------
            # TECHNICAL EVALUATION
            # -------------------------------
            "technical_evaluation": {
                "technical_confidence": tech,
                "semantic_score": combined_results.get("semantic_score", 0),
                "domain_score": combined_results.get("domain_score", 0),
                "key_strengths": self._extract_strengths(combined_results),
                "gaps": self._extract_gaps(combined_results)
            },

            # -------------------------------
            # BEHAVIORAL EVALUATION
            # -------------------------------
            "behavioral_evaluation": {
                "behavioral_confidence": beh,
                "communication_strength": combined_results.get("communication_strength", 0),
                "sentiment_score": combined_results.get("sentiment_score", 0),
                "risk_flags": combined_results.get("flags", [])
            },

            # -------------------------------
            # INSIGHTS
            # -------------------------------
            "highlights": self._extract_highlights(combined_results),
            "risks": self._generate_risks(combined_results),
            "missing_data": self._missing_data(combined_results)
        }