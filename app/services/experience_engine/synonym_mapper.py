def normalize_skill(skill: str) -> str:
    skill = skill.lower().strip()

    synonyms = {
        "gst": ["goods and services tax"],
    "tds": ["tax deducted at source"],
    "sap fico": ["sap finance", "sap fico module"],
    "ifrs": ["international financial reporting standards"],
    "gaap": ["generally accepted accounting principles"],
    "fp&a": ["financial planning and analysis"],
    "mis reporting": ["management information system reporting"]
    }

    return synonyms.get(skill, skill)