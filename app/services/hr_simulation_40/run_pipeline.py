import os
import json
from datetime import datetime

from tests.hr_simulation40 import run_simulation
from app.services.hr_simulation_40.evaluation.accuracy_metrics import calculate_accuracy
from app.services.hr_simulation_40.evaluation.bias_analysis import analyze_bias

# 📁 Output directory
OUTPUT_DIR = os.path.join("data", "processed", "output_40")


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_results(results, accuracy, bias):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_data = {
        "timestamp": timestamp,
        "accuracy": accuracy,
        "bias": bias,
        "results": results
    }

    filename = f"hr_simulation_{timestamp}.json"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w") as f:
        json.dump(output_data, f, indent=4)

    print(f"\n Results saved to: {filepath}")


def main():
    ensure_output_dir()

    results = run_simulation()

    accuracy = calculate_accuracy(results)
    bias = analyze_bias(results)

    print("\n=== HR SIMULATION RESULTS ===")
    print("Accuracy:", accuracy, "%")
    print("Bias:", bias)

    # 💾 Save output
    save_results(results, accuracy, bias)


if __name__ == "__main__":
    main()