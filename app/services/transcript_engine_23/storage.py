import json
import os
from datetime import datetime

OUTPUT_DIR = "data/transcripts23/processed"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_transcript(candidate_id, data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") 
    file_name = f"{candidate_id}_{timestamp}.json"
    file_path = os.path.join(OUTPUT_DIR, file_name)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return file_path