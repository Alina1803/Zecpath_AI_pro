class RecommendationEngine:

    @staticmethod
    def generate(report_data):

        technical_score = report_data.get(
            "technical_score",
            0
        )

        communication_score = report_data.get(
            "communication_score",
            0
        )

        confidence_score = report_data.get(
            "confidence_score",
            0
        )

        coding_score = report_data.get(
            "coding_score",
            0
        )

        system_design_score = report_data.get(
            "system_design_score",
            0
        )

        experience_level = report_data.get(
            "experience_level",
            "junior"
        )

        # =====================================
        # FINAL WEIGHTED SCORE
        # =====================================

        final_score = round(

            (
                technical_score * 0.35 +

                coding_score * 0.25 +

                communication_score * 0.15 +

                confidence_score * 0.10 +

                system_design_score * 0.15
            ),

            2
        )

        # =====================================
        # RECOMMENDATION LOGIC
        # =====================================

        if (
            final_score >= 85 and
            technical_score >= 80 and
            coding_score >= 75
        ):

            recommendation = "Strong Hire"

        elif (
            final_score >= 70 and
            technical_score >= 65
        ):

            recommendation = "Hire"

        elif final_score >= 55:

            recommendation = "Consider"

        else:

            recommendation = "Reject"

        # =====================================
        # STRENGTH ANALYSIS
        # =====================================

        strengths = []

        if technical_score >= 80:
            strengths.append(
                "Strong technical fundamentals"
            )

        if coding_score >= 75:
            strengths.append(
                "Good coding ability"
            )

        if communication_score >= 75:
            strengths.append(
                "Strong communication"
            )

        if confidence_score >= 75:
            strengths.append(
                "Confident problem solving"
            )

        if system_design_score >= 75:
            strengths.append(
                "Good architecture understanding"
            )

        # =====================================
        # WEAKNESS ANALYSIS
        # =====================================

        weaknesses = []

        if technical_score < 60:
            weaknesses.append(
                "Weak technical depth"
            )

        if coding_score < 60:
            weaknesses.append(
                "Coding performance needs improvement"
            )

        if communication_score < 60:
            weaknesses.append(
                "Communication clarity is low"
            )

        if confidence_score < 60:
            weaknesses.append(
                "Low confidence during interview"
            )

        if system_design_score < 60:
            weaknesses.append(
                "Limited system design knowledge"
            )

        # =====================================
        # RISK DETECTION
        # =====================================

        risks = []

        if (
            technical_score > 80 and
            communication_score < 50
        ):

            risks.append(
                "Strong technical skill but poor communication"
            )

        if (
            confidence_score < 40 and
            experience_level == "senior"
        ):

            risks.append(
                "Confidence level lower than expected for senior candidate"
            )

        # =====================================
        # FINAL DECISION
        # =====================================

        if recommendation == "Strong Hire":

            decision = "Proceed to Final Round"

        elif recommendation == "Hire":

            decision = "Shortlist for Next Round"

        elif recommendation == "Consider":

            decision = "Hold for Review"

        else:

            decision = "Reject Application"

        # =====================================
        # FINAL OUTPUT
        # =====================================

        return {

            "final_score": final_score,

            "recommendation": recommendation,

            "decision": decision,

            "strengths": strengths,

            "weaknesses": weaknesses,

            "risks": risks
        }