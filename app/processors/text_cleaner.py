import re

def clean_text(text):
    # Remove special characters
    text = re.sub(r'[^\w\s\.\,\-\@\(\)]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()