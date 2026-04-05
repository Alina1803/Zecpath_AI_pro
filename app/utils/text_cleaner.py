import re

def clean_text(text):
    if not text:
        return ""

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # 🔥 Fix broken letters from PDF
    text = re.sub(r"(\b\w\b\s)+\w\b", lambda m: m.group(0).replace(" ", ""), text)

    # Normalize dashes
    text = text.replace("–", "-").replace("—", "-")

    return text.strip()

def normalize_text(text):
    return text.lower().strip()


def remove_stopwords(text):
    STOPWORDS = {
        "and", "or", "the", "a", "an", "in", "on", "at", "for", "to", "of"
    }

    words = text.split()
    filtered = [w for w in words if w.lower() not in STOPWORDS]

    return " ".join(filtered)