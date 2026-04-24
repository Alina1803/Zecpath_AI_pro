import json
import os
from datetime import datetime

from app.services.screening_system_30.intent_detection import train_intent_model
from app.services.screening_system_30.simulator import simulate_call
from app.services.screening_system_30.evaluator import evaluate
from app.services.screening_system_30.optimizer import optimize_threshold

def main():
    print("===== SCREENING SYSTEM PIPELINE STARTED =====\n")

    # -------------------------------
    # 1. Load Training Data
    # -------------------------------
    with open('data/test_data30.json') as f:
        train_data = json.load(f)

    print("Training data loaded...")

    # -------------------------------
    # 2. Train Intent Model
    # -------------------------------
    train_intent_model(train_data)
    print("Model trained successfully...\n")

    # -------------------------------
    # 3. Simulate Screening Calls
    # -------------------------------
    test_inputs = [
        "I have 3 years experience in Python",
        "Looking for job",
        "My skills include AI and ML",
        "Hi"
    ]

    results = []

    print("---- Simulation Results ----")
    for inp in test_inputs:
        res = simulate_call(inp)
        results.append(res)
        print(res)

    # -------------------------------
    # 4. Evaluate System
    # -------------------------------
    accuracy = evaluate(results)
    print("\nAccuracy:", accuracy)

    # -------------------------------
    # 5. Optimize Threshold
    # -------------------------------
    threshold, best_acc = optimize_threshold(results)
    print("Best Threshold:", threshold)
    print("Optimized Accuracy:", best_acc)

    # -------------------------------
    # 6. Ensure Output Directory Exists
    # -------------------------------
    output_dir = "data/processed/output_30"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"\n Created folder: {output_dir}")
    else:
        print(f"\n Folder already exists: {output_dir}")

    # -------------------------------
    # 7. Save Report with Timestamp
    # -------------------------------
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"test_report_{timestamp}.txt"
    output_file = os.path.join(output_dir, filename)

    with open(output_file, 'w') as f:
        f.write("SCREENING SYSTEM TEST REPORT\n")
        f.write("====================================\n")
        f.write(f"Generated on: {timestamp}\n\n")

        f.write("---- Simulation Results ----\n")
        for r in results:
            f.write(str(r) + "\n")

        f.write("\n---- Evaluation ----\n")
        f.write(f"Accuracy: {accuracy}\n")

        f.write("\n---- Optimization ----\n")
        f.write(f"Best Threshold: {threshold}\n")
        f.write(f"Optimized Accuracy: {best_acc}\n")

    print(f"\n Report saved at: {output_file}")
    print("\n===== PIPELINE COMPLETED SUCCESSFULLY =====")


if __name__ == "__main__":
    main()