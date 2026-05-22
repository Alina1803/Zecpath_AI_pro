import os
import wave
import time
import queue
import traceback

import numpy as np
import sounddevice as sd


class MicrophoneInput:

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        self.output_dir = (
            "data/raw/Audios_45"
        )

        os.makedirs(
            self.output_dir,
            exist_ok=True
        )

        print("✅ MicrophoneInput Ready")

    # =====================================================
    # LIST DEVICES
    # =====================================================

    def list_devices(self):

        print("\n=================================")
        print("AVAILABLE MICROPHONE DEVICES")
        print("=================================\n")

        devices = sd.query_devices()

        for idx, device in enumerate(devices):

            if device["max_input_channels"] > 0:

                print(
                    f"[{idx}] "
                    f"{device['name']}"
                )

        return devices

    # =====================================================
    # SMART RECORDING
    # =====================================================

    def record_audio_dynamic(

        self,

        filename="output.wav",

        duration=60,

        silence_limit=4,

        sample_rate=16000,

        device=None

    ):

        print("\n=================================")
        print("SMART RECORDING STARTED")
        print("=================================")

        filepath = os.path.join(
            self.output_dir,
            filename
        )

        audio_queue = queue.Queue()

        audio_chunks = []

        # =================================================
        # IMPROVED SETTINGS
        # =================================================

        silence_threshold = 0.0015

        block_duration = 0.2

        silence_counter = 0

        speech_detected = False

        speech_frames = 0

        min_speech_frames = 5

        # =================================================
        # CALLBACK
        # =================================================

        def callback(

            indata,
            frames,
            time_info,
            status

        ):

            if status:

                print(status)

            audio_queue.put(
                indata.copy()
            )

        try:

            # =============================================
            # START STREAM
            # =============================================

            with sd.InputStream(

                samplerate=sample_rate,

                channels=1,

                dtype="float32",

                blocksize=int(
                    sample_rate * block_duration
                ),

                device=device,

                callback=callback

            ):

                print("\n🎤 Recording Started...")
                print("Speak naturally...")
                print(
                    f"Max Duration : {duration} sec"
                )

                start_time = time.time()

                while True:

                    # =====================================
                    # MAX DURATION
                    # =====================================

                    elapsed = (
                        time.time() - start_time
                    )

                    if elapsed >= duration:

                        print(
                            "\n⏰ Max duration reached"
                        )

                        break

                    # =====================================
                    # GET AUDIO DATA
                    # =====================================

                    try:

                        data = audio_queue.get(
                            timeout=1
                        )

                    except queue.Empty:

                        continue

                    audio_chunks.append(data)

                    # =====================================
                    # BETTER VOLUME CALCULATION
                    # =====================================

                    volume = float(

                        np.sqrt(
                            np.mean(
                                np.square(data)
                            )
                        )
                    )

                    print(
                        f"Volume : {volume:.5f}",
                        end="\r"
                    )

                    # =====================================
                    # SPEECH DETECTION
                    # =====================================

                    if volume > silence_threshold:

                        speech_frames += 1

                        silence_counter = 0

                        if (
                            speech_frames >=
                            min_speech_frames
                        ):

                            speech_detected = True

                    else:

                        # only track silence
                        # AFTER speech begins

                        if speech_detected:

                            silence_counter += (
                                block_duration
                            )

                    # =====================================
                    # STOP ON SILENCE
                    # =====================================

                    if (

                        speech_detected

                        and

                        silence_counter >=
                        silence_limit

                    ):

                        print(
                            "\n🔇 Silence detected"
                        )

                        break

            # =============================================
            # NO AUDIO CHECK
            # =============================================

            if len(audio_chunks) == 0:

                raise Exception(
                    "No audio chunks captured"
                )

            # =============================================
            # MERGE AUDIO
            # =============================================

            audio = np.concatenate(
                audio_chunks,
                axis=0
            )

            # =============================================
            # AUTO NORMALIZATION
            # =============================================

            max_amp = np.max(
                np.abs(audio)
            )

            if max_amp > 0:

                audio = audio / max_amp

            # =============================================
            # CONVERT TO INT16
            # =============================================

            audio_int16 = np.int16(
                audio * 32767
            )

            # =============================================
            # SAVE WAV
            # =============================================

            with wave.open(
                filepath,
                "wb"
            ) as wf:

                wf.setnchannels(1)

                wf.setsampwidth(2)

                wf.setframerate(sample_rate)

                wf.writeframes(
                    audio_int16.tobytes()
                )

            # =============================================
            # VALIDATE FILE
            # =============================================

            if not os.path.exists(filepath):

                raise Exception(
                    "Audio file not created"
                )

            file_size = os.path.getsize(
                filepath
            )

            print(
                f"\n✅ Audio Saved : {filepath}"
            )

            print(
                f"📦 File Size : "
                f"{file_size} bytes"
            )

            # =============================================
            # VERY SMALL AUDIO CHECK
            # =============================================

            if file_size < 5000:

                print(
                    "\n⚠ Warning:"
                    " Very small audio detected"
                )

            return filepath

        except Exception as e:

            print("\n⚠ RECORDING ERROR")
            print(str(e))
            print(traceback.format_exc())

            return None