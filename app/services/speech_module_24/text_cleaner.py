import re

FILLER_WORDS = [
    "um", "uh", "you know", "like", "actually",
    "basically", "so", "okay", "right"
]

class TextCleaner:

    def remove_fillers(self, text):
        pattern = r'\b(' + '|'.join(FILLER_WORDS) + r')\b'
        return re.sub(pattern, '', text, flags=re.IGNORECASE)

    def normalize_case(self, text):
        return text.lower()

    def fix_spacing(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def basic_punctuation(self, text):
        if not text.endswith('.'):
            text += '.'
        return text

    def clean_text(self, text):
        text = self.remove_fillers(text)
        text = self.normalize_case(text)
        text = self.fix_spacing(text)
        text = self.basic_punctuation(text)
        return text