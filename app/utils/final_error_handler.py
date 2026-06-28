def safe_execute(func):

    try:
        return func()

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e),
        }
