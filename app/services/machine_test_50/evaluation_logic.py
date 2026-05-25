# --------------------------------------
# Correctness Score
# --------------------------------------

def correctness_score(passed, total):

    if total == 0:
        return 0

    return passed / total


# --------------------------------------
# Efficiency Score
# --------------------------------------

def efficiency_score(runtime):

    if runtime < 1:
        return 1.0

    elif runtime < 2:
        return 0.7

    return 0.4


# --------------------------------------
# Code Quality Score
# --------------------------------------

def code_quality_score(code):

    lines = len(code.splitlines())

    if lines < 20:
        return 1.0

    elif lines < 50:
        return 0.7

    return 0.4


# --------------------------------------
# Problem Solving Score
# --------------------------------------

def problem_solving_score(attempts):

    if attempts == 1:
        return 1.0

    elif attempts <= 3:
        return 0.7

    return 0.4


# --------------------------------------
# Final Task Score
# --------------------------------------

def calculate_task_score(
    passed,
    total,
    runtime,
    code,
    attempts
):

    correctness = correctness_score(
        passed,
        total
    )

    efficiency = efficiency_score(runtime)

    quality = code_quality_score(code)

    problem = problem_solving_score(attempts)

    final = (

        correctness * 0.4 +

        efficiency * 0.2 +

        quality * 0.2 +

        problem * 0.2
    )

    return {

        "task_score": round(final * 100, 2),

        "breakdown": {

            "correctness": round(correctness, 2),

            "efficiency": round(efficiency, 2),

            "code_quality": round(quality, 2),

            "problem_solving": round(problem, 2)
        }
    }