import re

def remove_bullets(text):
    text = re.sub(r"[•▪►●]", "", text)
    text = re.sub(r"\n+", "\n", text)
    return text.strip()