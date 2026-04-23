def get_feedback(result):
    if result == "good":
        return "Good answer 👍"
    elif result == "average":
        return "Decent answer, but can improve."
    return "Answer is too short. Please elaborate."