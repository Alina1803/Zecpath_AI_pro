import spacy
from spacy.matcher import PhraseMatcher

from .skill_dictionary import MASTER_SKILLS
from .synonym_mapper import normalize_skill
from .stack_resolver import expand_stack


class SkillExtractor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

        # LOWER = case-insensitive matching
        self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")

        self.skill_map = {}

        patterns = []

        for category, skills in MASTER_SKILLS.items():
            for canonical, aliases in skills.items():
                for alias in aliases:
                    doc = self.nlp.make_doc(alias)
                    patterns.append(doc)
                    self.skill_map[alias.lower()] = canonical

        self.matcher.add("SKILLS", patterns)

    def extract_skills(self, text):
        doc = self.nlp(text)

        matches = self.matcher(doc)

        found = []

        for match_id, start, end in matches:
            phrase = doc[start:end].text.lower()

            canonical = self.skill_map.get(phrase, phrase)

            expanded = expand_stack(canonical)

            for skill in expanded:
                found.append(normalize_skill(skill))

        return list(set(found))