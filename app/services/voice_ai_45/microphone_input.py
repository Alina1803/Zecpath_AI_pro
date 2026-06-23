import os
import wave
import time
import queue
import traceback

import numpy as np
import sounddevice as sd


class MicrophoneInput:

    def __init__(self):

        self.output_dir = "data/raw/Audios_45"

        os.makedirs(
            self.output_dir,
            exist_ok=True,
        )

        print("✅ MicrophoneInput Ready")

    # =================================================
    # SMART DYNAMIC RECORDING
    # =================================================

    def record_audio_dynamic(
        self,
        filename="output.wav",
        duration=30,
        silence_limit=4,
        sample_rate=16000,
        device=None,
    ):

        filepath = os.path.join(
            self.output_dir,
            filename,
        )

        audio_queue = queue.Queue(maxsize=100)

        frames = []

        threshold = 0.005

        speech_started = False

        silence_time = 0

        min_record_time = 3

        min_audio_size = 12000

        block = 1024

        block_duration = block / sample_rate

        def callback(
            indata,
            frame_count,
            time_info,
            status,
        ):

            if status:
                print("Stream:", status)

            try:

                if not audio_queue.full():

                    audio_queue.put_nowait(indata.copy())

            except Exception:
                pass

        try:

            print("\n=================================")
            print("SMART RECORDING STARTED")
            print("=================================")

            sd.stop()

            time.sleep(0.5)

            with sd.InputStream(
                samplerate=sample_rate,
                channels=1,
                dtype="float32",
                blocksize=block,
                callback=callback,
                latency="low",
                device=device,
            ):

                print("\n🎤 Recording...")
                print("Speak now")

                start = time.time()

                while True:

                    elapsed = time.time() - start

                    if elapsed >= duration:

                        print("\n⏰ Duration Finished")

                        break

                    try:

                        data = audio_queue.get(timeout=1)

                    except queue.Empty:

                        continue

                    volume = float(np.sqrt(np.mean(np.square(data))))

                    print(
                        f"Volume={volume:.5f}",
                        end="\r",
                    )

                    frames.append(data)

                    if volume > threshold:

                        if not speech_started:

                            print("\n✅ Speech Detected")

                        speech_started = True

                        silence_time = 0

                    elif speech_started:

                        silence_time += block_duration

                    recorded_time = len(frames) * block_duration

                    if (
                        speech_started
                        and recorded_time >= min_record_time
                        and silence_time >= silence_limit
                    ):

                        print("\n🔇 Silence Detected")

                        break

            sd.stop()

            if len(frames) == 0:

                raise Exception("No audio captured")

            audio = np.concatenate(
                frames,
                axis=0,
            )

            energy = float(np.mean(np.abs(audio)))

            print(f"\nEnergy={energy}")

            if energy < 0.002:

                raise Exception("Audio energy too low")

            peak = np.max(np.abs(audio))

            if peak > 0:

                audio = audio / peak

            audio = (audio * 32767).astype(np.int16)

            with wave.open(
                filepath,
                "wb",
            ) as wf:

                wf.setnchannels(1)

                wf.setsampwidth(2)

                wf.setframerate(sample_rate)

                wf.writeframes(audio.tobytes())

            size = os.path.getsize(filepath)

            print("\n✅ Saved")
            print(filepath)
            print(f"Size={size}")

            if size < min_audio_size:

                raise Exception(f"Audio too small ({size})")

            return filepath

        except Exception as e:

            sd.stop()

            print("\n⚠ RECORD FAILED")

            print(str(e))

            print(traceback.format_exc())

            try:

                if os.path.exists(filepath):

                    os.remove(filepath)

            except Exception:
                pass

            return None
