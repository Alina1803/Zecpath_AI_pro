from app.pipeline.integration_pipeline import full_integration_pipeline


def test_pipeline():

    result = full_integration_pipeline(
        {
            "candidate_id": "AI001",
            "resume": "resume.pdf",
            "job_requirements": {
                "required_skills": ["python"],
                "min_experience_years": 2,
            },
        }
    )

    assert result["decision"] in [
        "Hire",
        "Consider",
        "Reject",
    ]
