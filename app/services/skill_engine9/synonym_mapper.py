synonyms = {
        "ca": "chartered accountant",
"chartered accountant": "chartered accountant",
"qualified ca": "chartered accountant",
"certified chartered accountant": "chartered accountant",
"aca": "chartered accountant",
"fca": "chartered accountant",

"ca inter": "ca intermediate",
"ca intermediate": "ca intermediate",
"ca final": "chartered accountant",
"icai": "chartered accountant",
"member of icai": "chartered accountant",

"accountant": "chartered accountant",
"senior accountant": "chartered accountant",
"accounts executive": "chartered accountant",
"finance executive": "chartered accountant",
"finance manager": "chartered accountant",
"audit associate": "audit",
"auditor": "audit",
"tax consultant": "taxation",
"tax analyst": "taxation",

"gst filing": "gst",
"gst returns": "gst",
"income tax": "taxation",
"direct tax": "taxation",
"indirect tax": "taxation",

"statutory audit": "audit",
"internal audit": "audit",

"balance sheet": "financial reporting",
"profit and loss": "financial reporting",
"p&l": "financial reporting",

    }

def normalize_skill(skill: str) -> str:
    skill = skill.lower().strip()

    if skill in synonyms:
        return synonyms[skill]

    # fallback: partial match
    for key in synonyms:
        if key in skill:
            return synonyms[key]

    return skill