import os
import time
import traceback

from datetime import datetime

from app.services.voice_ai_45.text_to_speech import (
    TextToSpeechEngine,
)

from app.services.voice_ai_45.microphone_input import (
    MicrophoneInput,
)

from app.services.voice_ai_45.speech_to_text import (
    SpeechToTextEngine,
)

from app.services.voice_ai_45.audio_cleaner import (
    AudioCleaner,
)

from app.services.voice_ai_45.wav_converter import (
    WAVConverter,
)


class VoiceInterviewPipeline:

    def __init__(self):

        print("\n=================================")
        print("VOICE INTERVIEW PIPELINE STARTED")
        print("=================================")

        self.raw_audio_dir = "data/raw/Audios_45"
        self.processed_audio_dir = "data/processed/output_45"

        os.makedirs(
            self.raw_audio_dir,
            exist_ok=True,
        )

        os.makedirs(
            self.processed_audio_dir,
            exist_ok=True,
        )

        self.tts_engine = TextToSpeechEngine()

        self.microphone = MicrophoneInput()

        self.stt_engine = SpeechToTextEngine(model_name="base")

        self.cleaner = AudioCleaner()

        self.converter = WAVConverter()

        print("✅ Components Loaded")

    # ===================================

    def log(
        self,
        msg,
    ):

        print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

    # ===================================

    def is_invalid_response(
        self,
        text,
    ):

        if not text:
            return True

        text = str(text).strip().lower()

        blocked = [
            "youtube",
            "subscribe",
            "thanks for watching",
            "background music",
        ]

        return any(x in text for x in blocked)

    # ===================================

    def get_thinking_time(
        self,
        question,
        qtype,
    ):

        wc = len(question.split())

        if qtype == "role":

            if wc > 25:
                return 25

            return 15

        return 10

    # ===================================

    def get_dynamic_duration(
        self,
        question,
        qtype,
    ):

        wc = len(question.split())

        if qtype == "role":

            if wc > 25:
                return 45

            return 30

        return 20

    # ===================================

    def ask_question(
        self,
        question,
        qid,
    ):

        qid = qid or 0

        filename = f"question_{qid}_" f"{int(time.time())}.mp3"

        return self.tts_engine.generate_audio(
            text=question,
            filename=filename,
        )

    # ===================================

    def wait_before_answer(
        self,
        sec,
    ):

        self.log(f"Thinking Time = {sec}s")

        while sec > 0:

            print(
                f"Start in {sec}s",
                end="\r",
            )

            time.sleep(1)

            sec -= 1

        print()

    # ===================================

    def capture_answer(
        self,
        qid,
        duration,
    ):

        filename = f"answer_{qid}.wav"

        for attempt in range(2):

            try:

                self.log(f"Recording Attempt " f"{attempt+1}")

                path = self.microphone.record_audio_dynamic(
                    filename=filename,
                    duration=duration,
                    silence_limit=6,
                    sample_rate=16000,
                )

                if path and os.path.exists(path):
                    return path

            except Exception:

                self.log(traceback.format_exc())

        return None

    # ===================================

    def clean_audio(
        self,
        path,
        qid,
    ):

        if not path:
            return None

        try:

            size = os.path.getsize(path)

            if size < 30000:

                self.log("Skipping Cleaner")

                return path

            output = os.path.join(
                self.processed_audio_dir,
                f"cleaned_{qid}.wav",
            )

            return self.cleaner.normalize_audio(
                path,
                output,
            )

        except Exception:

            self.log(traceback.format_exc())

            return path

    # ===================================

    def transcribe_answer(
        self,
        path,
    ):

        if not path:
            return ""

        self.log("Running Whisper")

        return self.stt_engine.transcribe(path)

    # ===================================

    def process_question(
        self,
        question,
        question_id=None,
        question_type="hr",
        duration=20,
    ):

        start = time.time()

        try:

            self.log(f"Question {question_id}")

            question_audio = self.ask_question(
                question,
                question_id,
            )

            thinking = self.get_thinking_time(
                question,
                question_type,
            )

            self.wait_before_answer(thinking)

            duration = duration or self.get_dynamic_duration(
                question,
                question_type,
            )

            recorded = self.capture_answer(
                question_id,
                duration,
            )

            if not recorded:

                raise Exception("Recording Failed")

            cleaned = self.clean_audio(
                recorded,
                question_id,
            )

            wav = self.converter.convert_to_wav(cleaned)

            transcript = self.transcribe_answer(wav)

            valid = not self.is_invalid_response(transcript)

            elapsed = round(
                time.time() - start,
                2,
            )

            return {
                "status": ("success" if valid else "failed"),
                "question": question,
                "question_audio": question_audio,
                "recorded_audio": recorded,
                "cleaned_audio": cleaned,
                "wav_audio": wav,
                "transcript": transcript,
                "valid_response": valid,
                "processing_time_sec": elapsed,
                "timestamp": str(datetime.now()),
            }

        except Exception as e:

            self.log(traceback.format_exc())

            return {
                "status": "failed",
                "error": str(e),
            }


if __name__ == "__main__":

    pipeline = VoiceInterviewPipeline()

    result = pipeline.process_question(
        question="Explain backend architecture",
        question_id=1,
        question_type="role",
        duration=15,
    )

    print(result)
