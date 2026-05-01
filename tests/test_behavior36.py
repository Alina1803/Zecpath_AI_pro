from app.services.stress_conf_analyzer36.run_analyzer import analyze_behavior

def test_high_confidence():
    result = analyze_behavior("I am confident and strong", 5)
    assert result["behavioral_score"] > 60

def test_low_confidence():
    result = analyze_behavior("um I think maybe I am not sure", 5)
    assert result["behavioral_score"] < 50

def test_contradiction():
    result = analyze_behavior("I am confident but I am not confident", 5)
    assert result["contradiction"] == 100