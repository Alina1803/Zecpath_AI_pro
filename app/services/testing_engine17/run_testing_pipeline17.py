import os
import json

from app.services.testing_engine17.test_dataset_loader import load_test_candidates
from app.services.testing_engine17.prediction_validator import validate_prediction
from app.services.testing_engine17.metrics_engine import calculate_accuracy
from app.services.testing_engine17.mismatch_tracker import find_mismatches
from app.services.testing_engine17.improvement_backlog import generate_backlog


INPUT_FOLDER = "data/test_cases"
OUTPUT_FILE = "data/processed/output_17/testing_report.json"


def save_output(data):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def main():
    candidates = load_test_candidates(INPUT_FOLDER)

    validation_results = []

    for candidate in candidates:
        expected = candidate.get("expected_decision", "REVIEW")

        result = validate_prediction(candidate, expected)
        validation_results.append(result)

    accuracy = calculate_accuracy(validation_results)
    mismatches = find_mismatches(validation_results)
    backlog = generate_backlog(mismatches)

    final_output = {
        "accuracy": accuracy,
        "total_test_cases": len(validation_results),
        "mismatches": mismatches,
        "improvement_backlog": backlog
    }

    save_output(final_output)

    print("Day 17 ATS testing completed successfully.")


if __name__ == "__main__":
    main()