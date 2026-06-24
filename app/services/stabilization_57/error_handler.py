import traceback


class ErrorHandler:
    @staticmethod
    def execute(func):
        try:
            return func()
        except Exception as exc:
            print("\nERROR")
            print(str(exc))
            print(traceback.format_exc())
            return None

    @staticmethod
    def safe_run(func, retries=3):
        for _ in range(retries):
            result = ErrorHandler.execute(func)

            if result is not None:
                return result

        return None
