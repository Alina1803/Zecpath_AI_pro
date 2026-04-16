def generate_ca_questions():
    skills = ["GST", "Income Tax", "Audit"]
    questions = []

    for skill in skills:
        questions.append(f"Do you have experience in {skill}?")

    return questions