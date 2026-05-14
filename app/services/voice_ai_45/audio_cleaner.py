from pydub import AudioSegment

class AudioCleaner:

    def normalize_audio(
        self,
        input_file,
        output_file
    ):

        try:

            audio = (
                AudioSegment
                .from_file(input_file))

            normalized_audio = (
                audio.normalize())

            normalized_audio.export(
                output_file,
                format="wav")

            return output_file

        except Exception as e:

            print(
                f"Audio Cleaning Error: "
                f"{e}")

            return None