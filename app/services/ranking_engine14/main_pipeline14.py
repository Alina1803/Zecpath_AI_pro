import os
import json

from app.services.ranking_engine14.rank_candidates import rank_candidates
from app.services.ranking_engine14.shortlist_engine import apply_shortlisting
from app.services.ranking_engine14.recruiter_summary import generate_summary


INPUT_FOLDER = "data/processed/output_13"
OUTPUT_FILE = "data/processed/output_14/ranked_candidates.json"


def load_candidates():
    """
    Load all candidate JSON files from Day 13 output.
    """
    candidates = []

    if not os.path.exists(INPUT_FOLDER):
        print(f"Input folder not found: {INPUT_FOLDER}")
        return candidates

    for file_name in os.listdir(INPUT_FOLDER):
        if file_name.endswith(".json"):
            file_path = os.path.join(INPUT_FOLDER, file_name)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                    # Keep traceability
                    data["file_name"] = file_name

                    candidates.append(data)

            except Exception as e:
                print(f"Error loading {file_name}: {e}")

    return candidates


def save_output(final_output):
    """
    Save ranked candidate output.
    """
    output_folder = os.path.dirname(OUTPUT_FILE)
    os.makedirs(output_folder, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(final_output, f, indent=4)

    print(f"Saved ranking output to: {OUTPUT_FILE}")


def main():
    candidates = load_candidates()

    if not candidates:
        print("No candidates found.")
        return

    ranked = rank_candidates(candidates)
    shortlisted = apply_shortlisting(ranked)
    summary = generate_summary(shortlisted)

    final_output = {
        "summary": summary,
        "ranked_candidates": shortlisted
    }

    save_output(final_output)

    print("Day 14 ranking completed successfully.")


if __name__ == "__main__":
    main()