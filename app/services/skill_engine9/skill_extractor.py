import spacy
from spacy.matcher import PhraseMatcher

from .skill_dictionary import MASTER_SKILLS
from .synonym_mapper import normalize_skill
from .stack_resolver import expand_stack


class SkillExtractor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")

        patterns = []
        self.skill_map = {}

        for category, skills in MASTER_SKILLS.items():
            for canonical, aliases in skills.items():
                for alias in aliases:
                    doc = self.nlp.make_doc(alias)
                    patterns.append(doc)
                    self.skill_map[alias.lower()] = canonical

        self.matcher.add("SKILLS", patterns)

    def extract(self, text):
        doc = self.nlp(text)
        matches = self.matcher(doc)

        found_skills = set()

        for match_id, start, end in matches:
            span = doc[start:end].text.lower()
            canonical = self.skill_map.get(span, span)
            normalized = normalize_skill(canonical)
            expanded = expand_stack(normalized)

            for skill in expanded:
                found_skills.add(skill)

        return list(found_skills)


# ✅ ADD THIS FUNCTION (IMPORTANT FIX)
def extract_skills(text):
    extractor = SkillExtractor()
    return extractor.extract(text)