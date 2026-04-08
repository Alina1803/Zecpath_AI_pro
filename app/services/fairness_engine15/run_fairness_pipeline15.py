import os
import json

from app.services.fairness_engine15.resume_normalizer import normalize_candidate
from app.services.fairness_engine15.score_normalizer import normalize_scores
from app.services.fairness_engine15.bias_masking import mask_sensitive_fields
from app.services.fairness_engine15.fairness_audit import generate_fairness_report


INPUT_FILE = "data/processed/output_14/ranked_candidates.json"
OUTPUT_FILE = "data/processed/output_15/fair_candidates.json"


def load_candidates():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data["ranked_candidates"]


def save_output(data):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def main():
    candidates = load_candidates()

    candidates = [normalize_candidate(c) for c in candidates]
    candidates = [mask_sensitive_fields(c) for c in candidates]
    candidates = normalize_scores(candidates)

    fairness_report = generate_fairness_report(candidates)

    final_output = {
        "fairness_report": fairness_report,
        "fair_candidates": candidates
    }

    save_output(final_output)

    print("Day 15 fairness pipeline completed successfully.")


if __name__ == "__main__":
    main()