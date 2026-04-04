import json
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from datetime import datetime

def evaluate(model, data_path):
    # Load labeled data
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = [item["text"] for item in data]
    labels = [item["label"] for item in data]

    # Predictions
    predictions = model.predict(texts)

    # Metrics
    accuracy = accuracy_score(labels, predictions)
    precision = precision_score(labels, predictions, average='weighted')
    recall = recall_score(labels, predictions, average='weighted')
    f1 = f1_score(labels, predictions, average='weighted')

    # Output file
    output_file = "data/processed/output_8/outputs/accuracy_report.txt"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Write report
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("SECTION SEGMENTATION MODEL - EVALUATION REPORT\n")
        f.write("="*45 + "\n\n")

        f.write(f"Total Samples: {len(labels)}\n")
        f.write(f"Correct Predictions: {(predictions == labels).sum()}\n")
        f.write(f"Incorrect Predictions: {(predictions != labels).sum()}\n\n")

        f.write(f"Accuracy: {accuracy:.2%}\n\n")

        f.write("-"*45 + "\n")
        f.write("CLASSIFICATION DETAILS\n\n")

        f.write(f"Precision: {precision:.2f}\n")
        f.write(f"Recall:    {recall:.2f}\n")
        f.write(f"F1-Score:  {f1:.2f}\n\n")

        f.write("-"*45 + "\n")
        f.write("MODEL INFO\n\n")

        f.write("Vectorizer: TF-IDF\n")
        f.write("Model: Logistic Regression\n\n")

        f.write("-"*45 + "\n")
        f.write(f"Generated On: {datetime.now().strftime('%Y-%m-%d')}\n")

    print("📊 Evaluation report saved at:", output_file)