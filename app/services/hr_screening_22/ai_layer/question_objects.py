def build_question_object(q):
    return {
        "id": q["question_id"],
        "text": q["question"],
        "type": q["answer_type"],
        "mandatory": q["mandatory"]
    }