import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_lines(text):
    return [line.strip() for line in text.split("\n") if line.strip()]