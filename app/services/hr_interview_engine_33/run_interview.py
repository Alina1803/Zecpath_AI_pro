import os
import json

from datetime import datetime

from app.services.hr_interview_engine_33.state_manager.interview_state import (InterviewState)
from app.services.hr_interview_engine_33.question_engine.role_based_generator import (RoleBasedQuestionGenerator)
from app.services.hr_interview_engine_33.flow_engine.interview_flow import (InterviewFlow)
from app.services.screening_engine_26.scoring_engine import (AdvancedScoringEngine)
from app.services.voice_ai_45.voice_pipeline import (VoiceInterviewPipeline)

# =========================================================
# CONFIG
# =========================================================

OUTPUT_DIR = os.path.join("data","processed","output_33")

DOMAIN_BASE_PATH = os.path.join("data","domain_knowledge")

# =========================================================
# FILE HELPERS
# =========================================================

def create_output_dir():

    os.makedirs(OUTPUT_DIR,exist_ok=True)

def save_results(data):

    create_output_dir()

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    file_path = os.path.join(
        OUTPUT_DIR,
        f"interview_{timestamp}.json"
    )

    with open(file_path, "w") as f:

        json.dump(
            data,
            f,
            indent=4
        )

    print(
        f"\nResults saved to: {file_path}"
    )

# =========================================================
# INPUT VALIDATION
# =========================================================

def get_valid_experience():

    while True:

        exp = input(
            "Enter experience (fresher/experienced): "
        ).strip().lower()

        if exp in [
            "fresher",
            "experienced"
        ]:

            return exp

        print(
            "Invalid input. "
            "Please enter "
            "'fresher' or 'experienced'."
        )

# =========================================================
# SCORING DEPENDENCIES
# =========================================================

def load_scoring_dependencies(role):

    role = role.lower()

    base_path = os.path.join(
        DOMAIN_BASE_PATH,
        role
    )

    domain_path = os.path.join(
        base_path,
        "domain.json"
    )

    prompt_path = os.path.join(
        base_path,
        "prompt.txt"
    )

    if (
        not os.path.exists(domain_path)
        or
        not os.path.exists(prompt_path)
    ):

        raise FileNotFoundError(
            f"Missing scoring files for role: {role}"
        )

    with open(domain_path, "r") as f:

        domain_data = json.load(f)

    with open(prompt_path, "r") as f:

        prompt_template = f.read()

    return (
        domain_data,
        prompt_template
    )

# =========================================================
# SIMPLE HR SCORE
# =========================================================

def simple_hr_score(answer):

    words = answer.strip().split()

    if len(words) < 3:
        return 3

    elif len(words) < 8:
        return 5

    return 7

# =========================================================
# FOLLOWUP DECISION
# =========================================================

class SimpleDecision:

    def should_followup(
        self,
        level
    ):

        return level == "low"

# =========================================================
# LEGACY INTERVIEW ENGINE
# =========================================================

class LegacyInterviewEngine:

    def __init__(self):

        self.total_questions = 6

        # =====================================
        # VOICE PIPELINE
        # =====================================

        self.voice_pipeline = (
            VoiceInterviewPipeline()
        )

    def run(
        self,
        role,
        experience
    ):

        print(
            "\n===== HR Interview Engine Started =====\n"
        )

        # -----------------------------------
        # CORE COMPONENTS
        # -----------------------------------

        state = InterviewState(
            role,
            experience
        )

        generator = (
            RoleBasedQuestionGenerator(
                role,
                experience
            )
        )

        flow = InterviewFlow(
            state,
            generator
        )

        # -----------------------------------
        # SCORING ENGINE
        # -----------------------------------

        scoring_engine = None

        try:

            (
                domain_data,
                prompt_template
            ) = load_scoring_dependencies(
                role
            )

            scoring_engine = (
                AdvancedScoringEngine(
                    domain_data,
                    prompt_template
                )
            )

            print(
                "Scoring Engine Initialized"
            )

        except Exception as e:

            print(
                f"Scoring Engine Disabled: {e}"
            )

        # -----------------------------------
        # DECISION ENGINE
        # -----------------------------------

        decision_engine = (
            SimpleDecision()
        )

        print(
            "\n--- Interview Started ---"
        )

        # -----------------------------------
        # MAIN LOOP
        # -----------------------------------

        for i in range(
            self.total_questions
        ):

            print(
                f"\nPhase: "
                f"{state.current_phase.upper()}"
            )

            q_data = flow.get_next_question()

            if (
                not q_data
                or
                "question" not in q_data
            ):

                print(
                    "No valid question available."
                )

                break

            question_text = q_data.get(
                "question",
                "No question"
            )

            q_type = q_data.get(
                "type",
                "unknown"
            )

            print(
                f"\nQ{i+1} "
                f"[{q_type.upper()}]: "
                f"{question_text}"
            )

            # =================================
            # VOICE INTERVIEW PIPELINE
            # =================================

            try:

                voice_result = (
                    self.voice_pipeline.process_question(
                        question=question_text,
                        question_id=i,
                        duration=15
                    )
                )

                answer = voice_result.get(
                    "transcript",
                    ""
                )

                print(
                    f"\nCandidate Answer: "
                    f"{answer}"
                )

            except Exception as e:

                print(
                    f"Voice Pipeline Failed: {e}"
                )

                answer = ""

            # =================================
            # SCORING
            # =================================

            score = 5

            if q_type == "hr":

                score = (
                    simple_hr_score(answer)
                )

            else:

                if scoring_engine:

                    try:

                        score = (
                            scoring_engine.evaluate(
                                question_text,
                                answer
                            )
                        )

                        if score is None:

                            score = 5

                    except Exception as e:

                        print(
                            f"Scoring failed: {e}"
                        )

                        score = 5

            # =================================
            # UPDATE STATE
            # =================================

            state.update(
                q_data,
                answer,
                score
            )

            # =================================
            # FOLLOWUP
            # =================================

            followup, level = (
                flow.handle_followup(
                    q_data,
                    answer,
                    analyzer=None,
                    followup_generator=None,
                    decision=decision_engine
                )
            )

            if followup:

                print(
                    f"\nFollow-up: {followup}"
                )

                # =============================
                # FOLLOWUP VOICE PIPELINE
                # =============================

                try:

                    followup_voice = (
                        self.voice_pipeline.process_question(
                            question=followup,
                            question_id=f"followup_{i}",
                            duration=10
                        )
                    )

                    fu_answer = (
                        followup_voice.get(
                            "transcript",
                            ""
                        )
                    )

                    print(
                        f"\nFollow-up Answer: "
                        f"{fu_answer}"
                    )

                except Exception as e:

                    print(
                        f"Follow-up Voice Failed: {e}"
                    )

                    fu_answer = ""

                state.update(
                    q_data,
                    fu_answer,
                    score,
                    followup=True
                )

            # =================================
            # NEXT PHASE
            # =================================

            flow.progress()

        # -----------------------------------
        # RESULTS
        # -----------------------------------

        print(
            "\n--- Interview Completed ---\n"
        )

        results = state.get_results()

        print(
            "===== INTERVIEW SUMMARY ====="
        )

        print(
            json.dumps(
                results,
                indent=4
            )
        )

        save_results(
            results
        )

        return results

# =========================================================
# LEGACY CLI ENTRY
# =========================================================

def run():

    role = input(
        "Enter role: "
    ).strip().lower()

    experience = (
        get_valid_experience()
    )

    engine = (
        LegacyInterviewEngine()
    )

    engine.run(
        role=role,
        experience=experience
    )

if __name__ == "__main__":

    run()