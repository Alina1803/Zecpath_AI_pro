import os
import traceback

from pydub import AudioSegment


class WAVConverter:

    def convert_to_wav(self, input_file, output_file=None):

        try:

            print("\n=================================")
            print("WAV CONVERSION STARTED")
            print("=================================")

            # ======================================
            # VALIDATE INPUT
            # ======================================

            if input_file is None:

                raise ValueError("input_file is None")

            input_file = os.path.abspath(input_file)

            print(f"Input File : {input_file}")

            # ======================================
            # AUTO OUTPUT FILE
            # ======================================

            if output_file is None:

                if input_file.endswith(".wav"):

                    output_file = input_file.replace(".wav", "_converted.wav")

                else:

                    output_file = input_file + ".wav"

            output_file = os.path.abspath(output_file)

            print(f"Output File : {output_file}")

            # ======================================
            # CHECK INPUT EXISTS
            # ======================================

            if not os.path.exists(input_file):

                raise FileNotFoundError(f"Input file not found: {input_file}")

            # ======================================
            # CHECK INPUT SIZE
            # ======================================

            file_size = os.path.getsize(input_file)

            print(f"Input Size : {file_size} bytes")

            if file_size <= 100:

                raise Exception("Input file is empty")

            # ======================================
            # LOAD AUDIO
            # ======================================

            audio = AudioSegment.from_file(input_file)

            # ======================================
            # EXPORT WAV
            # ======================================

            audio.export(output_file, format="wav")

            # ======================================
            # VERIFY OUTPUT
            # ======================================

            if not os.path.exists(output_file):

                raise FileNotFoundError(f"WAV output missing: {output_file}")

            output_size = os.path.getsize(output_file)

            print(f"Output Size : {output_size} bytes")

            if output_size <= 100:

                raise Exception("Generated WAV file corrupted")

            print("\n=================================")
            print("WAV CONVERSION SUCCESS")
            print("=================================")

            return output_file

        except Exception as e:

            print("\n=================================")
            print("WAV CONVERSION FAILED")
            print("=================================")

            print(f"Error : {str(e)}")

            print("\nTRACEBACK:\n")

            print(traceback.format_exc())

            # fallback to original file
            return input_file
