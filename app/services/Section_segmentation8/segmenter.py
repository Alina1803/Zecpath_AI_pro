from app.services.Section_segmentation8.rule_based import is_heading, classify_heading

def segment_text(lines):
    sections = {}
    current_section = "other"
    sections[current_section] = []

    for line in lines:
        if is_heading(line):
            section = classify_heading(line)
            current_section = section
            if section not in sections:
                sections[section] = []
        else:
            sections[current_section].append(line)

    return sections