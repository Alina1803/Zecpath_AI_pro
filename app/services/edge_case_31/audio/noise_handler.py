def detect_noise(audio_signal):
    if audio_signal < 0.2:
        return "low_quality"
    return "clear"