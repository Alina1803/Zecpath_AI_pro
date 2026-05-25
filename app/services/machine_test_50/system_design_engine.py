# --------------------------------------
# Mini System Design Evaluation
# --------------------------------------

def design_evaluation(modules):

    if modules >= 5:
        return "Scalable Architecture"

    elif modules >= 3:
        return "Structured Design"

    return "Basic Design"