import os
import time
import traceback

import sounddevice as sd
import numpy as np

from scipy.io.wavfile import write

class MicrophoneInput:

    def __init__(self):

        self.audio_dir = "data/raw/Audios"

        os.makedirs(self.audio_dir,exist_ok=True)

    # ==============================================
    # SHOW AVAILABLE DEVICES
    # ==============================================

    def list_devices(self):

        print("\n===== AVAILABLE AUDIO DEVICES =====\n")

        print(sd.query_devices())

    # ==============================================
    # RECORD AUDIO
    # ==============================================

    def record_audio(self,filename=None,duration=10,sample_rate=16000):

        try:

            # ======================================
            # AUTO GENERATE UNIQUE FILENAME
            # ======================================

            if filename is None:

                timestamp = int(time.time())

                filename = f"candidate_{timestamp}.wav"

            # ======================================
            # ENSURE WAV EXTENSION
            # ======================================

            if not filename.endswith(".wav"):

                filename += ".wav"

            # ======================================
            # FULL SAVE PATH
            # ======================================

            save_path = os.path.abspath(os.path.join(self.audio_dir,filename))

            # ======================================
            # DEBUG INFO
            # ======================================

            print("\n=================================")
            print("MICROPHONE RECORDING STARTED")
            print("=================================")

            print(f"Filename       : {filename}")
            print(f"Duration       : {duration} seconds")
            print(f"Sample Rate    : {sample_rate}")
            print(f"Absolute Path  : {save_path}")

            # ======================================
            # CHECK AUDIO DEVICES
            # ======================================

            try:

                default_input, default_output = sd.default.device

                print(f"Default Input Device  : {default_input}")
                print(f"Default Output Device : {default_output}")

            except Exception as device_error:

                print(f"Device Detection Error : {device_error}")

            # ======================================
            # START RECORDING
            # ======================================

            print("\nRecording... Speak now.")

            audio = sd.rec(
                int(duration * sample_rate),
                samplerate=sample_rate,
                channels=1,
                dtype="float32")

            # ======================================
            # WAIT FOR RECORDING COMPLETION
            # ======================================

            sd.wait()

            print("Recording finished.")

            # ======================================
            # VALIDATE AUDIO
            # ======================================

            if audio is None:

                raise Exception("Audio buffer is None")

            if len(audio) == 0:

                raise Exception("Audio buffer is empty")

            # ======================================
            # CONVERT FLOAT32 → INT16
            # ======================================

            audio_int16 = np.int16(audio * 32767)

            # ======================================
            # SAVE AUDIO FILE
            # ======================================

            write(save_path,
                sample_rate,
                audio_int16
            )

            # ======================================
            # VERIFY FILE EXISTS
            # ======================================

            if not os.path.exists(save_path):

                raise FileNotFoundError(
                    f"Audio file not found after save: {save_path}")

            # ======================================
            # VERIFY FILE SIZE
            # ======================================

            file_size = os.path.getsize(save_path)

            print(f"Saved File Size : {file_size} bytes")

            if file_size <= 100:

                raise Exception(
                    "Audio file too small. Recording likely failed.")

            print("\n=================================")
            print("RECORDING SUCCESS")
            print("=================================")

            print(f"Audio Saved At : {save_path}")

            return save_path

        except Exception as e:

            print("\n=================================")
            print("MICROPHONE RECORDING FAILED")
            print("=================================")

            print(f"Error : {str(e)}")

            print("\nTRACEBACK:\n")
            print(traceback.format_exc())

            return None