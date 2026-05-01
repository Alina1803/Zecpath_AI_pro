def extract_reasoning_steps(text):
    steps = []
    keywords = ["first", "then", "next", "finally"]

    for word in keywords:
        if word in text.lower():
            steps.append(word)

    return steps


def detect_structured_thinking(text):
    return len(extract_reasoning_steps(text)) > 2