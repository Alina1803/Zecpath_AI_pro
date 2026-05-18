import os
import time
import traceback

import pyttsx3


class TextToSpeechEngine:

    def __init__(self):

        # ==========================================
        # AUDIO DIRECTORY
        # ==========================================

        self.audio_dir = "data/raw/Audios"

        os.makedirs(self.audio_dir,
            exist_ok=True)

        # ==========================================
        # INIT ENGINE
        # ==========================================

        self.engine = pyttsx3.init()

        self.engine.setProperty(
            "rate",
            160)

        self.engine.setProperty(
            "volume",
            1.0)

        print("\nTTS Engine Initialized")

    # ==============================================
    # GENERATE AUDIO
    # ==============================================

    def generate_audio(
        self,
        text,
        filename=None,
        auto_play=True):

        try:

            # ======================================
            # VALIDATE INPUT
            # ======================================

            if text is None:

                raise ValueError(
                    "TTS text is None")

            text = str(text).strip()

            if text == "":

                raise ValueError(
                    "TTS text is empty")

            # ======================================
            # AUTO GENERATE FILENAME
            # ======================================

            if filename is None:

                timestamp = int(time.time())

                filename = f"tts_{timestamp}.wav"

            # ======================================
            # ENSURE WAV EXTENSION
            # ======================================

            if not filename.endswith(".wav"):

                filename += ".wav"

            # ======================================
            # ABSOLUTE SAVE PATH
            # ======================================

            save_path = os.path.abspath(
                os.path.join(
                    self.audio_dir,
                    filename)
            )

            print("\n=================================")
            print("OFFLINE TTS STARTED")
            print("=================================")

            print(f"Text Length : {len(text)}")
            print(f"Filename    : {filename}")
            print(f"Save Path   : {save_path}")

            # ======================================
            # CLEAR ENGINE QUEUE
            # ======================================

            self.engine.stop()

            # ======================================
            # SAVE AUDIO FILE FIRST
            # ======================================

            print("\nGenerating audio file...")

            self.engine.save_to_file(
                text,
                save_path)

            self.engine.runAndWait()

            # ======================================
            # VERIFY FILE EXISTS
            # ======================================

            if not os.path.exists(save_path):

                raise FileNotFoundError(
                    f"TTS file not generated: {save_path}")

            # ======================================
            # VERIFY FILE SIZE
            # ======================================

            file_size = os.path.getsize(
                save_path)

            print(f"Generated File Size : {file_size} bytes")

            if file_size <= 100:

                raise Exception(
                    "Generated TTS file is empty")

            # ======================================
            # OPTIONAL LIVE SPEAK
            # ======================================

            if auto_play:

                print("\nPlaying generated speech...")

                self.engine.say(text)

                self.engine.runAndWait()

            print("\n=================================")
            print("TTS SUCCESS")
            print("=================================")

            print(f"Saved At : {save_path}")

            return save_path

        except Exception as e:

            print("\n=================================")
            print("OFFLINE TTS FAILED")
            print("=================================")

            print(f"Error : {str(e)}")

            print("\nTRACEBACK:\n")

            print(traceback.format_exc())

            return None