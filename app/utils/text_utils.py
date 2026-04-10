import re
import string

# ----------------------------------------
# 🔹 Basic Text Cleaning
# ----------------------------------------

def clean_text(text: str) -> str:
    """
    Clean raw text from resumes/JDs
    """
    if not text:
        return ""

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove special characters (keep basic punctuation)
    text = re.sub(r"[^a-zA-Z0-9.,+/# ]", "", text)

    return text.strip().lower()


# ----------------------------------------
# 🔹 Advanced Preprocessing
# ----------------------------------------

def preprocess_text(text: str) -> str:
    """
    Full preprocessing pipeline
    """
    text = clean_text(text)
    text = remove_stopwords(text)
    text = normalize_text(text)
    return text


# ----------------------------------------
# 🔹 Stopword Removal
# ----------------------------------------

STOPWORDS = {
    "the", "is", "in", "and", "to", "of", "a", "for", "on", "with",
    "as", "by", "an", "at", "from", "or", "that", "this", "it"
}

def remove_stopwords(text: str) -> str:
    words = text.split()
    filtered = [w for w in words if w not in STOPWORDS]
    return " ".join(filtered)


# ----------------------------------------
# 🔹 Normalize Text
# ----------------------------------------

def normalize_text(text: str) -> str:
    """
    Normalize common variations
    """
    replacements = {
        "b.tech": "btech",
        "m.tech": "mtech",
        "e-mail": "email",
        "machine learning": "ml",
        "artificial intelligence": "ai"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text


# ----------------------------------------
# 🔹 Tokenization
# ----------------------------------------

def tokenize(text: str) -> list:
    return text.split()


# ----------------------------------------
# 🔹 Keyword Matching
# ----------------------------------------

def keyword_match(text: str, keywords: list) -> list:
    """
    Returns matched keywords
    """
    text = text.lower()
    matches = [kw for kw in keywords if kw.lower() in text]
    return matches


# ----------------------------------------
# 🔹 Similarity (Basic)
# ----------------------------------------

def jaccard_similarity(text1: str, text2: str) -> float:
    """
    Basic similarity score
    """
    set1 = set(tokenize(text1))
    set2 = set(tokenize(text2))

    if not set1 or not set2:
        return 0.0

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    return len(intersection) / len(union)


# ----------------------------------------
# 🔹 Extract Numbers (Experience, Years)
# ----------------------------------------

def extract_numbers(text: str) -> list:
    return re.findall(r"\d+", text)


# ----------------------------------------
# 🔹 Extract Emails
# ----------------------------------------

def extract_emails(text: str) -> list:
    return re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)


# ----------------------------------------
# 🔹 Extract Phone Numbers
# ----------------------------------------

def extract_phone_numbers(text: str) -> list:
    return re.findall(r"\+?\d[\d\s\-]{8,15}\d", text)