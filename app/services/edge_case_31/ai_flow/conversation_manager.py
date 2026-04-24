from app.services.edge_case_31.validation.input_validator import validate_input
from app.services.edge_case_31.validation.language_detector import detect_language
from app.services.edge_case_31.ai_flow.retry_handler import retry_process
from app.services.edge_case_31.ai_flow.clarification_engine import clarify_response
from app.services.edge_case_31.ai_flow.fallback_handler import fallback_response
from app.services.edge_case_31.logging.error_logger import log_error
from app.services.edge_case_31.logging.monitoring import track_failure


def process_user_input(user_input, ai_function):

    # ✅ Step 1: Structured Validation (NEW LOGIC)
    result = validate_input(user_input)

    # ❌ If rejected → stop everything
    if result.get("status") == "Rejected":
        log_error("ValidationError", "Empty input")
        track_failure()
        return result

    # 🟡 If issues exist → return directly (skip AI)
    if result.get("issues_detected"):
        return result

    # ✅ Step 2: Continue old pipeline for valid input
    language = detect_language(user_input)

    try:
        response = retry_process(ai_function, user_input)
        response = clarify_response(response)

        return {
            "input": user_input,
            "issues_detected": [],
            "status": "Processed",
            "ai_response": response,
            "language": language
        }

    except Exception as e:
        log_error("ProcessingError", str(e))
        track_failure()
        return fallback_response("ai")