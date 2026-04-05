def normalize_skill(skill: str) -> str:
    skill = skill.lower().strip()

    synonyms = {
        "ms excel": "excel",
        "microsoft excel": "excel",
        "gst filing": "gst",
        "tax": "taxation",
        "auditing": "audit"
    }

    return synonyms.get(skill, skill)