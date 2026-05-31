from app.services.report_engine_28.report_generator import (ReportGenerator)

from app.services.summary_39.summary_generator import (generate_interview_summary)

from app.services.integrity_engine_49.risk_engine import (risk_flagging)

from app.services.technical_interview_engine_46.engines.recommendation_engine import (RecommendationEngine)

from app.services.recommendation_ai_52.confidence_engine import (
    calculate_confidence
)


class HiringReportPipeline:

    def generate(self, candidate_data):

        # =====================================
        # TECHNICAL RECOMMENDATION
        # =====================================

        technical_report = RecommendationEngine.generate(
            candidate_data
        )

        # =====================================
        # HR SUMMARY
        # =====================================

        hr_summary = generate_interview_summary(
            candidate_id=candidate_data.get("candidate_id"),
            role=candidate_data.get("role"),
            experience=candidate_data.get("experience"),
            responses=candidate_data.get("responses"),
            communication=candidate_data.get("communication"),
            behavior=candidate_data.get("behavior")
        )

        # =====================================
        # RISK ANALYSIS
        # =====================================

        integrity_risk = risk_flagging(
            candidate_data.get(
                "integrity_score",
                0
            )
        )

        # =====================================
        # CONFIDENCE SCORE
        # =====================================

        confidence = calculate_confidence([
            candidate_data.get("technical_score", 0),
            candidate_data.get("coding_score", 0),
            candidate_data.get("communication_score", 0),
            candidate_data.get("confidence_score", 0)
        ])

        # =====================================
        # FINAL REPORT ENGINE
        # =====================================

        combined_results = {

            "candidate_id":
                candidate_data.get("candidate_id"),

            "technical_confidence":
                candidate_data.get("technical_score"),

            "behavioral_confidence":
                candidate_data.get("confidence_score"),

            "overall_confidence":
                confidence / 10,

            "semantic_score":
                candidate_data.get("technical_score"),

            "domain_score":
                candidate_data.get("system_design_score"),

            "communication_strength":
                candidate_data.get("communication_score"),

            "sentiment_score":
                candidate_data.get("sentiment_score"),

            "flags":
                technical_report.get("risks"),

            "experience":
                candidate_data.get("experience"),

            "salary_expectation":
                candidate_data.get("salary_expectation"),

            "final_score":
                technical_report.get("final_score")
        }

        final_report = ReportGenerator().generate(
            combined_results
        )

        # =====================================
        # MASTER OUTPUT
        # =====================================

        return {

            "candidate_id":
                candidate_data.get("candidate_id"),

            "technical_report":
                technical_report,

            "hr_summary":
                hr_summary,

            "integrity_risk":
                integrity_risk,

            "confidence_score":
                confidence,

            "final_report":
                final_report
        }
