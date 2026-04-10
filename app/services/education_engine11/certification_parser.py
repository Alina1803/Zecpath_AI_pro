import re

CERT_KEYWORDS = [
    "certified", "certification", "course", "training",
    "diploma", "license","cfa",
    "chartered financial analyst",
    "cpa",
    "certified public accountant",
    "acca",
    "association of chartered certified accountants",
    "cma",
    "certified management accountant"
]


def extract_certifications(text):
    certifications = []

    lines = text.split("\n")

    for line in lines:
        line_lower = line.lower()

        if any(word in line_lower for word in CERT_KEYWORDS):
            certifications.append(line.strip())

    return certifications