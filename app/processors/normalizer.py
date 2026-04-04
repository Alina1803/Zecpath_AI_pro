def normalize_text(text):
    # Lowercase
    text = text.lower()

    # Normalize bullet points
    text = text.replace("•", "-")
    text = text.replace("●", "-")

    # Normalize headings (simple rule)
    lines = text.split("\n")
    normalized_lines = []

    for line in lines:
        if line.isupper():
            normalized_lines.append(line.title())
        else:
            normalized_lines.append(line)

    return "\n".join(normalized_lines)