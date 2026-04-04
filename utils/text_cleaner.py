import re
import unicodedata


def normalize_unicode(text: str) -> str:
    """
    Convert special unicode characters to standard ASCII form.
    Example: “é” → "e"
    """
    return unicodedata.normalize("NFKD", text)


def remove_extra_whitespace(text: str) -> str:
    """
    Remove unnecessary spaces, tabs, and newlines.
    """
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def remove_urls(text: str) -> str:
    """
    Remove URLs from resume.
    """
    return re.sub(r'https?://\S+|www\.\S+', '', text)


def remove_emails(text: str) -> str:
    """
    Remove email addresses.
    """
    return re.sub(r'\S+@\S+', '', text)


def remove_phone_numbers(text: str) -> str:
    """
    Remove phone numbers (basic patterns).
    """
    return re.sub(r'\+?\d[\d\-\s]{8,}\d', '', text)


def normalize_case(text: str) -> str:
    """
    Convert text to lowercase for NLP processing.
    """
    return text.lower()


def remove_special_characters(text: str) -> str:
    """
    Keep only alphabets, numbers, and basic punctuation.
    """
    return re.sub(r'[^a-zA-Z0-9.,\n ]', '', text)


def clean_text(text: str) -> str:
    """
    Master function to clean resume text.
    Order of operations matters.
    """
    text = normalize_unicode(text)
    text = remove_urls(text)
    text = remove_emails(text)
    text = remove_phone_numbers(text)
    text = remove_special_characters(text)
    text = normalize_case(text)
    text = remove_extra_whitespace(text)

    return text