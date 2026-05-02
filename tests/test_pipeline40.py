from tests.hr_simulation40 import run_simulation
from app.services.hr_simulation_40.interview_engine import InterviewManager
from app.services.hr_simulation_40.evaluation.accuracy_metrics import calculate_accuracy
from app.services.hr_simulation_40.evaluation.bias_analysis import analyze_bias


def test_simulation_runs():
    results = run_simulation(10)
    assert len(results) == 10, "Simulation did not return expected number of results"


def test_result_structure():
    results = run_simulation(5)

    for r in results:
        assert "type" in r
        assert "ai_score" in r
        assert "human_score" in r
        assert "decision_ai" in r


def test_score_range():
    results = run_simulation(10)

    for r in results:
        assert 0 <= r["ai_score"] <= 100, "AI score out of range"


def test_accuracy_calculation():
    results = run_simulation(10)
    accuracy = calculate_accuracy(results)

    assert 0 <= accuracy <= 100, "Accuracy out of valid range"


def test_bias_analysis():
    results = run_simulation(10)
    bias = analyze_bias(results)

    assert isinstance(bias, dict), "Bias output should be dictionary"


def test_interview_manager():
    interview = InterviewManager("Confident")
    result = interview.run()

    assert "final_score" in result
    assert "decision" in result
    assert isinstance(result["responses"], list)


def test_decision_logic():
    interview = InterviewManager("Confident")
    result = interview.run()

    decision = result["decision"]

    assert decision in ["Strong Hire", "Consider", "Reject"]


if __name__ == "__main__":
    print("Running tests...\n")

    test_simulation_runs()
    test_result_structure()
    test_score_range()
    test_accuracy_calculation()
    test_bias_analysis()
    test_interview_manager()
    test_decision_logic()

    print("✅ All tests passed successfully!")