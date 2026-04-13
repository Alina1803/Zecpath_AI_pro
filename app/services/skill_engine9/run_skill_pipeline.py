import os
import json
from .skill_extractor import extract_skills
from .confidence_engine import score_skill_confidence


def run_skill_pipeline(input_json, output_json):
    with open(input_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("[DEBUG] JSON Keys:",data.keys())

    text = (
            data.get("raw_text")
            or data.get("text")
            or data.get("resume_text")
            or data.get("full_text")
            or json.dumps(data)
            )

    
    skills = extract_skills(text)

    scored = []
    for skill in skills:
        scored.append({
            "skill": skill,
            "confidence": score_skill_confidence(skill, text)
        })

    data["skills"] = scored

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return data


# ==========================
# MAIN EXECUTION
# ==========================
if __name__ == "__main__":
    input_root = "data/processed"
    output_folder = "data/processed/output_9_skills"

    os.makedirs(output_folder, exist_ok=True)

    processed_files = 0

    for root, dirs, files in os.walk(input_root):
        if "output_folder" in root:
            continue

        for file_name in files:
            if file_name.endswith(".json"):
                input_path = os.path.join(root, file_name)
                output_path = os.path.join(output_folder, file_name)

                print(f"[LOG] Processing: {input_path}")

                try:
                    result = run_skill_pipeline(input_path, output_path)
                    print(f"[LOG] Saved: {output_path}")
                    processed_files += 1

                except Exception as e:
                    print(f"[ERROR] Failed on {file_name}: {e}")

    print(f"\n Skill pipeline completed for {processed_files} files.")