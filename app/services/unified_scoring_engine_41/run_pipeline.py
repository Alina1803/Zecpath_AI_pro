import json
import os
from datetime import datetime
from app.services.unified_scoring_engine_41.pipeline.unified_pipeline import unified_pipeline

INPUT_FILE = "data/sample_candidates41.json"
OUTPUT_DIR = "data/processed"

def load_candidates(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f" Error loading input file: {e}")
        return []

def process_candidates(candidates):
    results = []
    errors = []

    for idx, c in enumerate(candidates):
        try:
            result = unified_pipeline(
                candidate_id=c.get("candidate_id", f"UNKNOWN_{idx}"),
                ats=c.get("ats", 0),
                screening=c.get("screening", 0),
                hr=c.get("hr", 0),
                role=c.get("role", "fresher")
            )
            results.append(result)

        except Exception as e:
            errors.append({
                "candidate": c,
                "error": str(e)
            })

    return results, errors

def save_output(results):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(OUTPUT_DIR, f"output_41_{timestamp}.json")

    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    return output_file

if __name__ == "__main__":

    print("\n Starting Unified Scoring Batch Process...\n")

    candidates = load_candidates(INPUT_FILE)

    if not candidates:
        print(" No candidates found. Exiting.")
        exit()

    results, errors = process_candidates(candidates)

    output_path = save_output(results)

    print(f"\n Successfully processed: {len(results)} candidates")
    
    if errors:
        print(f" Failed records: {len(errors)}")

    print(f" Output saved to: {output_path}")