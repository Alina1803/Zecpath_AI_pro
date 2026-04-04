from app.services.Section_segmentation8.extractor import extract_text
from app.services.Section_segmentation8.preprocessing import split_lines
from app.services.Section_segmentation8.segmenter import segment_text
from app.services.Section_segmentation8.ml_model import SectionClassifier
from app.services.Section_segmentation8.evaluator import evaluate
import json
import os


def main():
    print("CURRENT DIR:", os.getcwd())

    output_path = r"E:/Zecpath_AI_pro/data/processed/output_8/predictions.json"

    # Step 1: Train model
    model = SectionClassifier()
    print("MODEL ATTRIBUTES:", dir(model))
    model.train("data/labeled/labeled_data.json")

    # Step 2: Load resume
    text = extract_text("data/raw/resume1.txt")
    lines = split_lines(text)

    # Step 3: Segment
    sections = segment_text(lines)

    # Step 4: Save output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(sections, f, indent=4)

    print(" Output saved at:", output_path)

    # Step 5: Evaluate
    evaluate(model, "data/labeled/labeled_data.json")


#  Entry point
if __name__ == "__main__":
    main()