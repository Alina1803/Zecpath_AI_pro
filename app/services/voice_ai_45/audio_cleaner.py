import os
import traceback

from pydub import AudioSegment


class AudioCleaner:

    def normalize_audio(self,input_path,output_path=None):

        try:

            print("\n=================================")
            print("AUDIO NORMALIZATION STARTED")
            print("=================================")

            # ======================================
            # VALIDATE INPUT
            # ======================================

            if input_path is None:

                raise ValueError("input_path is None")

            input_path = os.path.abspath(input_path)

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
            # CHECK INPUT EXISTS
            # ======================================

            if not os.path.exists(input_path):

                raise FileNotFoundError(f"Input file not found: {input_path}")

            file_size = os.path.getsize(input_path)

            print(f"Input Size : {file_size} bytes")

            if file_size <= 100:

                raise Exception("Input audio file is empty")

            audio = AudioSegment.from_file(input_path)

            normalized_audio = audio.normalize()
            boosted_audio = normalized_audio + 10

            boosted_audio.export(
                output_path,
                format="wav")

            # ======================================
            # VERIFY OUTPUT
            # ======================================

            if not os.path.exists(output_path):

                raise FileNotFoundError(
                    f"Normalized output missing: {output_path}")

            output_size = os.path.getsize(output_path)

            print(f"Output Size : {output_size} bytes")

            if output_size <= 100:

                raise Exception("Normalized output file corrupted")

            print("\n=================================")
            print("AUDIO NORMALIZATION SUCCESS")
            print("=================================")

            return output_path

        except Exception as e:

            print("\n=================================")
            print("AUDIO CLEANING FAILED")
            print("=================================")

            print(f"Error : {str(e)}")

            print("\nTRACEBACK:\n")

            print(traceback.format_exc())

            # fallback to original audio
            return input_path