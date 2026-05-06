def generate_explanation(score):
    explanation = {
        "ats": "Skill match evaluation",
        "screening": "Response clarity and relevance",
        "hr": "Confidence and communication"
    }

    return {
        "final_score": score,
        "explanation": explanation
    }