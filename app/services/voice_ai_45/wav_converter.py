from pydub import AudioSegment

class WAVConverter:

    def convert_to_wav(
        self,
        input_file,
        output_file):

        try:

            audio = (
                AudioSegment
                .from_file(input_file))

            audio.export(
                output_file,
                format="wav")

            return output_file

        except Exception as e:

            print(
                f"WAV Conversion Error: "
                f"{e}"
            )

            return None