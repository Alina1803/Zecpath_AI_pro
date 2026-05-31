from app.services.hiring_report_generator_53.hiring_report_pipeline import (
    HiringReportPipeline
)


def test_report_pipeline():

    sample_data = {

        "candidate_id": "C101",

        "technical_score": 82,

        "coding_score": 80,

        "communication_score": 75,

        "confidence_score": 78,

        "system_design_score": 74,

        "integrity_score": 72,

        "experience": 3,

        "role": "Python Developer",

        "responses": [],

        "communication": {},

        "behavior": {}
    }

    result = HiringReportPipeline().generate(
        sample_data
    )

    assert "overall_report" in result

    assert "technical_evaluation" in result

    assert "formatted_summary" in result

    print("Day 53 Test Passed")