import os
import json
import datetime
import logging

from app.services.ethics_ai_43.ethics_framework import validate_ethics
from app.services.ethics_ai_43.fairness_review import remove_bias_features
from app.services.ethics_ai_43.explainability import generate_explanation
from app.services.ethics_ai_43.compliance import consent_check, check_retention
from app.utils.data_masking43 import mask_data


# -------------------------------
# Logging Configuration
# -------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# -------------------------------
# Output Directory
# -------------------------------
OUTPUT_DIR = "data/processed/output_43"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# -------------------------------
# Core Processing Function
# -------------------------------
def process_candidate(candidate: dict) -> dict:
    try:
        # Add timestamp (ISO format)
        current_time = datetime.datetime.now()
        candidate["date"] = current_time.isoformat()

        # Step 1: Consent check
        if not consent_check(candidate.get("consent")):
            return {"error": "Consent required"}

        # Step 2: Remove bias fields
        unbiased_data = remove_bias_features(candidate)

        # Step 3: Mask sensitive data
        masked_data = mask_data(unbiased_data)

        # Step 4: Ethics validation
        ethics_ok = validate_ethics()

        # Step 5: Explainability
        explanation = generate_explanation(candidate.get("score", 0))

        # Step 6: Retention check
        retention_status = check_retention(
            datetime.datetime.fromisoformat(candidate["date"])
        )

        # Final Output
        return {
            "data": masked_data,
            "ethics_valid": ethics_ok,
            "explanation": explanation,
            "retention": retention_status,
            "timestamp": candidate["date"]
        }

    except Exception as e:
        logger.error(f"Processing failed: {e}")
        return {"error": str(e)}


# -------------------------------
# Pipeline Runner
# -------------------------------
def run_pipeline():

    candidate = {
        "name": "John",
        "gender": "Male",
        "email": "john@email.com",
        "score": 78,
        "consent": True
    }

    result = process_candidate(candidate)

    # Save output
    output_path = os.path.join(OUTPUT_DIR, "final_output.json")

    try:
        with open(output_path, "w") as f:
            json.dump(result, f, indent=4)

        logger.info(f" Output saved to: {output_path}")

    except Exception as e:
        logger.error(f"Failed to save output: {e}")


# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    run_pipeline()