import os
import json
from datetime import datetime

from app.services.speech_module_24.stt_engine import SpeechToTextEngine
from app.services.speech_module_24.text_cleaner import TextCleaner
from app.services.speech_module_24.transcript_processor import TranscriptProcessor
from app.services.speech_module_24.accuracy_test import STTAccuracy


# ✅ FIXED BASE DIR
BASE_DIR = os.getcwd()

# ✅ Input & Output directories
INPUT_DIR = os.path.join(BASE_DIR, "data", "raw", "Audios")
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "processed", "output_24_Audio")


def save_output(result, audio_path):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"{base_name}_{timestamp}.json"
    file_path = os.path.join(OUTPUT_DIR, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

    print(f"[SAVED] {file_path}")


def run_pipeline(audio_path, ground_truth=None):

    print(f"\n[PROCESSING] {audio_path}")

    if not os.path.exists(audio_path):
        print(f"[ERROR] File not found: {audio_path}")
        return None

    if os.path.getsize(audio_path) == 0:
        print(f"[SKIPPED] Empty file: {audio_path}")
        return None

    print("[STEP 1] Speech-to-Text")
    stt = SpeechToTextEngine()
    stt_output = stt.transcribe(audio_path)

    print("[STEP 2] Processing Transcript")
    processor = TranscriptProcessor()
    processed_text = processor.process(stt_output)

    print("[STEP 3] Cleaning Text")
    cleaner = TextCleaner()
    clean_text = cleaner.clean_text(processed_text)

    result = {
        "audio_file": audio_path,
        "raw_text": stt_output["full_text"],
        "processed_text": processed_text,
        "clean_text": clean_text
    }

    if ground_truth:
        print("[STEP 4] Accuracy Testing")
        tester = STTAccuracy()
        result["accuracy"] = tester.calculate_wer(ground_truth, clean_text)

    save_output(result, audio_path)

    return result


if __name__ == "__main__":

    print(f"[DEBUG] BASE_DIR: {BASE_DIR}")
    print(f"[INFO] Reading from: {INPUT_DIR}")

    # ✅ Ensure input folder exists
    if not os.path.exists(INPUT_DIR):
        print(f"[INFO] Creating missing folder: {INPUT_DIR}")
        os.makedirs(INPUT_DIR, exist_ok=True)
        print("[WARNING] Add audio files and rerun.")
        exit()

    # ✅ Read audio files
    audio_files = [
        f for f in os.listdir(INPUT_DIR)
        if f.lower().endswith((".wav", ".mp3", ".m4a"))
    ]

    if not audio_files:
        print("[WARNING] No audio files found in input directory")
        exit()

    for file_name in audio_files:
        audio_path = os.path.join(INPUT_DIR, file_name)
        run_pipeline(audio_path)

    print("\n✅ Batch processing completed!")