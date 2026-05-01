from app.services.aptitude_logic_38.text_processing import keyword_match_count, contains_any, length_score

def detect_structure(text):
    keywords = ["first", "then", "next", "finally", "because", "therefore"]

    count = keyword_match_count(text, keywords)

    if count >= 3:
        return 1.0
    elif count >= 1:
        return 0.7
    return 0.4


def problem_solving_score(text):
    if contains_any(text, ["solution", "approach"]):
        return 1.0
    return length_score(text, threshold=10)


def decision_score(text):
    if contains_any(text, ["consider", "analyze"]):
        return 1.0
    elif contains_any(text, ["try"]):
        return 0.7
    return 0.4


def calculate_aptitude_score(text):
    structure = detect_structure(text)
    problem = problem_solving_score(text)
    decision = decision_score(text)

    final = (
        structure * 0.35 +
        problem * 0.35 +
        decision * 0.30
    )

    return {
        "aptitude_score": round(final * 100, 2),
        "breakdown": {
            "structure": round(structure, 2),
            "problem_solving": round(problem, 2),
            "decision_making": round(decision, 2)
        }
    }


