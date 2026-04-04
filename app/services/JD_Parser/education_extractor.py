EDUCATION = ["chartered accountant", "ca", "icai", "bcom", "mcom"]


def extract_education(text):
    return list(set([e for e in EDUCATION if e in text]))