def normalize_skill(skill: str) -> str:
    skill = skill.lower().strip()

    synonyms = {
        "ms excel": "excel",
        "microsoft excel": "excel",
        "advanced excel": "excel",

        "gst filing": "gst",
        "gst returns": "gst",

        "tax": "taxation",
        "tax filing": "taxation",

        "auditing": "audit",
        "internal audit": "audit",

        "financial analysis": "finance"
    }

    return synonyms.get(skill, skill)