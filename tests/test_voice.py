# test_voice.py

from app.services.voice_ai_45.text_to_speech import (
    TextToSpeechEngine
)

tts = TextToSpeechEngine()

tts.generate_audio(

    text="""
    Tell me about your backend
    development experience.
    """,

    interviewer_type="default"
)