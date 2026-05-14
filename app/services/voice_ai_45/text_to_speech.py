import os

from gtts import gTTS

class TextToSpeechEngine:

    def __init__(self):

        os.makedirs(
            "data/raw/Audios",
            exist_ok=True)

    def generate_audio(
        self,
        text,
        filename="question.mp3"):

        try:

            save_path = os.path.join(
                "data/raw/Audios",
                filename)

            tts = gTTS(
                text=text,
                lang="en")

            tts.save(save_path)

            print(f"Audio Saved: "
                f"{save_path}")

            return save_path

        except Exception as e:

            print(f"TTS Error: {e}")

            return None