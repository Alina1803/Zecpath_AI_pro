import os
import time
import traceback
from datetime import datetime

from app.services.voice_ai_45.text_to_speech import (
    TextToSpeechEngine
)

from app.services.voice_ai_45.microphone_input import (
    MicrophoneInput
)

from app.services.voice_ai_45.speech_to_text import (
    SpeechToTextEngine
)

from app.services.voice_ai_45.audio_cleaner import (
    AudioCleaner
)

from app.services.voice_ai_45.wav_converter import (
    WAVConverter
)


# =========================================================
# VOICE INTERVIEW PIPELINE
# =========================================================

class VoiceInterviewPipeline:

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        print("\n=================================")
        print("VOICE INTERVIEW PIPELINE STARTED")
        print("=================================")

        self.raw_audio_dir = (
            "data/raw/Audios_45"
        )

        self.processed_audio_dir = (
            "data/processed/output_45"
        )

        os.makedirs(
            self.raw_audio_dir,
            exist_ok=True
        )

        os.makedirs(
            self.processed_audio_dir,
            exist_ok=True
        )

        print("\nLoading Voice Components...")

        # =================================================
        # COMPONENTS
        # =================================================

        self.tts_engine = (
            TextToSpeechEngine()
        )

        self.microphone = (
            MicrophoneInput()
        )

        self.stt_engine = (
            SpeechToTextEngine(
                model_name="small.en"
            )
        )

        self.cleaner = (
            AudioCleaner()
        )

        self.converter = (
            WAVConverter()
        )

        print("\n✅ Voice Pipeline Ready")

    # =====================================================
    # RESPONSE VALIDATION
    # =====================================================

    def is_invalid_response(
        self,
        transcript
    ):

        try:

            if not transcript:
                return True

            text = str(
                transcript
            ).strip().lower()

            if not text:
                return True

            blocked = [

                "background music",
                "subscribe",
                "youtube",
                "facebook",
                "instagram",
                "testing testing",
                "be right back",
                "music noise"
            ]

            for item in blocked:

                if item in text:
                    return True

            words = text.split()

            # =============================================
            # EMPTY / VERY SHORT
            # =============================================

            if len(words) <= 1:
                return True

            return False

        except:

            return False

    # =====================================================
    # SMART THINKING TIME
    # =====================================================

    def get_thinking_time(
        self,
        question,
        question_type="hr"
    ):

        try:

            question = str(question)

            word_count = len(
                question.split()
            )

            # =============================================
            # ROLE QUESTIONS
            # =============================================

            if question_type == "role":

                if word_count >= 35:
                    return 60

                elif word_count >= 20:
                    return 45

                return 30

            # =============================================
            # HR QUESTIONS
            # =============================================

            if word_count >= 20:
                return 30

            return 20

        except:

            return 20

    # =====================================================
    # SMART ANSWER DURATION
    # =====================================================

    def get_dynamic_duration(
        self,
        question,
        question_type="hr"
    ):

        try:

            question = str(question)

            word_count = len(
                question.split()
            )

            # =============================================
            # ROLE QUESTIONS
            # =============================================

            if question_type == "role":

                if word_count >= 35:
                    return 300

                elif word_count >= 25:
                    return 240

                elif word_count >= 15:
                    return 180

                return 120

            # =============================================
            # HR QUESTIONS
            # =============================================

            if word_count >= 25:
                return 180

            elif word_count >= 15:
                return 120

            return 90

        except:

            return 120

    # =====================================================
    # ASK QUESTION
    # =====================================================

    def ask_question(
        self,
        question,
        question_id=0
    ):

        print("\n=================================")
        print("AI HR ASKING QUESTION")
        print("=================================")

        print(f"Question ID : {question_id}")
        print(f"Question    : {question}")

        try:
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            filename = (
                f"question_{question_id}_{timestamp}.mp3")
        

            print(
                "\nGenerating Natural AI Voice..."
            )

            # =============================================
            # GENERATE + AUTO PLAY
            # =============================================

            audio_path = (
                self.tts_engine.generate_audio(
                    text=question,
                    filename=filename
                )
            )

            if not audio_path:

                raise Exception(
                    "TTS audio generation failed"
                )

            # =============================================
            # SPEAKER BUFFER
            # =============================================

            time.sleep(1.5)

            print(
                "\n✅ AI Question Completed"
            )

            return audio_path

        except Exception as e:

            print("\n⚠ TTS FAILED")
            print(str(e))
            print(traceback.format_exc())

            return None

    # =====================================================
    # THINKING TIME
    # =====================================================

    def wait_before_answer(
        self,
        thinking_time=20
    ):

        print("\n=================================")
        print("THINKING TIME")
        print("=================================")

        print(
            f"\nCandidate has "
            f"{thinking_time} seconds to think..."
        )

        for sec in range(
            thinking_time,
            0,
            -1
        ):

            print(
                f"Starting answer in {sec} sec",
                end="\r"
            )

            time.sleep(1)

        print(
            "\n✅ Recording Starting Now..."
        )

    # =====================================================
    # RECORD ANSWER
    # =====================================================

    def capture_answer(
        self,
        question_id=0,
        duration=120
    ):

        print("\n=================================")
        print("CAPTURING CANDIDATE ANSWER")
        print("=================================")

        try:

            filename = (
                f"answer_{question_id}.wav"
            )

            print(
                f"Maximum Recording Duration : "
                f"{duration} sec"
            )

            print(
                "\n🎤 Candidate can speak freely..."
            )

            print(
                "Smart silence detection enabled."
            )

            # =============================================
            # MIC WARMUP
            # =============================================

            time.sleep(2)

            # =============================================
            # RECORD
            # =============================================

            recorded_path = (
                self.microphone.record_audio_dynamic(
                    filename=filename,
                    duration=duration,
                    silence_limit=8,
                    sample_rate=16000
                )
            )

            if not recorded_path:

                raise Exception(
                    "Microphone returned empty path"
                )

            if not os.path.exists(
                recorded_path
            ):

                raise FileNotFoundError(
                    recorded_path
                )

            file_size = os.path.getsize(
                recorded_path
            )

            print(
                f"Recorded File Size : "
                f"{file_size} bytes"
            )

            if file_size <= 1000:

                raise Exception(
                    "Recorded audio too small"
                )

            print(
                f"\n✅ Candidate Audio Captured : "
                f"{recorded_path}"
            )

            return recorded_path

        except Exception as e:

            print("\n⚠ RECORDING FAILED")
            print(str(e))
            print(traceback.format_exc())

            return None

    # =====================================================
    # CLEAN AUDIO
    # =====================================================

    def clean_audio(
        self,
        input_path,
        question_id=0
    ):

        print("\n=================================")
        print("AUDIO CLEANING STARTED")
        print("=================================")

        try:

            if not input_path:

                print(
                    "⚠ Input audio missing"
                )

                return None

            output_path = os.path.join(

                self.processed_audio_dir,

                f"cleaned_{question_id}.wav"
            )

            cleaned_audio = (
                self.cleaner.normalize_audio(
                    input_path=input_path,
                    output_path=output_path
                )
            )

            print(
                f"✅ Cleaned Audio : "
                f"{cleaned_audio}"
            )

            return cleaned_audio

        except Exception as e:

            print("\n⚠ AUDIO CLEANING FAILED")
            print(str(e))
            print(traceback.format_exc())

            return input_path

    # =====================================================
    # WAV CONVERSION
    # =====================================================

    def convert_audio(
        self,
        audio_path
    ):

        print("\n=================================")
        print("WAV CONVERSION STARTED")
        print("=================================")

        try:

            if not audio_path:

                return None

            converted_audio = (
                self.converter.convert_to_wav(
                    audio_path
                )
            )

            print(
                f"✅ Converted Audio : "
                f"{converted_audio}"
            )

            return converted_audio

        except Exception as e:

            print("\n⚠ WAV CONVERSION FAILED")
            print(str(e))
            print(traceback.format_exc())

            return audio_path

    # =====================================================
    # TRANSCRIBE AUDIO
    # =====================================================

    def transcribe_answer(
        self,
        audio_path
    ):

        print("\n=================================")
        print("TRANSCRIPTION STARTED")
        print("=================================")

        try:

            if not audio_path:
                return ""

            transcript = (
                self.stt_engine.transcribe(
                    audio_path
                )
            )

            transcript = str(
                transcript
            ).strip()

            print("\n=================================")
            print("FINAL TRANSCRIPT")
            print("=================================")

            print(transcript)

            return transcript

        except Exception as e:

            print("\n⚠ STT FAILED")
            print(str(e))
            print(traceback.format_exc())

            return ""

    # =====================================================
    # FULL PROCESS PIPELINE
    # =====================================================

    def process_question(
        self,
        question,
        question_id=0,
        question_type="hr",
        duration=None
    ):

        print("\n=================================")
        print("VOICE INTERVIEW PROCESS STARTED")
        print("=================================")

        pipeline_start = time.time()

        try:

            # =============================================
            # SMART DURATION
            # =============================================

            if duration is None:

                duration = (
                    self.get_dynamic_duration(
                        question=question,
                        question_type=question_type
                    )
                )

            # =============================================
            # THINKING TIME
            # =============================================

            thinking_time = (
                self.get_thinking_time(
                    question=question,
                    question_type=question_type
                )
            )

            print(
                f"\nThinking Time : "
                f"{thinking_time} sec"
            )

            print(
                f"Answer Duration : "
                f"{duration} sec"
            )

            # =============================================
            # STEP 1 : ASK QUESTION
            # =============================================

            step_start = time.time()

            question_audio = (
                self.ask_question(
                    question=question,
                    question_id=question_id
                )
            )

            print(
                f"Question Step Time : "
                f"{round(time.time()-step_start,2)} sec"
            )

            # =============================================
            # STEP 2 : THINKING TIME
            # =============================================

            self.wait_before_answer(
                thinking_time=thinking_time
            )

            # =============================================
            # STEP 3 : RECORD ANSWER
            # =============================================

            step_start = time.time()

            recorded_audio = (
                self.capture_answer(
                    question_id=question_id,
                    duration=duration
                )
            )

            print(
                f"Recording Step Time : "
                f"{round(time.time()-step_start,2)} sec"
            )

            # =============================================
            # STEP 4 : CLEAN AUDIO
            # =============================================

            step_start = time.time()

            cleaned_audio = (
                self.clean_audio(
                    input_path=recorded_audio,
                    question_id=question_id
                )
            )

            print(
                f"Cleaning Step Time : "
                f"{round(time.time()-step_start,2)} sec"
            )

            # =============================================
            # STEP 5 : CONVERT AUDIO
            # =============================================

            wav_audio = (
                self.convert_audio(
                    cleaned_audio
                )
            )

            if not wav_audio:

                raise Exception(
                    "Final WAV audio missing"
                )

            # =============================================
            # STEP 6 : TRANSCRIBE
            # =============================================

            step_start = time.time()

            transcript = (
                self.transcribe_answer(
                    wav_audio
                )
            )

            print(
                f"STT Step Time : "
                f"{round(time.time()-step_start,2)} sec"
            )

            # =============================================
            # STEP 7 : VALIDATION
            # =============================================

            invalid = (
                self.is_invalid_response(
                    transcript
                )
            )

            if invalid:

                transcript = (
                    "Invalid or unclear response detected."
                )

            total_time = round(
                time.time() - pipeline_start,
                2
            )

            # =============================================
            # RESULT
            # =============================================

            result = {

                "question": question,

                "question_id": question_id,

                "question_type": question_type,

                "thinking_time": thinking_time,

                "duration": duration,

                "question_audio": question_audio,

                "recorded_audio": recorded_audio,

                "cleaned_audio": cleaned_audio,

                "wav_audio": wav_audio,

                "audio_path": wav_audio,

                "transcript": transcript,

                "valid_response": (
                    not invalid
                ),

                "status": (
                    "success"
                    if not invalid
                    else "failed"
                ),

                "timestamp": str(
                    datetime.now()
                ),

                "processing_time_sec": total_time
            }

            print("\n=================================")
            print("VOICE PIPELINE RESULT")
            print("=================================")

            print(result)

            return result

        except Exception as e:

            print("\n=================================")
            print("VOICE PIPELINE FAILED")
            print("=================================")

            print(str(e))
            print(traceback.format_exc())

            return {

                "question": question,

                "question_id": question_id,

                "question_type": question_type,

                "status": "failed",

                "transcript": "",

                "error": str(e),

                "timestamp": str(
                    datetime.now()
                )
            }


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    pipeline = (
        VoiceInterviewPipeline()
    )

    result = pipeline.process_question(

        question=(
            "Explain your backend architecture "
            "and database optimization strategy "
            "with real-world examples."
        ),

        question_id=1,

        question_type="role"
    )

    print("\n=================================")
    print("FINAL RESULT")
    print("=================================")

    print(result)