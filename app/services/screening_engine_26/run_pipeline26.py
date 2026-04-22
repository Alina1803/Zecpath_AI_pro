import os
import json
from datetime import datetime

from app.services.screening_engine_26.scoring_engine import AdvancedScoringEngine
from app.utils.logger import get_logger
# ==============================
# LOGGER
# =============================
logger = get_logger()
# ==============================
# PATH CONFIG
# ==============================
BASE_DIR = os.getcwd()

DATA_DIR = os.path.join(BASE_DIR, "data")

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "output_26"
)
# ==============================
# LOAD CONFIG FILES
# ==============================
def load_configs():
    try:
        domain_path = os.path.join(DATA_DIR, "ca_domain_knowledge26.json")
        prompt_path = os.path.join(DATA_DIR, "scoring_prompts26.txt")
        logger.info(f"Loading config: {domain_path}")
        logger.info(f"Loading config: {prompt_path}")
        
        with open(domain_path, encoding="utf-8") as f:
            domain_data = json.load(f)

        with open(prompt_path, encoding="utf-8") as f:
            prompt_template = f.read()

        logger.info("Config files loaded")

        return domain_data, prompt_template

    except Exception as e:
        logger.error(f"Config load failed: {e}")
        raise
# ==============================
# DIRECTORY SETUP
# ==============================

def ensure_dirs():
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        logger.info(f"Output directory ready: {OUTPUT_DIR}")
    except Exception as e:
        logger.error(f"Failed to create directory: {e}")
        raise
# ==============================
# LOAD INPUT DATA
# ==============================
def load_data():
    # Replace with Day 25 output later
    return [
        {
            "candidate_id": "CAND_001",
            "question": "Explain GST filing",
            "answer": "GST filing involves invoice tracking, ITC claims, and return submission.",
            "expected_answer": "GST filing includes calculating tax, input tax credit, and submitting returns."
        }
    ]


# ==============================
# SAVE OUTPUT
# ==============================

def save_output(data):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_path = os.path.join(
            OUTPUT_DIR,
            f"screening_results_{timestamp}.json"
        )

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        return file_path

    except Exception as e:
        logger.error(f"Failed to save output: {e}")
        raise


# ==============================
# MAIN PIPELINE
# ==============================

def run():
    logger.info("Pipeline started")

    ensure_dirs()

    # Load configs
    domain_data, prompt_template = load_configs()

    # Initialize engine
    engine = AdvancedScoringEngine(
        domain_data=domain_data,
        prompt_template=prompt_template
    )

    data = load_data()

    logger.info(f"Processing {len(data)} candidates")

    results = []
    failed = 0

    for item in data:
        try:
            result = engine.evaluate(
                item["question"],
                item["answer"],
                item["expected_answer"]
            )

            result["candidate_id"] = item.get("candidate_id", "UNKNOWN")
            results.append(result)

        except Exception as e:
            failed += 1
            logger.error(f"Error processing {item.get('candidate_id')}: {e}")

    # ==============================
    # METADATA
    # ==============================

    meta = {
        "run_id": f"RUN_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "run_time": datetime.now().isoformat(),
        "total_candidates": len(data),
        "processed": len(results),
        "failed": failed,
        "engine_version": "v2.2",
        "domain": "Chartered Accountant"
    }

    final_output = {
        "meta": meta,
        "results": results
    }

    output_path = save_output(final_output)

    logger.info("Pipeline completed successfully")
    logger.info(f"Output saved at: {output_path}")


# ==============================
# ENTRY POINT
# ==============================

if __name__ == "__main__":
    run()