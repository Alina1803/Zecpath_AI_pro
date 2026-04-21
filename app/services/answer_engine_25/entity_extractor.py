import re

class EntityExtractor:

    SKILLS = [
        "gst", "taxation", "audit", "tds",
        "tally", "balance sheet", "financial analysis"
    ]

    def extract_skills(self, text):
        text = text.lower()
        return [skill for skill in self.SKILLS if skill in text]

    def extract_experience(self, text):
        match = re.search(r'(\d+)\s*(years?|yrs?)', text.lower())
        return match.group(0) if match else None

    def extract_salary(self, text):
        match = re.search(r'(\d+)\s*(lpa|lakhs?)', text.lower())
        return match.group(0) if match else None

    def extract_availability(self, text):
        text = text.lower()

        if "immediate" in text:
            return "Immediate"

        if "notice period" in text:
            return "Notice Period"

        return None