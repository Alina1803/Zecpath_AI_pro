import os
import time
import asyncio
import random
import threading
import edge_tts
from pydub import AudioSegment
from pydub.playback import play

class TextToSpeechEngine:
    def __init__(self): 
        # Fix: Use Absolute Path to ensure you find the files easily
        self.base_dir = os.getcwd() 
        self.output_dir = os.path.join(self.base_dir, "data", "raw", "questions_45")
        
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir, exist_ok=True)
            print(f"📁 Created directory: {self.output_dir}")

        self.hr_voices = {
            "senior_female": "en-IN-NeerjaNeural", 
            "senior_male": "en-IN-PrabhatNeural", 
            "modern_female": "en-IN-AnanyaNeural",
            "default": "en-IN-NeerjaNeural"
        }

    def make_natural_script(self, text):
        """Adds human-like variations to the HR script."""
        intro_fillers = ["Alright.", "Moving on,", "I see.", "Great.", "Next question.", "Tell me..."]
        outro_prompts = [
            "Please share your thoughts on this.",
            "I'd love to hear some examples.",
            "Take your time to explain.",
            "Could you elaborate on that?"
        ]
        
        prefix = random.choice(intro_fillers)
        suffix = random.choice(outro_prompts)
        return f"{prefix}... {text},,, {suffix}"

    async def _generate(self, text, output_path, voice):
        """Internal async method to call Edge TTS."""
        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
            rate="-10%", 
            pitch="-2Hz"
        )
        await communicate.save(output_path)

    def run_async(self, coro):
        """Runs the async TTS generator in a synchronous thread."""
        result = {"success": False, "error": None}

        def runner():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                loop.run_until_complete(coro)
                result["success"] = True
            except Exception as e:
                result["error"] = str(e)
            finally:
                loop.close()

        thread = threading.Thread(target=runner)
        thread.start()
        thread.join()

        if result["error"]:
            raise Exception(result["error"])

    def wait_for_audio(self, path, timeout=15):
        """Checks if the file was created and is not empty."""
        start = time.time()
        while time.time() - start < timeout:
            if os.path.exists(path):
                if os.path.getsize(path) > 1000: # Ensure file is not just a 0kb placeholder
                    return True
            time.sleep(0.5)
        return False

    def play_audio(self, audio_path):
        """Plays the generated audio with professional HR pauses."""
        try:
            audio = AudioSegment.from_file(audio_path)
            pause = AudioSegment.silent(duration=400) # 400ms professional pause
            final_audio = pause + audio + pause
            play(final_audio)
        except Exception as e:
            print(f"Playback Error: {e}")

    def generate_audio(self, text, filename="question.mp3", interviewer_type="senior_female"):
        try:
            natural_text = self.make_natural_script(text)
            voice = self.hr_voices.get(interviewer_type, self.hr_voices["default"])
            
            unique_filename = f"{int(time.time())}_{filename}"
            output_path = os.path.join(self.output_dir, unique_filename)

            print(f"\n--- AI HR GENERATION ---")
            print(f"📍 Location: {output_path}")
            print(f"🎤 Voice   : {voice} ({interviewer_type})")
            print(f"💬 Script  : {natural_text}")

            # 1. Run the async generation
            self.run_async(self._generate(natural_text, output_path, voice))

            # 2. Verify file exists
            if self.wait_for_audio(output_path):
                print("✅ Audio File Generated Successfully.")
                # 3. Play the audio
                self.play_audio(output_path)
                return output_path
            else:
                print("❌ Timeout: File was not created.")
                return None

        except Exception as e:
            print(f"❌ TTS Error: {e}")
            import traceback
            traceback.print_exc()
            return None