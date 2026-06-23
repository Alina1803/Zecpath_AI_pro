from app.services.technical_interview_engine_46.engines.recommendation_engine import (
    RecommendationEngine,
)


class ScoringEngine:

    def __init__(self):

        self.recommendation_engine = RecommendationEngine()

    def calculate(self, evaluation_data):

        # =====================================
        # FETCH SCORES
        # =====================================

        technical_score = evaluation_data.get("technical_score", 0)

        coding_score = evaluation_data.get("coding_score", 0)

        communication_score = evaluation_data.get("communication_score", 0)

        confidence_score = evaluation_data.get("confidence_score", 0)

        system_design_score = evaluation_data.get("system_design_score", 0)

        semantic_score = evaluation_data.get("semantic_score", 0)

        domain_score = evaluation_data.get("domain_score", 0)

        experience_level = evaluation_data.get("experience_level", "junior")

        # =====================================
        # EXPERIENCE WEIGHTING
        # =====================================

        if experience_level == "junior":

            weights = {
                "technical": 0.30,
                "coding": 0.30,
                "communication": 0.15,
                "confidence": 0.10,
                "system_design": 0.05,
                "semantic": 0.05,
                "domain": 0.05,
            }

        elif experience_level == "mid":

            weights = {
                "technical": 0.30,
                "coding": 0.25,
                "communication": 0.15,
                "confidence": 0.10,
                "system_design": 0.10,
                "semantic": 0.05,
                "domain": 0.05,
            }

        else:

            weights = {
                "technical": 0.25,
                "coding": 0.20,
                "communication": 0.15,
                "confidence": 0.10,
                "system_design": 0.20,
                "semantic": 0.05,
                "domain": 0.05,
            }

        # =====================================
        # FINAL WEIGHTED SCORE
        # =====================================

        final_score = round(
            (
                technical_score * weights["technical"]
                + coding_score * weights["coding"]
                + communication_score * weights["communication"]
                + confidence_score * weights["confidence"]
                + system_design_score * weights["system_design"]
                + semantic_score * weights["semantic"]
                + domain_score * weights["domain"]
            ),
            2,
        )

        # =====================================
        # PERFORMANCE CATEGORY
        # =====================================

        if final_score >= 85:

            performance = "Excellent"

        elif final_score >= 70:

            performance = "Good"

        elif final_score >= 55:

            performance = "Average"

        else:

            performance = "Poor"

        # =====================================
        # RECOMMENDATION ENGINE
        # =====================================

        recommendation_result = self.recommendation_engine.generate(
            {
                "technical_score": technical_score,
                "coding_score": coding_score,
                "communication_score": communication_score,
                "confidence_score": confidence_score,
                "system_design_score": system_design_score,
                "experience_level": experience_level,
            }
        )

        # =====================================
        # FINAL OUTPUT
        # =====================================

        return {
            "technical_score": technical_score,
            "coding_score": coding_score,
            "communication_score": communication_score,
            "confidence_score": confidence_score,
            "system_design_score": system_design_score,
            "semantic_score": semantic_score,
            "domain_score": domain_score,
            "experience_level": experience_level,
            "final_score": final_score,
            "performance": performance,
            "recommendation": recommendation_result["recommendation"],
            "decision": recommendation_result["decision"],
            "strengths": recommendation_result["strengths"],
            "weaknesses": recommendation_result["weaknesses"],
            "risks": recommendation_result["risks"],
        }
