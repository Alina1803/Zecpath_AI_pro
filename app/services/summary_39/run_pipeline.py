import os
import json
from datetime import datetime

from app.services.summary_39.summary_generator import generate_interview_summary

OUTPUT_DIR = os.path.join("data", "processed", "output_39")
DATASET_FILE = os.path.join("app","services","summary_39", "sample_reports.json")

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def ensure_dataset_file():
    os.makedirs(os.path.dirname(DATASET_FILE), exist_ok=True)

    if not os.path.exists(DATASET_FILE):
        with open(DATASET_FILE, "w") as f:
            json.dump([], f)


def save_result(result: dict):
    ensure_output_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"interview_summary_{timestamp}.json"

    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w") as f:
        json.dump(result, f, indent=4)

    return filepath


def append_to_dataset(new_result: dict):
    ensure_dataset_file()

    try:
        with open(DATASET_FILE, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        data = []

    data.append(new_result)

    with open(DATASET_FILE, "w") as f:
        json.dump(data, f, indent=4)


def run_pipeline39(candidate_id, hr_scores, communication, behavior, answers, save_output=True):
    """
    Full Interview Summary Pipeline (Day 39)
    """

    try:
        # Step 1: Generate summary
        result = generate_interview_summary(
            candidate_id=candidate_id,
            hr_scores=hr_scores,
            communication=communication,
            behavior=behavior,
            answers=answers
        )

        # Step 2: Add timestamp
        result["timestamp"] = datetime.now().isoformat()

        # Step 3: Save + Aggregate
        if save_output:
            filepath = save_result(result)
            result["saved_to"] = filepath

            # ✅ Append to dataset
            append_to_dataset(result)

        return result

    except Exception as e:
        return {
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }


# ===============================
# ▶️ EXECUTION ENTRY
# ===============================
def run():
    print("\n Starting Interview Summary Pipeline (Day 39)...\n")

    # 🔹 Sample Input
    candidate_id = "C500"

    hr_scores = [
        {"question_id": "Q1", "final_score": 85},
        {"question_id": "Q2", "final_score": 60}
    ]

    communication = {
        "communication_score": 78
    }

    behavior = {
        "confidence": {"confidence_score": 65},
        "behavioral_score": 70,
        "contradiction": False
    }

    answers = ["I worked in a team project"]

    # 🔹 Run pipeline
    result = run_pipeline39(
        candidate_id=candidate_id,
        hr_scores=hr_scores,
        communication=communication,
        behavior=behavior,
        answers=answers,
        save_output=True
    )

    # 🔹 Print result
    print("=== Interview Summary Result ===")
    print(json.dumps(result, indent=4))

    print("\n Pipeline execution completed.\n")


# ===============================
# 🧪 MAIN
# ===============================
if __name__ == "__main__":
    run()