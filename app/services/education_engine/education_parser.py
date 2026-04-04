import re

def extract_education(text):
    from app.services.education_engine.section_segmenter import extract_section

    clean_text = text.lower()

    section = extract_section(
        clean_text,
        ["education", "academic", "qualification"]
    )

    if not section:
        print("[DEBUG] No education section found, using full text")
        section = clean_text

    results = []

    # 🔥 Better splitting (handles line breaks + OCR)
    lines = re.split(r'[\n•\-]+', section)

    DEGREES = [
        "bachelor", "master", "b.sc", "m.sc",
        "b.tech", "m.tech", "bca", "mca",
        "mba", "phd", "diploma"
    ]

    for line in lines:
        line_low = line.strip().lower()

        if any(deg in line_low for deg in DEGREES):
            results.append({
                "degree": next((d for d in DEGREES if d in line_low), None),
                "original_line": line.strip()
            })

    print("Education extracted:", results)
    return results