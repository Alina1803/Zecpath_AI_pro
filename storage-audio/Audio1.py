import pyttsx3
import os

# Output path
output_path = r"E:\Zecpath_AI_pro\Data\raw\Audios\sample_audio.wav"

# Ensure folder exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Initialize engine
engine = pyttsx3.init()

# CA domain test sentence
text = "I worked on GST filing, taxation compliance, and audit reporting."

# Save audio
engine.save_to_file(text, output_path)
engine.runAndWait()

print("✅ Audio file created at:", output_path)