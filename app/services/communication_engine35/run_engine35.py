import os
import json
from datetime import datetime
import traceback

from app.services.communication_engine35.communication_engine import CommunicationEngine


OUTPUT_DIR = os.path.join("data", "processed", "output_35")


def ensure_output_dir():
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
    except Exception as e:
        print(" Failed to create output directory:", e)


def save_result(result: dict):
    """
    Save output JSON safely
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"communication_score_{timestamp}.json"

        filepath = os.path.join(OUTPUT_DIR, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

        return filepath

    except Exception as e:
        print(" Failed to save result:", e)
        return None


def safe_evaluate(engine, answer):
    """
    Wrapper to prevent full crash
    """
    try:
        return engine.evaluate(answer)
    except Exception as e:
        print(" Evaluation failed:", e)
        traceback.print_exc()

        # fallback structure
        return {
            "final_score": 0,
            "component_scores": {},
            "error": str(e)
        }


if __name__ == "__main__":

    print(" Starting Communication Engine...")

    ensure_output_dir()

    try:
        engine = CommunicationEngine()
    except Exception as e:
        print(" Engine initialization failed:", e)
        exit(1)

    answer = """
    I believe communication is very important because it helps teams collaborate effectively.
    For example, in my previous project, clear communication improved delivery speed.
    """

    result = safe_evaluate(engine, answer)

    # ✅ Validate structure
    final_score = result.get("final_score", 0)
    component_scores = result.get("component_scores", {})

    output = {
        "timestamp": datetime.now().isoformat(),
        "input_answer": answer.strip(),
        "evaluation": result
    }

    saved_path = save_result(output)

    # ✅ Clean output
    print("\n ===== FINAL RESULT =====")
    print("Final Score:", final_score)
    print("Breakdown:", component_scores)

    if saved_path:
        print(" Saved to:", saved_path)
    else:
        print(" Result not saved")