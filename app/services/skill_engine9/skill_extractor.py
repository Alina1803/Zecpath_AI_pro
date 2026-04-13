import spacy
from spacy.matcher import PhraseMatcher

from .skill_dictionary import MASTER_SKILLS
from .synonym_mapper import normalize_skill
from .stack_resolver import expand_stack


# -------------------------------
# LOAD MODEL ONLY ONCE (CRITICAL)
# -------------------------------
nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

skill_map = {}

# -------------------------------
# BUILD MATCHER ONCE
# -------------------------------
patterns = []

for category, skills in MASTER_SKILLS.items():
    for canonical, aliases in skills.items():
        for alias in aliases:
            doc = nlp.make_doc(alias)
            patterns.append(doc)
            skill_map[alias.lower()] = canonical

matcher.add("SKILLS", patterns)


# -------------------------------
# MAIN EXTRACTION FUNCTION
# -------------------------------
def extract_skills(text: str):

    if not text or not text.strip():
        return []

    doc = nlp(text)
    matches = matcher(doc)

    found_skills = set()

    for _, start, end in matches:
        span = doc[start:end].text.lower()

        canonical = skill_map.get(span, span)
        normalized = normalize_skill(canonical)
        expanded = expand_stack(normalized)

        for skill in expanded:
            found_skills.add(skill)

    return sorted(list(found_skills))