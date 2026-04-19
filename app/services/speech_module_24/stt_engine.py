import os
import whisper


os.environ["PATH"] += os.pathsep + r"G:\ffmpeg-8.1\bin"

class SpeechToTextEngine:
    def __init__(self, model_size="base"):
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)
        
        return {
            "full_text": result["text"],
            "segments": result["segments"]
        }