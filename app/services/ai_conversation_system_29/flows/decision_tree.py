def decide_next_step(answer: str):
    if not answer or answer.strip() == "":
        return "handle_silence"

    if len(answer.split()) < 3:
        return "short_answer"

    return "evaluate_answer"