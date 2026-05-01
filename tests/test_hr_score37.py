from app.services.interview_ai_37.hr_scoring_engine import hr_scoring_pipeline


def test_hr_score():
    result = hr_scoring_pipeline([], "fresher")
    assert "hr_score" in result


def test_valid_candidate():
    answers = [
        {
            "question_id": "Q1",
            "relevance_score": 0.9,
            "communication_score": 85,
            "confidence_score": 80,
            "contradiction": False,
            "is_vague": False
        }
    ]

    result = hr_scoring_pipeline(answers, "experienced")

    assert result["hr_score"] > 0
    assert result["decision"] in ["Strong Hire", "Consider", "Reject"]