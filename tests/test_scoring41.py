from app.services.unified_scoring_engine_41.unified_scoring_engine import calculate_unified_score

def test_score():
    score = calculate_unified_score(80, 70, 90, {
        "ats": 0.3,
        "screening": 0.3,
        "hr": 0.4
    })
    assert score > 0