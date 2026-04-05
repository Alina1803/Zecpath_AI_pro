from .synonym_mapper import normalize_skill
from app.utils.constants import SKILL_KEYWORDS

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILL_KEYWORDS:
        if skill in text:
            normalized = normalize_skill(skill)
            found_skills.append(normalized)

    return list(set(found_skills))