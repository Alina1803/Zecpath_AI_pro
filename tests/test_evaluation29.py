from app.services.ai_conversation_system_29.evaluation.evaluator import evaluate_answer

def test_good():
    assert evaluate_answer("This is a very long detailed answer explaining the concept clearly") == "good"