def fallback_response(error_type="general"):
    if error_type == "validation":
        return "Invalid input. Please try again."
    elif error_type == "audio":
        return "Audio not clear. Please retry."
    elif error_type == "ai":
        return "System error. Please try again later."

    return "Something went wrong. Try again."