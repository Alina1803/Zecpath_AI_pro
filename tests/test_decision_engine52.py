from app.services.recommendation_ai_52.decision_engine import generate_decision


def test_selected():
    assert generate_decision(85) == "Selected"


def test_hold():
    assert generate_decision(65) == "Hold / Review"


def test_rejected():
    assert generate_decision(40) == "Rejected"