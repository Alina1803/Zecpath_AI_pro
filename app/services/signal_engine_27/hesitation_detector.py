HESITATION_WORDS = ["um", "uh", "maybe", "not sure", "I think", "probably"]

def detect_hesitation(text):
    count = sum(word in text.lower() for word in HESITATION_WORDS)
    return min(count / 5, 1.0)  # normalized