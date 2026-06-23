import os
import re
import wave
import traceback
import logging

import numpy as np
from faster_whisper import WhisperModel

logger = logging.getLogger(__name__)

_WHISPER_MODEL = None


class SpeechToTextEngine:

    def __init__(
        self,
        model_name="base",
        device="cpu",
        compute_type="int8",
    ):

        global _WHISPER_MODEL

        self.model = None

        try:

            print("\n=================================")
            print("LOADING FASTER WHISPER")
            print("=================================")

            cache = r"E:\hf_cache"

            os.makedirs(
                cache,
                exist_ok=True,
            )

            os.environ["HF_HOME"] = cache
            os.environ["HUGGINGFACE_HUB_CACHE"] = cache
            os.environ["HF_HUB_DISABLE_SYMLINKS"] = "1"

            if _WHISPER_MODEL:

                self.model = _WHISPER_MODEL

                print("✅ Using Cached Model")

                return

            candidates = [
                model_name,
                "base",
                "tiny",
            ]

            for name in candidates:

                try:

                    print(f"Trying Model → {name}")

                    self.model = WhisperModel(
                        name,
                        device=device,
                        compute_type=compute_type,
                        download_root=cache,
                    )

                    _WHISPER_MODEL = self.model

                    print(f"✅ Loaded → {name}")

                    break

                except Exception as e:

                    print(f"❌ Failed → {name}")

                    print(str(e))

            print("✅ SpeechToTextEngine Ready")

        except Exception:

            print(traceback.format_exc())

            self.model = None

    # =========================================

    def validate_audio(
        self,
        audio_path,
    ):

        try:

            with wave.open(
                audio_path,
                "rb",
            ) as wf:

                rate = wf.getframerate()

                frames = wf.getnframes()

                duration = frames / rate

                raw = wf.readframes(frames)

            audio = np.frombuffer(
                raw,
                dtype=np.int16,
            )

            energy = float(np.abs(audio).mean())

            print(f"Duration={duration}")

            print(f"Energy={energy}")

            if duration < 0.6:

                print("⚠ Too Short")

                return False

            if energy < 80:

                print("⚠ Very Low Energy")

                return False

            return True

        except Exception:

            return False

    # =========================================

    def clean_transcript(
        self,
        text,
    ):

        try:

            text = re.sub(
                r"\s+",
                " ",
                str(text),
            )

            words = text.split()

            out = []

            prev = ""

            repeat = 0

            for w in words:

                lw = w.lower()

                if lw == prev:

                    repeat += 1

                else:

                    repeat = 0

                if repeat < 2:

                    out.append(w)

                prev = lw

            return " ".join(out).strip()

        except Exception:

            return text

    # =========================================

    def is_invalid_response(
        self,
        text,
    ):

        if not text:

            return True

        text = text.lower()

        blocked = [
            "subscribe",
            "youtube",
            "background music",
            "test test",
        ]

        if any(x in text for x in blocked):

            return True

        return False

    # =========================================

    def transcribe(
        self,
        audio_path,
    ):

        try:

            if not self.model:

                return ""

            if not audio_path:

                return ""

            audio_path = os.path.abspath(audio_path)

            if not os.path.exists(audio_path):

                return ""

            if not self.validate_audio(audio_path):

                return ""

            print("Transcribing...")

            segments, info = self.model.transcribe(
                audio_path,
                language="en",
                beam_size=3,
                best_of=3,
                temperature=0,
                vad_filter=True,
                vad_parameters={"min_silence_duration_ms": 600},
                condition_on_previous_text=False,
                compression_ratio_threshold=2.4,
                no_speech_threshold=0.45,
            )

            text = " ".join(seg.text for seg in segments).strip()

            text = self.clean_transcript(text)

            print(f"Detected={info.language}")

            print(f"Transcript={text}")

            if self.is_invalid_response(text):

                return ""

            return text

        except Exception:

            print(traceback.format_exc())

            return ""
