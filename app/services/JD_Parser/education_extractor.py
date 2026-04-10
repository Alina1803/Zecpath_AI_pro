EDUCATION = [ "chartered accountant",
    "ca",
    "ca inter",
    "ca intermediate",
    "ca final",
    "icai"
    ]


def extract_education(text):
    return list(set([e for e in EDUCATION if e in text]))