import os

from app.services.voice_ai_45.text_to_speech import TextToSpeechEngine
from app.services.voice_ai_45.microphone_input import MicrophoneInput
from app.services.voice_ai_45.speech_to_text import SpeechToTextEngine
from app.services.voice_ai_45.audio_cleaner import AudioCleaner
from app.services.voice_ai_45.wav_converter import WAVConverter


class VoiceInterviewPipeline:

    def __init__(self):

        self.tts_engine = TextToSpeechEngine()

        self.microphone = MicrophoneInput()

        self.stt_engine = SpeechToTextEngine()

        self.cleaner = AudioCleaner()

        self.converter = WAVConverter()
                         
    # ==========================================
    # AI ASK QUESTION
    # ==========================================
    def ask_question(
        self,
        question,
        question_id=0):

        return self.tts_engine.generate_audio(
            question,
            f"question_{question_id}.mp3"
        )

    # ==========================================
    # RECORD ANSWER
    # ==========================================
    def capture_answer(
        self,
        question_id=0,
        duration=10
    ):

        return self.microphone.record_audio(
            filename=f"answer_{question_id}.wav",
            duration=duration
        )

    # ==========================================
    # CLEAN AUDIO
    # ==========================================
    def clean_audio(
        self,
        input_path,
        question_id=0
    ):

        output_path = os.path.join(
            "data/processed/output_Audios_45",
            f"cleaned_{question_id}.wav"
        )

        return self.cleaner.normalize_audio(
            input_path,
            output_path
        )

    # ==========================================
    # TRANSCRIBE AUDIO
    # ==========================================
    def transcribe_answer(
        self,
        audio_path
    ):

        return self.stt_engine.transcribe_audio(
            audio_path
        )

    # ==========================================
    # COMPLETE PIPELINE
    # ==========================================
    def process_question(
        self,
        question,
        question_id=0,
        duration=10
    ):

        self.ask_question(
            question,
            question_id
        )

        recorded_audio = self.capture_answer(
            question_id,
            duration
        )

        cleaned_audio = self.clean_audio(
            recorded_audio,
            question_id
        )

        transcript = self.transcribe_answer(
            cleaned_audio
        )

        return {
            "question": question,
            "audio_path": cleaned_audio,
            "transcript": transcript
        }


# ==============================================
# RUN PIPELINE
# ==============================================
if __name__ == "__main__":

    pipeline = VoiceInterviewPipeline()

    result = pipeline.process_question(
        question="Tell me about yourself",
        question_id=1,
        duration=10
    )

    print("\nFINAL RESULT\n")

    print(result)