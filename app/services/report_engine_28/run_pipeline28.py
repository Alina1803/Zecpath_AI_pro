import json
import os
from datetime import datetime

from app.services.report_engine_28.report_generator import ReportGenerator


def run_pipeline():
    # -------------------------------
    # LOAD DAY 27 OUTPUT (AUTO PICK FILE)
    # -------------------------------
    folder_path = "data/processed/output_27"

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f" Folder not found: {folder_path}")

    files = [f for f in os.listdir(folder_path) if f.endswith(".json")]

    if not files:
        raise FileNotFoundError(" No JSON files found in output_27 folder")

    # Pick latest file
    files.sort(reverse=True)
    input_file = files[0]

    input_path = os.path.join(folder_path, input_file)

    print(f" Using input file: {input_path}")

    with open(input_path, "r") as f:
        data = json.load(f)

    records = data.get("results", [])

    # -------------------------------
    # LOAD OPTIONAL DATASET (ENRICHMENT)
    # -------------------------------
    dataset_path = "data/dataset28.json"
    dataset_map = {}

    if os.path.exists(dataset_path):
        print(f" Loading dataset: {dataset_path}")

        with open(dataset_path, "r") as f:
            dataset = json.load(f)

        dataset_map = {
            item.get("candidate_id"): item
            for item in dataset
        }

    # -------------------------------
    # INIT REPORT GENERATOR
    # -------------------------------
    report_generator = ReportGenerator()

    final_reports = []
    processed = 0
    failed = 0

    # -------------------------------
    # PROCESS EACH RECORD
    # -------------------------------
    for rec in records:
        try:
            tech_conf = rec.get("technical_confidence", 0)
            beh_conf = rec.get("behavioral_confidence", 0)

            # Overall confidence
            overall_conf = round((tech_conf + beh_conf) / 2, 2)

            # Merge dataset info
            extra = dataset_map.get(rec.get("candidate_id"), {})

            combined = {
                **rec,
                **extra,
                "overall_confidence": overall_conf
            }

            # Generate report
            report = report_generator.generate(combined)

            final_reports.append(report)
            processed += 1

        except Exception as e:
            failed += 1
            final_reports.append({
                "candidate_id": rec.get("candidate_id", "UNKNOWN"),
                "status": "failed",
                "error": str(e)
            })

    # -------------------------------
    # META INFO
    # -------------------------------
    meta = {
        "run_id": f"RUN_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "run_time": datetime.now().isoformat(),
        "total_candidates": len(records),
        "processed": processed,
        "failed": failed,
        "engine_version": "v3.0",
        "stage": "Day28_Report_Generation"
    }

    # -------------------------------
    # FINAL OUTPUT
    # -------------------------------
    output = {
        "meta": meta,
        "reports": final_reports
    }

    # -------------------------------
    # SAVE OUTPUT (FIXED )
    # -------------------------------
    output_dir = "data/processed/output_28"

    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "output_28.json")

    with open(output_path, "w") as f:
        json.dump(output, f, indent=4)

    print("\n PIPELINE COMPLETED")
    print(f" Output saved to: {output_path}")
    print(f" Processed: {processed} |  Failed: {failed}")


# -------------------------------
# ENTRY POINT
# -------------------------------
if __name__ == "__main__":
    run_pipeline()