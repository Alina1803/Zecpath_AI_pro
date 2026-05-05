import os
import json

from app.services.optimization_stability42.interview_ai.stable_hr_ai import stable_hr_evaluation
from app.services.optimization_stability42.interview_ai.refined_scoring import refined_score_pipeline
from app.services.optimization_stability42.screening_ai.optimized_cleaner import advanced_clean
from app.utils.batch_processing import batch_process

OUTPUT_DIR = "data/processed/output_42"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# -----------------------------------
# Process Single Candidate
# -----------------------------------
def process_candidate(candidate):

    raw_scores = candidate["scores"]
    confidence_scores = candidate["confidence"]
    transcript = candidate["transcript"]

    # Step 1: Clean transcript
    clean_text = advanced_clean(transcript)

    # Step 2: Refined scoring
    refined_scores = refined_score_pipeline(raw_scores, confidence_scores)

    # Step 3: Stable evaluation
    result = stable_hr_evaluation(refined_scores)

    return {
        "cleaned_transcript": clean_text,
        "refined_scores": refined_scores,
        "evaluation": result
    }


# -----------------------------------
# Main Pipeline
# -----------------------------------
def run_pipeline():

    # ✅ Multiple candidates (Batch Input)
    candidates = [
        {
            "scores": [50, 60, 90, 30],
            "confidence": [60, 70, 80, 50],
            "transcript": "Um I think I I can do this job, you know..."
        },
        {
            "scores": [70, 75, 80, 65],
            "confidence": [80, 85, 90, 70],
            "transcript": "Uh I have strong experience in backend development..."
        }
    ]

    # ✅ Batch processing
    results = batch_process(candidates, process_candidate)

    # Save output
    output_path = os.path.join(OUTPUT_DIR, "final_output.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)

    print(" Batch output saved to:", output_path)


if __name__ == "__main__":
    run_pipeline()