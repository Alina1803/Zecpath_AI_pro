import os
import json
import shutil

from datetime import datetime

from app.services.voice_ai_45.voice_pipeline import VoiceInterviewPipeline

# =====================================================
# OUTPUT CONFIG
# =====================================================

OUTPUT_DIR = os.path.join("data", "processed", "output", "output_test")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================================
# SAVE RESULT JSON
# =====================================================


def save_result(data):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_path = os.path.join(OUTPUT_DIR, f"voice_pipeline_test_{timestamp}.json")

    with open(output_path, "w", encoding="utf-8") as f:

        json.dump(data, f, indent=4, ensure_ascii=False)

    print("\n=================================")
    print("RESULT SAVED")
    print("=================================")

    print(f"Saved JSON : {output_path}")

    return output_path


# =====================================================
# COPY AUDIO TO OUTPUT FOLDER
# =====================================================


def save_audio_copy(audio_path):

    if not audio_path or not os.path.exists(audio_path):

        print("\nAudio file not found")
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    copied_audio = os.path.join(OUTPUT_DIR, f"recorded_intro_{timestamp}.wav")

    shutil.copy(audio_path, copied_audio)

    print("\n=================================")
    print("AUDIO SAVED")
    print("=================================")

    print(f"Saved Audio : {copied_audio}")

    return copied_audio


# =====================================================
# SAFE AUDIO PLAY
# =====================================================


def play_audio(audio_path):

    try:

        print("\n=================================")
        print("PLAYING RECORDED AUDIO")
        print("=================================")

        # convert to absolute path
        audio_path = os.path.abspath(audio_path)

        # check file exists
        if not os.path.exists(audio_path):

            print("Audio file not found")
            return

        print(f"Audio File : {audio_path}")

        # open using default windows player
        os.startfile(audio_path)

        print("\nAudio player launched successfully")

    except Exception as e:

        print("\n=================================")
        print("AUDIO PLAYBACK FAILED")
        print("=================================")

        print(str(e))

        print("\nOpen this file manually:\n")
        print(audio_path)


# =====================================================
# TEST VOICE PIPELINE
# =====================================================


def run_test():

    print("\n=================================")
    print("VOICE PIPELINE TEST STARTED")
    print("=================================")

    # =================================================
    # INITIALIZE PIPELINE
    # =================================================

    pipeline = VoiceInterviewPipeline()

    # =================================================
    # PROCESS QUESTION
    # =================================================

    result = pipeline.process_question(
        question=(
            "Please introduce yourself. "
            "Tell me about your background, "
            "skills, and experience."
        ),
        question_id="self_intro",
        duration=60,
    )

    # =================================================
    # PRINT FINAL RESULT
    # =================================================

    print("\n=================================")
    print("FINAL RESULT")
    print("=================================")

    print(json.dumps(result, indent=4))

    # =================================================
    # SAVE JSON OUTPUT
    # =================================================

    save_result(result)

    # =================================================
    # SAVE AUDIO COPY
    # =================================================

    audio_path = result.get("audio_path")

    copied_audio = save_audio_copy(audio_path)

    # =================================================
    # PLAY AUDIO
    # =================================================

    play_audio(copied_audio)

    # =================================================
    # VALIDATION
    # =================================================

    transcript = result.get("transcript", "")

    print("\n=================================")
    print("TRANSCRIPT CHECK")
    print("=================================")

    if transcript:

        print("\nSTT SUCCESS")

        print(f"\nTranscript:\n{transcript}")

    else:

        print("\nSTT FAILED")

        print(
            "\nPossible Issues:\n"
            "- microphone not capturing\n"
            "- ffmpeg missing\n"
            "- whisper issue\n"
            "- silent audio\n"
            "- wrong input device\n"
            "- low microphone volume"
        )

    print("\n=================================")
    print("TEST COMPLETED")
    print("=================================")


# =====================================================
# ENTRY POINT
# =====================================================

if __name__ == "__main__":

    run_test()
