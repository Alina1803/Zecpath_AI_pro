from app.services.parsers.resume_parser import (
    parse_resume,
)

from app.services.ats_scoring import (
    calculate_ats_score,
)

from app.services.cross_round_ai_51.decision_engine import (
    hiring_decision,
)


def full_integration_pipeline(data):

    parsed = parse_resume(data["resume"])

    ats = calculate_ats_score(
        parsed,
        data["job_requirements"],
    )

    final_score = ats["final_ats_score"]

    decision = hiring_decision(final_score)

    return {
        "status": "success",
        "candidate_id": data["candidate_id"],
        "resume_score": 80,
        "ats_score": ats["final_ats_score"],
        "screening_score": 78,
        "interview_score": 82,
        "final_score": final_score,
        "decision": decision,
    }


if __name__ == "__main__":

    print(
        full_integration_pipeline(
            {
                "candidate_id": "AI001",
                "resume": "resume.pdf",
                "job_requirements": {
                    "required_skills": ["python"],
                    "min_experience_years": 2,
                },
            }
        )
    )
