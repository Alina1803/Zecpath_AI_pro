import os
import traceback

from pydub import AudioSegment
from pydub.effects import normalize
from pydub.silence import detect_nonsilent


class AudioCleaner:

    def __init__(self):

        self.target_sample_rate = 16000

        self.min_duration = 0.8

    # =====================================================
    # REMOVE SILENCE (LESS AGGRESSIVE)
    # =====================================================

    def remove_silence(self, audio):

        try:

            original_duration = len(audio)

            ranges = detect_nonsilent(
                audio,
                min_silence_len=800,
                silence_thresh=max(
                    audio.dBFS - 25,
                    -45,
                ),
            )

            if not ranges:

                print("No speech detected")

                return audio

            cleaned = AudioSegment.empty()

            padding = 250

            for start, end in ranges:

                start = max(
                    0,
                    start - padding,
                )

                end = min(
                    len(audio),
                    end + padding,
                )

                cleaned += audio[start:end]

            if len(cleaned) < (original_duration * 0.50):

                print("Too much removed → keeping original")

                return audio

            return cleaned

        except Exception:

            return audio

    # =====================================================
    # SMART BOOST
    # =====================================================

    def smart_volume_boost(
        self,
        audio,
    ):

        try:

            db = audio.dBFS

            print(f"Current Audio dBFS : {db}")

            if db < -35:

                return audio + 18

            elif db < -28:

                return audio + 12

            elif db < -22:

                return audio + 8

            elif db < -18:

                return audio + 5

            return audio

        except Exception:

            return audio

    # =====================================================
    # NOISE REDUCTION
    # =====================================================

    def reduce_noise(
        self,
        audio,
    ):

        try:

            audio = audio.high_pass_filter(80)

            audio = audio.low_pass_filter(7500)

            return audio

        except Exception:

            return audio

    # =====================================================
    # MONO
    # =====================================================

    def convert_to_mono(
        self,
        audio,
    ):

        try:

            return audio.set_channels(1)

        except Exception:

            return audio

    # =====================================================
    # RESAMPLE
    # =====================================================

    def resample_audio(
        self,
        audio,
    ):

        try:

            return audio.set_frame_rate(self.target_sample_rate)

        except Exception:

            return audio

    # =====================================================
    # VALIDATE
    # =====================================================

    def validate_audio(
        self,
        audio,
    ):

        try:

            duration = len(audio) / 1000

            print(f"Audio Duration : {duration}")

            if duration < self.min_duration:

                print("Short audio accepted")

                return True

            if audio.rms < 50:

                print("Low RMS accepted")

                return True

            return True

        except Exception:

            return True

    # =====================================================
    # MAIN
    # =====================================================

    def normalize_audio(
        self,
        input_path,
        output_path=None,
    ):

        try:

            print("\n=================================")
            print("SMART AUDIO CLEANING STARTED")
            print("=================================")

            if not input_path:

                raise ValueError("input_path missing")

            input_path = os.path.abspath(input_path)

            if output_path is None:

                output_path = input_path.replace(
                    ".wav",
                    "_cleaned.wav",
                )

            audio = AudioSegment.from_file(input_path)

            print(f"Duration : {len(audio)/1000}")

            audio = self.convert_to_mono(audio)

            audio = self.resample_audio(audio)

            audio = self.reduce_noise(audio)

            audio = self.remove_silence(audio)

            audio = normalize(audio)

            audio = self.smart_volume_boost(audio)

            self.validate_audio(audio)

            audio.export(
                output_path,
                format="wav",
            )

            print("\n✅ AUDIO CLEAN SUCCESS")

            return output_path

        except Exception as e:

            print("\n⚠ AUDIO CLEAN FAILED")

            print(str(e))

            print(traceback.format_exc())

            return input_path
