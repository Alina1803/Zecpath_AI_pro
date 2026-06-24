class EmotionDetector:

    def __init__(self):

        self.supported = [
            "happy",
            "neutral",
            "confident",
            "nervous",
        ]

    @staticmethod
    def detect(transcript=""):

        detector = EmotionDetector()

        return detector.analyze(
            transcript
        )

    def analyze(
        self,
        transcript,
    ):

        transcript = str(
            transcript
        ).lower()

        if "confident" in transcript:

            emotion = "confident"

        elif "happy" in transcript:

            emotion = "happy"

        elif len(transcript) < 20:

            emotion = "nervous"

        else:

            emotion = "neutral"

        return {

            "emotion": emotion,

            "confidence": 0.92,

            "status": "success",

        }