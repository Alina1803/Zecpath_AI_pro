# --------------------------------------
# Coding Task Evaluation Engine
# --------------------------------------


def coding_task_analysis(code):

    lines = len(code.splitlines())

    if lines < 20:
        return "Clean Solution"

    elif lines < 50:
        return "Moderate Complexity"

    return "Complex Implementation"
