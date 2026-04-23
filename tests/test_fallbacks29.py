from app.services.ai_conversation_system_29.flows.fallback_handler import fallback_response


def test_fallback():
    assert fallback_response(1) is not None