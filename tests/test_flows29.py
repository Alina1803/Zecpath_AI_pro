from app.services.ai_conversation_system_29.flows.decision_tree import decide_next_step

def test_silence():
    assert decide_next_step("") == "handle_silence"

def test_short():
    assert decide_next_step("hi") == "short_answer"