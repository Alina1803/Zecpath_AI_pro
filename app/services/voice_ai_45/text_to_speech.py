# app/services/voice_ai_45/text_to_speech.py

import os
import time
import asyncio
import traceback
import threading

import edge_tts
from pydub import AudioSegment
from pydub.playback import play


class TextToSpeechEngine:

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        self.output_dir = (
            "data/raw/questions_45"
        )

        os.makedirs(
            self.output_dir,
            exist_ok=True
        )

        # =============================================
        # NATURAL HR VOICES
        # =============================================

        self.hr_voices = {

            "female_hr": "en-IN-NeerjaNeural",

            "male_hr": "en-IN-PrabhatNeural",

            "default": "en-IN-NeerjaNeural"
        }

        self.default_voice = (
            self.hr_voices[
                "default"
            ]
        )

        print(
            "✅ Natural TTS Engine Ready"
        )

    # =====================================================
    # NATURAL QUESTION FORMATTER
    # =====================================================

    def make_natural_script(
        self,
        text
    ):

        text = str(text).strip()

        # =============================================
        # HUMAN-LIKE HR DELIVERY
        # =============================================

        text = (

            f"Alright. "

            f"{text} "

            f"Please explain with examples."
        )

        return text

    # =====================================================
    # ASYNC GENERATOR
    # =====================================================

    async def _generate(
        self,
        text,
        output_path,
        voice
    ):

        communicate = edge_tts.Communicate(

            text=text,

            voice=voice,

            rate="-12%",

            pitch="-4Hz"
        )

        await communicate.save(
            output_path
        )

    # =====================================================
    # SAFE ASYNC RUNNER
    # =====================================================

    def run_async(
        self,
        coro
    ):

        result = {}

        def runner():

            loop = asyncio.new_event_loop()

            asyncio.set_event_loop(loop)

            try:

                loop.run_until_complete(
                    coro
                )

                result["success"] = True

            except Exception as e:

                result["error"] = str(e)

            finally:

                loop.close()

        thread = threading.Thread(
            target=runner
        )

        thread.start()

        thread.join()

        if "error" in result:

            raise Exception(
                result["error"]
            )

    # =====================================================
    # WAIT FOR FILE
    # =====================================================

    def wait_for_audio(
        self,
        path,
        timeout=10
    ):

        start = time.time()

        while True:

            if os.path.exists(path):

                try:

                    size = os.path.getsize(
                        path
                    )

                    if size > 5000:

                        return True

                except:
                    pass

            if time.time() - start > timeout:

                return False

            time.sleep(0.2)

    # =====================================================
    # PLAY NATURAL AUDIO
    # =====================================================

    def play_audio(
        self,
        audio_path
    ):

        try:

            audio = AudioSegment.from_file(
                audio_path
            )

            # =========================================
            # SLIGHT HR PAUSE EFFECT
            # =========================================

            pause = AudioSegment.silent(
                duration=300
            )

            final_audio = (
                pause + audio + pause
            )

            play(final_audio)

        except Exception as e:

            print(
                f"Playback Error : {e}"
            )

    # =====================================================
    # GENERATE AUDIO
    # =====================================================

    def generate_audio(

        self,

        text,

        filename="question.mp3",

        interviewer_type="senior_recruiter"
    ):

        try:

            # =============================================
            # NATURAL HR SCRIPT
            # =============================================

            natural_text = (
                self.make_natural_script(
                    text
                )
            )

            # =============================================
            # UNIQUE FILE
            # =============================================

            filename = (

                f"{int(time.time())}_"
                f"{filename}"
            )

            output_path = os.path.join(

                self.output_dir,

                filename
            )

            voice = self.hr_voices.get(

                interviewer_type,

                self.default_voice
            )

            print("\n=================================")
            print("NATURAL AI HR VOICE")
            print("=================================")

            print(
                f"Voice : {interviewer_type}"
            )

            print(
                f"Speaking : {natural_text}"
            )

            # =============================================
            # GENERATE
            # =============================================

            self.run_async(

                self._generate(

                    text=natural_text,

                    output_path=output_path,

                    voice=voice
                )
            )

            # =============================================
            # WAIT
            # =============================================

            ready = self.wait_for_audio(
                output_path
            )

            if not ready:

                raise Exception(
                    "TTS generation timeout"
                )

            # =============================================
            # NATURAL PLAYBACK
            # =============================================

            print(
                "\n🔊 AI HR Speaking..."
            )

            self.play_audio(
                output_path
            )

            print(
                "✅ HR Question Completed"
            )

            return output_path

        except Exception as e:

            print("\n=================================")
            print("NATURAL TTS FAILED")
            print("=================================")

            print(str(e))
            print(traceback.format_exc())

            return None