import re

DEGREES = [
    "bachelor", "master", "b.com", "m.com", "bsc", "msc",
    "mba", "bba", "ca", "chartered accountant"
]


def extract_education(text):
    education_list = []

    lines = text.split("\n")

    for line in lines:
        line_lower = line.lower()

        if any(degree in line_lower for degree in DEGREES):

            year_match = re.search(r"(19|20)\d{2}", line)

            education_list.append({
                "degree": line.strip(),
                "year": year_match.group() if year_match else None
            })

    return education_list