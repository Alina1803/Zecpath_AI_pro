import os
import re
import json

from app.services.JD_Parser.jd_parser import parse_jd
from app.services.JD_Parser.pdf_reader import extract_text_from_pdf
from app.services.JD_Parser.section_splitter import split_role_blocks


PDF_PATH = "data/raw/Chartered Accountant.pdf"


def main():
    print(" Extracting full PDF text...")

    full_text = extract_text_from_pdf(PDF_PATH)

    if not full_text.strip():
        raise ValueError("PDF extraction failed.")

    # ==========================================
    # STEP 1: Split full domain PDF into roles
    # ==========================================
    role_blocks = split_role_blocks(full_text)

    print(f" Total Role Blocks Found: {len(role_blocks)}")

    output_dir = "data/processed/output_6_jd"
    os.makedirs(output_dir, exist_ok=True)

    all_roles_summary = []

    # ==========================================
    # STEP 2: Process each role block separately
    # ==========================================
    for block in role_blocks:
        role_name = block["role_name"]
        role_text = block["text"]

        print(f" Processing: {role_name}")

        # Parse only this role block
        result = parse_jd(role_text, [role_name])

        # Clean extracted sections
        sections = result.get("sections", {})

        # Safe filename
        safe_name = re.sub(
            r'[^a-zA-Z0-9]+',
            '_',
            role_name
        ).strip('_').lower()

        file_path = os.path.join(output_dir, f"{safe_name}.json")

        # Final clean JSON
        role_output = {
            "role": role_name,
            "matched": True,
            "confidence": 100.0,
            "matched_keywords": [role_name.lower()],

            "role_summary": sections.get("role_summary", ""),
            "responsibilities": sections.get("responsibilities", ""),
            "qualifications": sections.get("qualifications", ""),

            "skills": result.get("skills", {}),
            "sections": sections
        }

        # Save role JSON
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(role_output, f, indent=4)

        all_roles_summary.append(role_output)

    # ==========================================
    # STEP 3: Save combined summary
    # ==========================================
    summary_path = os.path.join(output_dir, "all_roles_summary.json")

    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(all_roles_summary, f, indent=4)

    print(
        f" Successfully created {len(role_blocks)} unique role JSON files!"
    )


if __name__ == "__main__":
    main()