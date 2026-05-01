import os
import json

from app.services.aptitude_logic_38.aptitude_scoring import calculate_aptitude_score
from app.services.aptitude_logic_38.scenario_evaluator import evaluate_scenario
from app.services.aptitude_logic_38.run_pipeline import run_pipeline


# ===============================
# 🧪 TEST 1: BASIC SCORING
# ===============================
def test_calculate_aptitude_score():
    text = "First I analyze the problem, then I plan a solution and finally execute it"

    result = calculate_aptitude_score(text)

    assert "aptitude_score" in result
    assert result["aptitude_score"] > 70
    assert result["breakdown"]["structure"] >= 0.7


# ===============================
# 🧪 TEST 2: SCENARIO EVALUATION
# ===============================
def test_scenario_evaluation():
    text = "I prioritize tasks, plan properly and execute efficiently"

    score = evaluate_scenario(text, "deadline_pressure")

    assert score is not None
    assert score >= 0.7


# ===============================
# 🧪 TEST 3: FULL PIPELINE
# ===============================
def test_run_pipeline():
    text = "First I analyze, then plan and execute the solution"

    result = run_pipeline(
        answer=text,
        scenario_type="deadline_pressure",
        save_output=False
    )

    assert "aptitude_score" in result
    assert result["aptitude_score"] > 60
    assert "details" in result


# ===============================
# 🧪 TEST 4: OUTPUT FILE CREATION
# ===============================
def test_output_saved():
    text = "First I analyze, then plan and execute the solution"

    result = run_pipeline(
        answer=text,
        scenario_type="deadline_pressure",
        save_output=True
    )

    assert "saved_to" in result
    assert os.path.exists(result["saved_to"])


# ===============================
# 🧪 TEST 5: EMPTY INPUT (EDGE CASE)
# ===============================
def test_empty_input():
    result = calculate_aptitude_score("")

    assert result["aptitude_score"] >= 0


# ===============================
# 🧪 TEST 6: UNKNOWN SCENARIO
# ===============================
def test_unknown_scenario():
    text = "I will handle the situation carefully"

    score = evaluate_scenario(text, "unknown_type")

    assert score is None or score >= 0


# ===============================
# 🧪 TEST 7: SHORT ANSWER
# ===============================
def test_short_answer():
    text = "I try"

    result = calculate_aptitude_score(text)

    assert result["aptitude_score"] <= 70


# ===============================
# ▶️ RUN TESTS MANUALLY
# ===============================
if __name__ == "__main__":
    print("\n Running Aptitude Tests...\n")

    test_calculate_aptitude_score()
    print(" test_calculate_aptitude_score passed")

    test_scenario_evaluation()
    print(" test_scenario_evaluation passed")

    test_run_pipeline()
    print(" test_run_pipeline passed")

    test_output_saved()
    print(" test_output_saved passed")

    test_empty_input()
    print(" test_empty_input passed")

    test_unknown_scenario()
    print(" test_unknown_scenario passed")

    test_short_answer()
    print(" test_short_answer passed")

    print("\n All tests passed successfully!\n")