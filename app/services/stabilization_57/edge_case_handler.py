class EdgeCaseHandler:
    @staticmethod
    def validate(result):
        if result is None:
            return False

        if result == "":
            return False

        return True

    @staticmethod
    def validate_transcript(text):
        if not text:
            return False

        if len(text.strip()) < 3:
            return False

        return True

    @staticmethod
    def validate_audio(size):
        return size > 10000
