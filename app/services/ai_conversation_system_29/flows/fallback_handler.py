def fallback_response(count: int):
    if count == 1:
        return "I didn't catch that. Could you answer the question?"
    elif count == 2:
        return "Please provide a complete answer so I can evaluate you."
    else:
        return "Ending interview due to no proper response."