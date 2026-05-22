import os
import traceback
from pydub import AudioSegment
from pydub.effects import normalize
from pydub.silence import detect_nonsilent


class AudioCleaner:

    def __init__(self):

        self.target_sample_rate = 16000

    # =====================================================
    # REMOVE SILENCE
    # =====================================================

    def remove_silence(self, audio):

        try:

            non_silent_ranges = detect_nonsilent(
                audio,
                min_silence_len=400,
                silence_thresh=audio.dBFS - 16
            )

            if not non_silent_ranges:
                return audio

            cleaned_audio = AudioSegment.empty()

            for start, end in non_silent_ranges:

                cleaned_audio += audio[start:end]

            return cleaned_audio

        except:
            return audio

    # =====================================================
    # BOOST LOW AUDIO
    # =====================================================

    def smart_volume_boost(self, audio):

        try:

            current_dbfs = audio.dBFS

            print(f"Current Audio dBFS : {current_dbfs}")

            # ==========================================
            # VERY LOW AUDIO
            # ==========================================

            if current_dbfs < -35:

                print("Applying +25 dB Boost")

                return audio + 25

            elif current_dbfs < -28:

                print("Applying +18 dB Boost")

                return audio + 18

            elif current_dbfs < -22:

                print("Applying +12 dB Boost")

                return audio + 12

            elif current_dbfs < -18:

                print("Applying +8 dB Boost")

                return audio + 8

            return audio

        except:
            return audio

    # =====================================================
    # NOISE REDUCTION
    # =====================================================

    def reduce_noise(self, audio):

        try:

            # ==========================================
            # SIMPLE LOW PASS FILTER
            # ==========================================

            audio = audio.low_pass_filter(7500)

            # ==========================================
            # REMOVE LOW HUM
            # ==========================================

            audio = audio.high_pass_filter(80)

            return audio

        except:
            return audio

    # =====================================================
    # CONVERT TO MONO
    # =====================================================

    def convert_to_mono(self, audio):

        try:

            if audio.channels > 1:

                print("Converting Stereo To Mono")

                audio = audio.set_channels(1)

            return audio

        except:
            return audio

    # =====================================================
    # RESAMPLE AUDIO
    # =====================================================

    def resample_audio(self, audio):

        try:

            if audio.frame_rate != self.target_sample_rate:

                print(
                    f"Resampling Audio : "
                    f"{audio.frame_rate} -> "
                    f"{self.target_sample_rate}"
                )

                audio = audio.set_frame_rate(
                    self.target_sample_rate
                )

            return audio

        except:
            return audio

    # =====================================================
    # VALIDATE AUDIO
    # =====================================================

    def validate_audio(self, audio):

        try:

            duration_sec = len(audio) / 1000

            print(f"Audio Duration : {duration_sec} sec")

            if duration_sec < 1:

                raise Exception(
                    "Audio duration too short"
                )

            if audio.rms <= 0:

                raise Exception(
                    "Audio contains no signal"
                )

            return True

        except Exception as e:

            print(f"Validation Failed : {e}")

            return False

    # =====================================================
    # MAIN NORMALIZATION
    # =====================================================

    def normalize_audio(

        self,

        input_path,

        output_path=None
    ):

        try:

            print("\n=================================")
            print("SMART AUDIO CLEANING STARTED")
            print("=================================")

            # ======================================
            # VALIDATE INPUT
            # ======================================

            if input_path is None:

                raise ValueError(
                    "input_path is None"
                )

            input_path = os.path.abspath(
                input_path
            )

            print(f"Input File : {input_path}")

            # ======================================
            # AUTO OUTPUT PATH
            # ======================================

            if output_path is None:

                output_path = input_path.replace(
                    ".wav",
                    "_cleaned.wav"
                )

            output_path = os.path.abspath(
                output_path
            )

            print(f"Output File : {output_path}")

            # ======================================
            # FILE CHECK
            # ======================================

            if not os.path.exists(input_path):

                raise FileNotFoundError(
                    f"Input file not found: "
                    f"{input_path}"
                )

            input_size = os.path.getsize(
                input_path
            )

            print(
                f"Input Size : "
                f"{input_size} bytes"
            )

            if input_size <= 100:

                raise Exception(
                    "Input audio file empty"
                )

            # ======================================
            # LOAD AUDIO
            # ======================================

            audio = AudioSegment.from_file(
                input_path
            )

            print("\n=================================")
            print("ORIGINAL AUDIO INFO")
            print("=================================")

            print(f"Channels    : {audio.channels}")
            print(f"Frame Rate  : {audio.frame_rate}")
            print(f"Sample Width: {audio.sample_width}")
            print(f"Duration    : {len(audio)/1000} sec")
            print(f"dBFS        : {audio.dBFS}")

            # ======================================
            # PROCESSING PIPELINE
            # ======================================

            audio = self.convert_to_mono(audio)

            audio = self.resample_audio(audio)

            audio = self.reduce_noise(audio)

            audio = self.remove_silence(audio)

            audio = normalize(audio)

            audio = self.smart_volume_boost(audio)

            # ======================================
            # FINAL VALIDATION
            # ======================================

            if not self.validate_audio(audio):

                raise Exception(
                    "Processed audio invalid"
                )

            # ======================================
            # EXPORT
            # ======================================

            audio.export(
                output_path,
                format="wav"
            )

            # ======================================
            # VERIFY OUTPUT
            # ======================================

            if not os.path.exists(output_path):

                raise FileNotFoundError(
                    "Output file missing"
                )

            output_size = os.path.getsize(
                output_path
            )

            print(
                f"Output Size : "
                f"{output_size} bytes"
            )

            if output_size <= 100:

                raise Exception(
                    "Output audio corrupted"
                )

            print("\n=================================")
            print("SMART AUDIO CLEANING SUCCESS")
            print("=================================")

            return output_path

        except Exception as e:

            print("\n=================================")
            print("AUDIO CLEANING FAILED")
            print("=================================")

            print(f"Error : {str(e)}")

            print("\nTRACEBACK:\n")

            print(traceback.format_exc())

            # ======================================
            # FALLBACK
            # ======================================

            print(
                "\n⚠ Returning Original Audio"
            )

            return input_path