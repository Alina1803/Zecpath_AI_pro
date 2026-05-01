import re


# ===============================
# 🧹 CLEAN TEXT
# ===============================
def clean_text(text: str) -> str:
    """
    Normalize text:
    - Lowercase
    - Remove special characters
    - Remove extra spaces
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# ===============================
# 🔤 TOKENIZATION
# ===============================
def tokenize(text: str):
    """
    Split text into words
    """
    text = clean_text(text)
    return text.split()


# ===============================
# 🔍 KEYWORD MATCH COUNT
# ===============================
def keyword_match_count(text: str, keywords: list) -> int:
    """
    Count how many keywords appear in text
    """
    words = tokenize(text)
    return sum(1 for word in keywords if word in words)


# ===============================
# 🔎 KEYWORD PRESENCE
# ===============================
def contains_any(text: str, keywords: list) -> bool:
    """
    Check if any keyword exists in text
    """
    words = tokenize(text)
    return any(word in words for word in keywords)


# ===============================
# 📏 TEXT LENGTH SCORE
# ===============================
def length_score(text: str, threshold: int = 10) -> float:
    """
    Score based on text length
    """
    word_count = len(tokenize(text))

    if word_count >= threshold:
        return 1.0
    elif word_count >= threshold // 2:
        return 0.7
    return 0.4


# ===============================
# 🧠 STEP DETECTION
# ===============================
def detect_steps(text: str) -> int:
    """
    Detect structured reasoning steps
    """
    step_words = ["first", "then", "next", "finally"]

    return keyword_match_count(text, step_words)


# ===============================
# 🧾 DEBUG HELPER
# ===============================
def debug_text(text: str):
    """
    Print debug info for analysis
    """
    print("Cleaned:", clean_text(text))
    print("Tokens:", tokenize(text))