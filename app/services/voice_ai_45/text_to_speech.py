import os
import time
import asyncio
import random
import traceback
import threading

import edge_tts
from pydub import AudioSegment
from pydub.playback import play


class TextToSpeechEngine:

    def __init__(self):

        self.base_dir = os.getcwd()

        self.output_dir = os.path.join(
            self.base_dir,
            "data",
            "raw",
            "questions_45",
        )

        os.makedirs(
            self.output_dir,
            exist_ok=True,
        )

        self.hr_voices = {
            "senior_female": "en-IN-NeerjaNeural",
            "senior_male": "en-IN-PrabhatNeural",
            "modern_female": "en-IN-AnanyaNeural",
            "default": "en-IN-NeerjaNeural",
        }

        print("✅ TextToSpeechEngine Ready")

    def make_natural_script(self, text):

        intro = [
            "Alright.",
            "Moving on.",
            "Great.",
            "Next question.",
            "Tell me.",
        ]

        outro = [
            "Take your time.",
            "Please explain.",
            "Share examples.",
            "Could you elaborate?",
        ]

        return f"{random.choice(intro)} " f"{text} " f"{random.choice(outro)}"

    async def _generate(
        self,
        text,
        output_path,
        voice,
    ):

        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
            rate="-10%",
            pitch="-2Hz",
        )

        await communicate.save(output_path)

    def run_async(
        self,
        coro,
    ):

        result = {"error": None}

        def runner():

            loop = None

            try:

                loop = asyncio.new_event_loop()

                asyncio.set_event_loop(loop)

                loop.run_until_complete(coro)

            except Exception as e:

                result["error"] = e

            finally:

                try:

                    if loop:
                        loop.close()

                except Exception:
                    pass

        thread = threading.Thread(
            target=runner,
            daemon=True,
        )

        thread.start()

        thread.join()

        if result["error"]:

            raise result["error"]

    def wait_for_audio(
        self,
        path,
        timeout=20,
    ):

        start = time.time()

        while time.time() - start < timeout:

            if os.path.exists(path) and os.path.getsize(path) > 1024:
                return True

            time.sleep(0.5)

        return False

    def play_audio(
        self,
        audio_path,
    ):

        def player():

            try:

                audio = AudioSegment.from_file(audio_path)

                pause = AudioSegment.silent(duration=300)

                play(pause + audio + pause)

            except Exception as e:

                print(f"Playback Error: {e}")

        threading.Thread(
            target=player,
            daemon=True,
        ).start()

    def generate_audio(
        self,
        text,
        filename="question.mp3",
        interviewer_type="senior_female",
        autoplay=True,
    ):

        try:

            if not text:

                raise ValueError("Empty text")

            natural_text = self.make_natural_script(text)

            voice = self.hr_voices.get(
                interviewer_type,
                self.hr_voices["default"],
            )

            unique_name = f"{int(time.time())}_" f"{filename}"

            output = os.path.join(
                self.output_dir,
                unique_name,
            )

            print("\n===== TTS =====")

            print(f"Voice: {voice}")

            self.run_async(
                self._generate(
                    natural_text,
                    output,
                    voice,
                )
            )

            if not self.wait_for_audio(output):

                raise TimeoutError("Audio timeout")

            print("✅ Audio Generated")

            if autoplay:

                self.play_audio(output)

            return output

        except Exception as e:

            print("\n❌ TTS FAILED")

            print(str(e))

            print(traceback.format_exc())

            return None


if __name__ == "__main__":

    tts = TextToSpeechEngine()

    result = tts.generate_audio("Explain your backend architecture.")

    print(result)
