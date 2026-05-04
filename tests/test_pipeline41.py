from app.services.unified_scoring_engine_41.pipeline.unified_pipeline import unified_pipeline

def test_pipeline():
    result = unified_pipeline("C1", 80, 70, 85)
    assert "final_score" in result
    assert result["decision"] in ["Hire", "Consider", "Reject"]