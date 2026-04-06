import re

CERT_KEYWORDS = [
    "certified", "certification", "course", "training",
    "diploma", "license"
]


def extract_certifications(text):
    certifications = []

    lines = text.split("\n")

    for line in lines:
        line_lower = line.lower()

        if any(word in line_lower for word in CERT_KEYWORDS):
            certifications.append(line.strip())

    return certifications