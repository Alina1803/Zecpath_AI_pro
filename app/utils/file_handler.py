def save_output(file_name, text):
    import os
    import json

    output_dir = "data/processed/output_5"
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, file_name + ".json")

    data = {
        "file_name": file_name,
        "cleaned_text": text
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"[SAVED] {output_file}")