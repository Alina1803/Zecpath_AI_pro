def clarify_response(response):
    if not response or len(response.strip()) < 5:
        return "Could you please provide more details?"
    return response