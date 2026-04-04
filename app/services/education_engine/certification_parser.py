def extract_certifications(text):
    from app.services.education_engine.section_segmenter import extract_section
    import re

    clean_text = text.lower()

    section = extract_section(
        clean_text,
        ["certification", "certifications", "license"]
    )

    if not section:
        return []  # ❗ REMOVE fallback (important)

    lines = re.split(r'[\n•\-]+', section)

    KEYWORDS = [
        "certified", "certificate", "certification",
        "aws", "google", "microsoft", "pmp", "cfa"
    ]

    results = []

    for line in lines:
        line_low = line.strip().lower()

        if any(k in line_low for k in KEYWORDS):
            results.append(line.strip())

    print("Certifications extracted:", results)
    return results