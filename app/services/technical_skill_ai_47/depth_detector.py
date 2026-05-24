# -------------------------------
# Depth Detection Engine
# -------------------------------

def detect_depth(text):
    keywords = [
        "because",
        "architecture",
        "optimize",
        "scalable",
        "tradeoff",
        "performance",
        "design"
    ]

    count = sum(word in text.lower() for word in keywords)

    if count >= 4:
        return 1.0

    elif count >= 2:
        return 0.7

    return 0.4