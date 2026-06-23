import json
from datetime import datetime


class ReportGenerator:

    @staticmethod
    def generate(candidate_data):

        report = {
            "candidate_id": candidate_data.get("candidate_id"),
            "candidate_name": candidate_data.get("candidate_name"),
            "role": candidate_data.get("role"),
            "experience_level": candidate_data.get("experience_level"),
            "technical_score": candidate_data.get("technical_score"),
            "coding_score": candidate_data.get("coding_score"),
            "communication_score": candidate_data.get("communication_score"),
            "confidence_score": candidate_data.get("confidence_score"),
            "system_design_score": candidate_data.get("system_design_score"),
            "final_score": candidate_data.get("final_score"),
            "recommendation": candidate_data.get("recommendation"),
            "decision": candidate_data.get("decision"),
            "strengths": candidate_data.get("strengths"),
            "weaknesses": candidate_data.get("weaknesses"),
            "risks": candidate_data.get("risks"),
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        print("\n========== TECHNICAL INTERVIEW REPORT ==========\n")

        print(json.dumps(report, indent=4))

        return report
