CA_SKILLS = {
    "gst": ["gst", "input tax credit", "itc"],
    "tds": ["tds", "tax deducted at source"],
    "audit": ["audit", "internal control", "vouching"],
    "sap_fico": ["sap fico", "gl posting", "cost center"],
    "financial_reporting": ["balance sheet", "p&l", "cash flow"],
    "compliance": ["roc", "mca", "statutory", "ind as", "ifrs"]
}

def extract_ca_skills(text: str):
    text = text.lower()
    detected = []

    for skill, keywords in CA_SKILLS.items():
        for kw in keywords:
            if kw in text:
                detected.append(skill)
                break

    return detected