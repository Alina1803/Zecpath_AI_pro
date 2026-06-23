from app.services.hiring_report_generator_53.recruiter_formatter import (
    RecruiterFormatter,
)


class FinalReportBuilder:

    def build(self, results):

        technical = results.get("technical_report", {})

        hr = results.get("hr_summary", {})

        formatted_summary = RecruiterFormatter().format(results)

        return {
            "candidate_id": results.get("candidate_id"),
            # =====================================
            # OVERALL REPORT
            # =====================================
            "overall_report": {
                "recommendation": technical.get("recommendation"),
                "decision": technical.get("decision"),
                "confidence_score": results.get("confidence_score"),
                "integrity_risk": results.get("integrity_risk"),
            },
            # =====================================
            # TECHNICAL REPORT
            # =====================================
            "technical_evaluation": {
                "final_score": technical.get("final_score"),
                "strengths": technical.get("strengths"),
                "weaknesses": technical.get("weaknesses"),
                "risks": technical.get("risks"),
            },
            # =====================================
            # HR REPORT
            # =====================================
            "hr_evaluation": hr,
            # =====================================
            # RECRUITER SUMMARY
            # =====================================
            "formatted_summary": formatted_summary,
        }
