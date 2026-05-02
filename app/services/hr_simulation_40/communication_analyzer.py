def communication_score(answer: str) -> float:
    length = len(answer.split())
    
    if length < 5:
        return 50
    elif length < 15:
        return 70
    else:
        return 85