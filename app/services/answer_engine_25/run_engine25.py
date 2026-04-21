import os
import json
from datetime import datetime

from app.services.answer_engine_25.answer_engine import AnswerEngine


BASE_DIR = os.getcwd()

INPUT_DIR = os.path.join(BASE_DIR, "Data", "processed", "output_24_Audio")
OUTPUT_DIR = os.path.join(BASE_DIR, "Data", "processed", "output_25")


def load_files():
    if not os.path.exists(INPUT_DIR):
        print(f"[ERROR] Input folder not found: {INPUT_DIR}")
        return []

    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".json")]

    if not files:
        print("[WARNING] No JSON files found in output_24")
        return []

    return files


def save_output(data, file_name):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    base_name = file_name.replace(".json", "")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_file = os.path.join(OUTPUT_DIR, f"{base_name}_{timestamp}.json")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"[SAVED] {output_file}")


def run():

    print("[INFO] Running Day 25 from output_24")

    engine = AnswerEngine()
    files = load_files()

    if not files:
        return

    for file_name in files:

        file_path = os.path.join(INPUT_DIR, file_name)

        print(f"\n[PROCESSING] {file_name}")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

        except Exception as e:
            print(f"[ERROR] Failed to read {file_name}: {e}")
            continue

        clean_text = data.get("clean_text", "").strip()

        if not clean_text:
            print("[SKIPPED] No clean_text found")
            continue

        # 👉 Apply Day 25
        analysis = engine.process(clean_text)

        result = {
            "audio_file": data.get("audio_file"),
            "clean_text": clean_text,
            "analysis": analysis
        }

        save_output(result, file_name)

    print("\n✅ Day 25 processing completed!")


if __name__ == "__main__":
    run()