from app.services.optimization_stability42.interview_ai.stable_hr_ai import stable_hr_evaluation

def test_stability():
    result = stable_hr_evaluation([50, 60, 90, 30])
    assert result["stable_score"] > 0
    assert result["decision"] in ["Hire", "Consider", "Reject"]