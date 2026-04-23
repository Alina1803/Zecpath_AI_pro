def retry_message(count):
    messages = [
        "Please answer the question.",
        "Try explaining in more detail.",
        "Final attempt before ending interview."
    ]
    return messages[min(count - 1, len(messages) - 1)]