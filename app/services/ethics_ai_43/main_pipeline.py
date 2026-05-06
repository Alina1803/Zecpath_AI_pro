import os
import json
import datetime

from app.services.ethics_ai_43.ethics_framework import validate_ethics
from app.services.ethics_ai_43.fairness_review import remove_bias_features
from app.services.ethics_ai_43.explainability import generate_explanation
from app.services.ethics_ai_43.compliance import consent_check, check_retention
from app.utils.data_masking43 import mask_data


OUTPUT_DIR = "data/processed/output_43"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def run_pipeline():

    # ✅ Convert datetime at source (BEST PRACTICE)
    current_time = datetime.datetime.now()

    candidate = {
        "name": "John",
        "gender": "Male",
        "email": "john@email.com",
        "score": 78,
        "consent": True,
        "date": current_time.isoformat()   # stored as string
    }

    # Step 1: Consent check
    if not consent_check(candidate["consent"]):
        print(" Consent required")
        return

    # Step 2: Remove bias fields
    unbiased_data = remove_bias_features(candidate)

    # Step 3: Mask sensitive data
    masked_data = mask_data(unbiased_data)

    # Step 4: Ethics validation
    ethics_ok = validate_ethics()

    # Step 5: Explainability
    explanation = generate_explanation(candidate["score"])

    # Step 6: Retention check (convert back to datetime)
    retention_status = check_retention(
        datetime.datetime.fromisoformat(candidate["date"])
    )

    # Final Output (clean JSON-safe structure)
    final_output = {
        "data": masked_data,
        "ethics_valid": ethics_ok,
        "explanation": explanation,
        "retention": retention_status,
        "timestamp": candidate["date"]   # already string
    }

    # Save output
    output_path = os.path.join(OUTPUT_DIR, "final_output.json")

    with open(output_path, "w") as f:
        json.dump(final_output, f, indent=4)

    print(" Output saved to:", output_path)


if __name__ == "__main__":
    run_pipeline()