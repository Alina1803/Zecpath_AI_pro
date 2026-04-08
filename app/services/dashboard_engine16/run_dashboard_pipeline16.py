import json
import os

from app.services.dashboard_engine16.dashboard_data import prepare_dashboard_rows
from app.services.dashboard_engine16.explainability_engine import explain_candidate
from app.services.dashboard_engine16.fairness_dashboard import fairness_metrics


INPUT_FILE = "data/processed/output_15/fair_candidates.json"
OUTPUT_FILE = "data/processed/output_16/dashboard_data.json"


def load_candidates():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data["fair_candidates"]


def save_output(data):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def main():
    candidates = load_candidates()

    dashboard_rows = prepare_dashboard_rows(candidates)
    fairness = fairness_metrics(candidates)

    explainability = [
        explain_candidate(c)
        for c in candidates[:5]
    ]

    final_output = {
        "dashboard_rows": dashboard_rows,
        "fairness_metrics": fairness,
        "top_5_explanations": explainability
    }

    save_output(final_output)

    print("Day 16 dashboard pipeline completed successfully.")


if __name__ == "__main__":
    main()