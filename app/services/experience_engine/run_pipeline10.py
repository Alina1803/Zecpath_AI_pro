import os
import json
from pprint import pprint

from app.services.experience_engine.parser import parse_experience
from app.services.experience_engine.text_preprocessor import remove_bullets
from app.services.experience_engine.relevance_engine import (
    calculate_total_experience,
    detect_gaps_and_overlaps
)
from app.services.experience_engine.extracted_pdf import extract_text_from_pdf


RAW_FOLDER = "data/raw"
OUTPUT_FOLDER = "data/processed/output_10"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


for file in os.listdir(RAW_FOLDER):

    file_path = os.path.join(RAW_FOLDER, file)

    print(f"\nProcessing: {file}")

    # -------- READ FILE --------
    if file.endswith(".txt"):

        with open(file_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

    elif file.endswith(".pdf"):

        raw_text = extract_text_from_pdf(file_path)

    else:
        continue


    # -------- PROCESS TEXT --------
    clean_text = remove_bullets(raw_text)

    experiences = parse_experience(clean_text)

    total_exp = calculate_total_experience(experiences)

    gaps, overlaps = detect_gaps_and_overlaps(experiences)


    # -------- RESULT --------
    result = {
        "file_name": file,
        "experience_details": experiences,
        "total_experience_years": total_exp,
        "total_experience_months": sum(role.get("duration_months", 0) for role in experiences),
        "gaps": gaps,
        "overlaps": overlaps
    }


    # -------- SAVE JSON --------
    output_file = os.path.join(
        OUTPUT_FOLDER,
        file.replace(".txt", ".json").replace(".pdf", ".json")
    )

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)


    # -------- PRINT OUTPUT --------
    pprint(result)

print("\nPipeline Finished Successfully")