import os
import sounddevice as sd

from scipy.io.wavfile import write


class MicrophoneInput:

    def __init__(self):

        os.makedirs(
            "data/raw/Audios",
            exist_ok=True)

    def record_audio(
        self,
        filename="candidate_answer.wav",
        duration=10,
        sample_rate=44100):

        save_path = os.path.join(
            "data/raw/Audios",
            filename)

        print("\\nRecording Started...")

        audio = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16")

        sd.wait()

        write(
            save_path,
            sample_rate,
            audio
        )

        print(
            "Recording Completed"
        )

        return save_path