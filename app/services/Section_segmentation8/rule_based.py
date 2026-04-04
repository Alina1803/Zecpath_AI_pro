SECTION_HEADERS = {
    "skills": ["skills", "technical skills"],
    "education": ["education"],
    "experience": ["experience", "work experience"],
    "projects": ["projects"],
    "certifications": ["certifications"],
    "summary": ["summary", "objective"]
}

def is_heading(line):
    if line.isupper():
        return True
    if line.endswith(":"):
        return True
    return False

def classify_heading(line):
    line = line.lower()
    for section, keywords in SECTION_HEADERS.items():
        for kw in keywords:
            if kw in line:
                return section
    return "other"