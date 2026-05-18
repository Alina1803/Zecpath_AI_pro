import os
import traceback
import whisper
import wave

class SpeechToTextEngine:

    def __init__(
        self,
        model_name="base"):

        try:

            print("\n=================================")

            print("LOADING WHISPER MODEL")
            print("=================================")

            self.model = whisper.load_model(
                model_name)

            print(
                f"Model Loaded : {model_name}")

        except Exception as e:

            print(
                "\nWHISPER MODEL LOAD FAILED")

            print(str(e))

            raise e

    # =====================================================
    # AUDIO VALIDATION
    # =====================================================

    def validate_audio(
        self,
        audio_path):

        try:

            with wave.open(
                audio_path,
                "rb"
            ) as wav_file:

                channels = wav_file.getnchannels()

                sample_width = (
                    wav_file.getsampwidth())

                frame_rate = (
                    wav_file.getframerate())

                frames = (
                    wav_file.getnframes())

                duration = (
                    frames / float(frame_rate))

                print("\n=================================")
                print("AUDIO INFO")
                print("=================================")

                print(f"Channels     : {channels}")

                print(
                    f"Sample Width : {sample_width}")

                print(
                    f"Frame Rate   : {frame_rate}")

                print(f"Frames        : {frames}")

                print(
                    f"Duration      : "
                    f"{round(duration, 2)} sec")

                if duration < 1:

                    print(
                        "\nWARNING: Audio too short")

        except Exception as e:

            print(
                f"\nAudio Validation Failed: {e}")

    # =====================================================
    # TRANSCRIBE AUDIO
    # =====================================================

    def transcribe(
        self,
        audio_path):

        try:

            print("\n=================================")
            print("STARTING SPEECH TO TEXT")
            print("=================================")

            # =================================================
            # VALIDATE INPUT
            # =================================================

            if audio_path is None:

                raise ValueError(
                    "audio_path is None")

            if not isinstance(
                audio_path,
                str):

                raise TypeError(
                    f"Expected string path, "
                    f"got {type(audio_path)}")

            # =================================================
            # ABSOLUTE PATH
            # =================================================

            audio_path = os.path.abspath(
                audio_path)

            print(
                f"Audio Path : {audio_path}")

            # =================================================
            # FILE EXISTS
            # =================================================

            if not os.path.exists(
                audio_path):

                raise FileNotFoundError(
                    f"Audio file not found:\n"
                    f"{audio_path}")

            # =================================================
            # FILE SIZE
            # =================================================

            file_size = os.path.getsize(
                audio_path)

            print(
                f"File Size : {file_size} bytes")

            if file_size <= 100:

                raise Exception(
                    "Audio file empty/corrupted")

            # =================================================
            # AUDIO VALIDATION
            # =================================================

            self.validate_audio(
                audio_path)

            # =================================================
            # TRANSCRIBE
            # =================================================

            print("\nTranscribing audio...")

            result = self.model.transcribe(

                audio_path,

                fp16=False,

                language="en")

            # =================================================
            # RAW RESULT DEBUG
            # =================================================

            print("\n=================================")
            print("RAW WHISPER OUTPUT")
            print("=================================")

            segments = result.get(
                "segments",
                []
            )

            if segments:

                for segment in segments:

                    print(
                        f"[{segment['start']:.2f}s "
                        f"-> "
                        f"{segment['end']:.2f}s]")

                    print(segment["text"])

            else:

                print("No segments detected")

            # =================================================
            # FINAL TEXT
            # =================================================

            transcript = result.get(
                "text",
                ""
            ).strip()

            # =================================================
            # EMPTY CHECK
            # =================================================

            if not transcript:

                print("\nWARNING: Empty transcript generated")

                print("\nPossible Causes:")

                print("- silent microphone")

                print("- low microphone volume")

                print("- unsupported audio")

                print("- noisy environment")

                print("- wrong recording device")

            # =================================================
            # SUCCESS
            # =================================================

            print("\n=================================")
            print("TRANSCRIPTION SUCCESS")
            print("=================================")

            print(f"Transcript :\n{transcript}")

            return transcript

        except Exception as e:

            print("\n=================================")
            print("STT FAILED")
            print("=================================")

            print(f"Error : {str(e)}")

            print("\nTRACEBACK:\n")

            print(traceback.format_exc())

            return None