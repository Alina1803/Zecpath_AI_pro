HESITATION_WORDS = ["uh", "um", "maybe", "i think", "not sure"]

def detect_confidence(answer: str) -> float:
    answer = answer.lower()
    penalty = sum(1 for word in HESITATION_WORDS if word in answer)
    
    score = max(0, 100 - penalty * 10)
    return score