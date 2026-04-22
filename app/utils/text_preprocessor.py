import re


class TextPreprocessor:

    @staticmethod
    def clean_text(text: str) -> str:
        text = text.lower()
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^a-z0-9\s]', '', text)
        return text.strip()

    @staticmethod
    def tokenize(text: str):
        return text.split()

    @staticmethod
    def remove_stopwords(tokens):
        stopwords = {"is", "the", "and", "a", "an", "in", "of", "to"}
        return [t for t in tokens if t not in stopwords]