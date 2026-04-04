import re


def normalize_text(text):
    """
    Normalize text to handle OCR issues and inconsistent formatting
    """
    text = text.lower()

    # Fix OCR spaced words like: E D U C A T I O N
    text = re.sub(r'(?<=\b)([a-z])\s+(?=[a-z]\b)', r'\1', text)

    # Replace multiple spaces/newlines
    text = re.sub(r'\s+', ' ', text)

    return text


def extract_section(text, keywords):
    """
    Extract a section from resume text using flexible keyword matching
    """

    if not text:
        return None

    text = normalize_text(text)

    # Convert keywords to lowercase
    keywords = [k.lower() for k in keywords]

    # Common section headers (used to detect section boundaries)
    ALL_HEADERS = [
        "education", "academic", "qualification",
        "experience", "work experience", "employment",
        "projects", "skills", "summary",
        "certification", "certifications",
        "licenses", "awards", "achievements"
    ]

    # 🔍 Find start position
    start_idx = -1
    for kw in keywords:
        match = re.search(rf"\b{re.escape(kw)}\b", text)
        if match:
            start_idx = match.start()
            break

    # ❌ If no keyword found
    if start_idx == -1:
        return None

    # 🔍 Find end position (next section header)
    end_idx = len(text)

    for header in ALL_HEADERS:
        if header in keywords:
            continue

        match = re.search(rf"\b{re.escape(header)}\b", text[start_idx + 1:])
        if match:
            end_idx = start_idx + 1 + match.start()
            break

    section = text[start_idx:end_idx]

    return section.strip()