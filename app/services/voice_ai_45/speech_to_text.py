import os
import re
import wave
import traceback
import logging
import numpy as np

from faster_whisper import WhisperModel


logger = logging.getLogger(__name__)

# =====================================================
# GLOBAL MODEL CACHE
# =====================================================

_WHISPER_MODEL = None


# =====================================================
# SPEECH TO TEXT ENGINE
# =====================================================

class SpeechToTextEngine:

    # =================================================
    # INIT
    # =================================================

    def __init__(

        self,

        model_name="base",

        device="cpu",

        compute_type="int8"
    ):

        global _WHISPER_MODEL

        try:

            print("\n=================================")
            print("LOADING FASTER WHISPER MODEL")
            print("=================================")

            if _WHISPER_MODEL is None:

                print(
                    "Initializing Global Whisper Model..."
                )

                _WHISPER_MODEL = WhisperModel(

                    model_name,

                    device=device,

                    compute_type=compute_type
                )

                print(
                    f"✅ Model Loaded : {model_name}"
                )

            else:

                print(
                    "✅ Reusing Existing Whisper Model"
                )

            self.model = _WHISPER_MODEL

            print(
                "✅ SpeechToTextEngine Ready"
            )

        except Exception as e:

            print("\n=================================")
            print("WHISPER MODEL LOAD FAILED")
            print("=================================")

            print(str(e))
            print(traceback.format_exc())

            raise e

    # =================================================
    # INVALID RESPONSE FILTER
    # =================================================

    def is_invalid_response(

        self,

        transcript
    ):

        try:

            text = str(
                transcript
            ).lower().strip()

            # =========================================
            # EMPTY
            # =========================================

            if not text:

                return True

            # =========================================
            # BLOCKED PHRASES
            # =========================================

            blocked = [

                "i don't know",
                "i dont know",

                "what's going on",
                "whats going on",

                "i don't want to talk",
                "i dont want to talk",

                "subscribe",
                "thank you for watching",

                "background music",

                "be right back",
                "i'll be right back",

                "testing testing",

                "hello hello",

                "you you you",

                "check one two",

                "can you hear me"
            ]

            for item in blocked:

                if item in text:

                    print(
                        f"\n⚠ BLOCKED RESPONSE DETECTED : {item}"
                    )

                    return True

            # =========================================
            # VERY SHORT RESPONSE
            # =========================================

            words = text.split()

            if len(words) <= 1:

                print(
                    "\n⚠ VERY SHORT RESPONSE"
                )

                return True

            # =========================================
            # REPETITIVE SPEECH DETECTION
            # =========================================

            unique_words = len(set(words))

            repetition_ratio = (
                unique_words / max(len(words), 1)
            )

            print(
                f"Repetition Ratio : {repetition_ratio}"
            )

            if repetition_ratio < 0.30:

                print(
                    "\n⚠ REPETITIVE RESPONSE DETECTED"
                )

                return True

            # =========================================
            # SAME PHRASE REPEATED
            # =========================================

            repeated_patterns = re.findall(

                r"(.{3,40}?)\1{2,}",

                text
            )

            if repeated_patterns:

                print(
                    "\n⚠ REPEATED PHRASE DETECTED"
                )

                return True

            return False

        except Exception as e:

            print(
                f"\nInvalid Response Check Failed : {e}"
            )

            return False

    # =================================================
    # AUDIO VALIDATION
    # =================================================

    def validate_audio(

        self,

        audio_path
    ):

        try:

            with wave.open(
                audio_path,
                "rb"
            ) as wav_file:

                channels = (
                    wav_file.getnchannels()
                )

                sample_width = (
                    wav_file.getsampwidth()
                )

                frame_rate = (
                    wav_file.getframerate()
                )

                num_frames = (
                    wav_file.getnframes()
                )

                duration = (
                    num_frames / float(frame_rate)
                )

                print("\n=================================")
                print("AUDIO INFO")
                print("=================================")

                print(f"Channels     : {channels}")
                print(f"Sample Width : {sample_width}")
                print(f"Frame Rate   : {frame_rate}")
                print(f"Frames       : {num_frames}")
                print(f"Duration     : {duration} sec")

            # ==========================================
            # AUDIO ENERGY
            # ==========================================

            with wave.open(audio_path, "rb") as wf:

                frames = wf.readframes(
                    wf.getnframes()
                )

            audio = np.frombuffer(
                frames,
                dtype=np.int16
            )

            energy = np.abs(audio).mean()

            print(f"Audio Energy : {energy}")

            # ==========================================
            # SILENT AUDIO
            # ==========================================

            if energy < 150:

                print("\n⚠ SILENT AUDIO DETECTED")

                return False

            # ==========================================
            # WARNINGS
            # ==========================================

            if duration < 1:

                print(
                    "⚠ WARNING: Audio Too Short"
                )

            if frame_rate < 16000:

                print(
                    "⚠ WARNING: Low Sample Rate"
                )

            return True

        except Exception as e:

            print(f"\n⚠ Audio Validation Failed: {e}")

            print(traceback.format_exc())

            return False

    # =================================================
    # CLEAN TRANSCRIPT
    # =================================================

    def clean_transcript(

        self,

        transcript
    ):

        try:

            transcript = str(
                transcript
            ).strip()

            # ==========================================
            # REMOVE EXTRA SPACES
            # ==========================================

            transcript = re.sub(

                r"\s+",

                " ",

                transcript
            )

            # ==========================================
            # REMOVE DUPLICATE WORDS
            # ==========================================

            words = transcript.split()

            cleaned_words = []

            prev_word = None

            repeat_count = 0

            for word in words:

                current = word.lower()

                if current == prev_word:

                    repeat_count += 1

                else:

                    repeat_count = 0

                # ======================================
                # KEEP ONLY MAX 2 REPETITIONS
                # ======================================

                if repeat_count < 2:

                    cleaned_words.append(word)

                prev_word = current

            transcript = " ".join(
                cleaned_words
            )

            return transcript.strip()

        except:
            return transcript

    # =================================================
    # TRANSCRIBE AUDIO
    # =================================================

    def transcribe(

        self,

        audio_path
    ):

        try:

            print("\n=================================")
            print("STARTING SPEECH TO TEXT")
            print("=================================")

            # =============================================
            # INPUT VALIDATION
            # =============================================

            if audio_path is None:

                raise ValueError(
                    "audio_path is None"
                )

            if not isinstance(
                audio_path,
                str
            ):

                raise TypeError(

                    f"Expected string path, "
                    f"got {type(audio_path)}"
                )

            # =============================================
            # ABSOLUTE PATH
            # =============================================

            audio_path = os.path.abspath(
                audio_path
            )

            print(
                f"Audio Path : {audio_path}"
            )

            # =============================================
            # FILE EXISTS
            # =============================================

            if not os.path.exists(
                audio_path
            ):

                raise FileNotFoundError(

                    f"Audio File Not Found:\n"
                    f"{audio_path}"
                )

            # =============================================
            # FILE SIZE
            # =============================================

            file_size = os.path.getsize(
                audio_path
            )

            print(
                f"File Size : {file_size} bytes"
            )

            if file_size <= 100:

                raise Exception(
                    "Audio file empty/corrupted"
                )

            # =============================================
            # AUDIO VALIDATION
            # =============================================

            valid_audio = self.validate_audio(
                audio_path
            )

            if not valid_audio:

                return ""

            # =============================================
            # TRANSCRIBE
            # =============================================

            print("\nTranscribing Audio...")

            segments, info = self.model.transcribe(

                audio_path,

                beam_size=1,

                best_of=1,

                temperature=0.0,

                language="en",

                vad_filter=False,

                condition_on_previous_text=False,

                compression_ratio_threshold=2.4,

                log_prob_threshold=-1.0,

                no_speech_threshold=0.3
            )

            segments = list(segments)

            # =============================================
            # DEBUG SEGMENTS
            # =============================================

            transcript_parts = []

            print("\n=================================")
            print("RAW WHISPER OUTPUT")
            print("=================================")

            for segment in segments:

                text = segment.text.strip()

                print(

                    f"[{segment.start:.2f}s "
                    f"-> "
                    f"{segment.end:.2f}s]"
                )

                print(text)

                if text:

                    transcript_parts.append(text)

            # =============================================
            # FINAL TRANSCRIPT
            # =============================================

            transcript = " ".join(
                transcript_parts
            ).strip()

            transcript = self.clean_transcript(
                transcript
            )

            # =============================================
            # TRANSCRIPTION INFO
            # =============================================

            print("\n=================================")
            print("TRANSCRIPTION INFO")
            print("=================================")

            print(
                f"Detected Language : "
                f"{info.language}"
            )

            print(
                f"Language Probability : "
                f"{round(info.language_probability, 2)}"
            )

            # =============================================
            # EMPTY CHECK
            # =============================================

            if not transcript:

                print("\n⚠ EMPTY TRANSCRIPT")

                return ""

            # =============================================
            # INVALID RESPONSE CHECK
            # =============================================

            if self.is_invalid_response(
                transcript
            ):

                print("\n=================================")
                print("INVALID RESPONSE DETECTED")
                print("=================================")

                return "Invalid or unclear response detected."

            # =============================================
            # SUCCESS
            # =============================================

            print("\n=================================")
            print("TRANSCRIPTION SUCCESS")
            print("=================================")

            print(
                f"Transcript :\n{transcript}"
            )

            return transcript

        except Exception as e:

            print("\n=================================")
            print("STT FAILED")
            print("=================================")

            print(f"Error : {str(e)}")

            print("\nTRACEBACK:\n")

            print(traceback.format_exc())

            return ""