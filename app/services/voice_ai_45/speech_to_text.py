import speech_recognition as sr

class SpeechToTextEngine:

    def __init__(self):

        self.recognizer = (
            sr.Recognizer()
        )

    def transcribe_audio(
        self,
        audio_path
    ):

        try:

            with sr.AudioFile(
                audio_path
            ) as source:

                audio = (
                    self.recognizer.record(
                        source
                    )
                )

            text = (
                self.recognizer
                .recognize_google(audio)
            )

            return text

        except sr.UnknownValueError:

            return (
                "Speech could not "
                "be understood"
            )

        except sr.RequestError as e:

            return (
                f"Speech API Error: {e}"
            )

        except Exception as e:

            return (
                f"STT Error: {str(e)}"
            )