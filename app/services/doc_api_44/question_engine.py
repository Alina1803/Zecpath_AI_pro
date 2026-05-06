def generate_questions(role_type: str):
    if role_type == "technical":
        return [
            "Tell me about yourself",
            "What are your strengths?",
            "Explain a project you worked on"
        ]
    return ["Why should we hire you?"]