import os
import json
from datetime import datetime

from app.services.aptitude_logic_38.aptitude_scoring import calculate_aptitude_score
from app.services.aptitude_logic_38.scenario_evaluator import evaluate_scenario


OUTPUT_DIR = os.path.join("data", "processed", "output_38")


def ensure_output_dir():
    """Create output directory if not exists"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_result(result: dict):
    """Save result as JSON file with timestamp"""
    ensure_output_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"aptitude_score_{timestamp}.json"

    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w") as f:
        json.dump(result, f, indent=4)

    return filepath


def run_pipeline(answer: str, scenario_type: str = None, save_output: bool = True):
    """
    Full aptitude evaluation pipeline
    """

    try:
        # Step 1: Base scoring
        score = calculate_aptitude_score(answer)

        # Step 2: Scenario evaluation
        scenario_score = None
        if scenario_type:
            scenario_score = evaluate_scenario(answer, scenario_type)

        # Step 3: Final score calculation
        final_score = score["aptitude_score"]

        if scenario_score is not None:
            final_score = (final_score * 0.7) + (scenario_score * 100 * 0.3)

        # Step 4: Build result
        result = {
            "timestamp": datetime.now().isoformat(),
            "input": {
                "answer": answer,
                "scenario_type": scenario_type
            },
            "aptitude_score": round(final_score, 2),
            "details": score["breakdown"],
            "scenario_score": scenario_score
        }

        # Step 5: Save output
        if save_output:
            filepath = save_result(result)
            result["saved_to"] = filepath

        return result

    except Exception as e:
        return {
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }


# ===============================
# ▶️ EXECUTION ENTRY POINT
# ===============================
def run():
    print("\n Starting Aptitude Pipeline...\n")

    # Sample input
    text = "First I analyze the problem, then I plan a solution and finally execute it"

    # Run pipeline
    result = run_pipeline(
        answer=text,
        scenario_type="deadline_pressure",  # try: team_conflict / learning
        save_output=True
    )

    # Print result
    print("=== Aptitude Pipeline Result ===")
    print(json.dumps(result, indent=4))

    print("\n Pipeline execution completed.\n")


# ===============================
# 🧪 MAIN
# ===============================
if __name__ == "__main__":
    run()