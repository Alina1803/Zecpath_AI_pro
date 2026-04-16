def run_interview(questions):
    answers = {}

    for q in questions:
        ans = input(q["question"] + " : ")
        answers[q["question_id"]] = ans

    return answers