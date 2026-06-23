from app.services.voice_ai_45.text_to_speech import TextToSpeechEngine


def test_tts():
    # 1. Initialize Engine
    print("Initializing TTS Engine...")
    engine = TextToSpeechEngine()

    # 2. Test Scenario A: Default Female HR
    print("\n--- Testing: Default Female HR ---")
    question_1 = "Can you tell me about a time you handled a difficult conflict within your team?"
    engine.generate_audio(
        text=question_1, filename="conflict_question.mp3", interviewer_type="female_hr"
    )

    # 3. Test Scenario B: Male HR
    print("\n--- Testing: Male HR ---")
    question_2 = "What are your salary expectations for this role?"
    engine.generate_audio(
        text=question_2, filename="salary_question.mp3", interviewer_type="male_hr"
    )

    # 4. Test Scenario C: Fallback Logic
    # (Testing what happens if an invalid interviewer_type is passed)
    print("\n--- Testing: Fallback Logic ---")
    question_3 = "Where do you see yourself in five years?"
    engine.generate_audio(
        text=question_3, filename="career_goal.mp3", interviewer_type="unknown_type"
    )


if __name__ == "__main__":
    test_tts()
