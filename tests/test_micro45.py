from app.services.voice_ai_45.microphone_input import MicrophoneInput

mic = MicrophoneInput()

mic.list_devices()

path = mic.record_audio_dynamic(filename="smart_test.wav", duration=20, silence_limit=5)

print(path)
