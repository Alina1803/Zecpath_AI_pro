import os

from app.services.voice_ai_45.text_to_speech import (TextToSpeechEngine)

from app.services.voice_ai_45.microphone_input import (MicrophoneInput)

from app.services.voice_ai_45.speech_to_text import (SpeechToTextEngine)

from app.services.voice_ai_45.audio_cleaner import (AudioCleaner)

from app.services.voice_ai_45.wav_converter import (WAVConverter)

# =========================================================
# VOICE INTERVIEW PIPELINE
# =========================================================

class VoiceInterviewPipeline:

    def __init__(self):

        print("\n=================================")

        print("VOICE INTERVIEW PIPELINE STARTED")

        print("=================================")

        # =================================================
        # CREATE OUTPUT DIRECTORIES
        # =================================================

        os.makedirs(
            "data/raw/Audios",
            exist_ok=True)

        os.makedirs(
            "data/processed/output_Audios_45",
            exist_ok=True)

        # =================================================
        # LOAD COMPONENTS
        # =================================================

        self.tts_engine = (TextToSpeechEngine())

        self.microphone = (MicrophoneInput())

        self.stt_engine = (SpeechToTextEngine())

        self.cleaner = (AudioCleaner())

        self.converter = (WAVConverter())

        print("Voice Pipeline Ready")

    # =====================================================
    # AI ASK QUESTION
    # =====================================================

    def ask_question(
        self,
        question,
        question_id=0):

        print("\n=================================")
        print("AI HR ASKING QUESTION")
        print("=================================")

        print(f"Question ID : {question_id}")
        print(f"Question    : {question}")

        try:

            audio_path = (
                self.tts_engine.generate_audio(
                    text=question,
                    filename=f"question_{question_id}.mp3"))

            return audio_path

        except Exception as e:

            print(f"TTS Failed: {e}")

            return None

    # =====================================================
    # RECORD ANSWER
    # =====================================================

    def capture_answer(
        self,
        question_id=0,
        duration=10):

        print("\n=================================")
        print("CAPTURING CANDIDATE ANSWER")
        print("=================================")

        try:

            recorded_path = (
                self.microphone.record_audio(
                    filename=f"answer_{question_id}.wav",
                    duration=duration,
                    sample_rate=16000))

            return recorded_path

        except Exception as e:

            print(f"Recording Failed: {e}")

            return None

    # =====================================================
    # CLEAN AUDIO
    # =====================================================

    def clean_audio(
        self,
        input_path,
        question_id=0):

        print("\n=================================")

        print("AUDIO CLEANING STARTED")

        print("=================================")

        try:

            if not input_path:

                print("No input audio provided")

                return None

            output_path = os.path.join(
                "data/processed/output_Audios_45",
                f"cleaned_{question_id}.wav")

            cleaned_audio = (
                self.cleaner.normalize_audio(
                    input_path=input_path,
                    output_path=output_path))

            print(
                f"Cleaned Audio : "
                f"{cleaned_audio}")

            return cleaned_audio

        except Exception as e:

            print(f"Audio Cleaning Error: {e}")

            return input_path

    # =====================================================
    # CONVERT AUDIO TO WAV
    # =====================================================

    def convert_audio(
        self,
        audio_path):

        print("\n=================================")
        print("WAV CONVERSION STARTED")
        print("=================================")

        try:

            if not audio_path:

                return None

            converted_audio = (
                self.converter.convert_to_wav(
                    audio_path))

            print(
                f"Converted Audio : "
                f"{converted_audio}")

            return converted_audio

        except Exception as e:

            print(f"WAV Conversion Failed: {e}")

            return audio_path

    # =====================================================
    # TRANSCRIBE AUDIO
    # =====================================================

    def transcribe_answer(
        self,
        audio_path):

        print("\n=================================")
        print("TRANSCRIPTION STARTED")
        print("=================================")

        try:

            if not audio_path:

                print("No audio available for STT")

                return ""

            transcript = (
                self.stt_engine.transcribe(
                    audio_path))

            print(
                f"\nFinal Transcript : "
                f"{transcript}")

            return transcript

        except Exception as e:

            print(f"STT Failed: {e}")

            return ""

    # =====================================================
    # COMPLETE PIPELINE
    # =====================================================

    def process_question(
        self,
        question,
        question_id=0,
        duration=10
    ):

        print("\n=================================")
        print("VOICE INTERVIEW PROCESS STARTED")
        print("=================================")

        # =================================================
        # STEP 1 : AI ASK QUESTION
        # =================================================

        question_audio = (
            self.ask_question(
                question=question,
                question_id=question_id))

        # =================================================
        # STEP 2 : RECORD ANSWER
        # =================================================

        recorded_audio = (
            self.capture_answer(
                question_id=question_id,
                duration=duration))

        # =================================================
        # STEP 3 : CLEAN AUDIO
        # =================================================

        cleaned_audio = (
            self.clean_audio(
                input_path=recorded_audio,
                question_id=question_id
            )
        )

        # =================================================
        # STEP 4 : CONVERT AUDIO
        # =================================================

        wav_audio = (
            self.convert_audio(
                cleaned_audio
            )
        )

        # =================================================
        # STEP 5 : TRANSCRIBE AUDIO
        # =================================================

        transcript = (
            self.transcribe_answer(
                wav_audio
            )
        )

        # =================================================
        # FINAL RESULT
        # =================================================

        result = {

            "question": question,
            "question_audio": question_audio,
            "recorded_audio": recorded_audio,
            "cleaned_audio": cleaned_audio,
            "wav_audio": wav_audio,
            "audio_path": wav_audio,
            "transcript": transcript
        }

        print("\n=================================")
        print("VOICE PIPELINE RESULT")
        print("=================================")

        print(result)

        return result

# =========================================================
# TEST PIPELINE
# =========================================================

if __name__ == "__main__":

    pipeline = (VoiceInterviewPipeline())

    result = pipeline.process_question(
        question="Tell me about yourself",
        question_id=1,
        duration=15)

    print("\n=================================")
    print("FINAL RESULT")
    print("=================================")

    print(result)