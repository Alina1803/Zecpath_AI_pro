import os
import json
from datetime import datetime

from app.services.hr_interview_engine_33.state_manager.interview_state import (InterviewState)
from app.services.hr_interview_engine_33.question_engine.role_based_generator import (RoleBasedQuestionGenerator)
from app.services.hr_interview_engine_33.flow_engine.interview_flow import (InterviewFlow)
from app.services.screening_engine_26.scoring_engine import (AdvancedScoringEngine)

from app.services.followup_engine34.response_analyzer import (ResponseAnalyzer)
from app.services.followup_engine34.followup_generator import (FollowUpGenerator)
from app.services.followup_engine34.decision_tree import (DecisionTree)

# =========================================================
# CONFIG
# =========================================================

OUTPUT_DIR = os.path.join("Data","processed","output_34")
DOMAIN_BASE_PATH = os.path.join("Data","domain_knowledge")

# =========================================================
# FILE HELPERS
# =========================================================

def create_output_dir():

    os.makedirs(OUTPUT_DIR,exist_ok=True)

def save_results(data):
    create_output_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(OUTPUT_DIR,f"interview_{timestamp}.json")

    with open(file_path, "w") as f:

        json.dump(data,f,indent=4)

    print(f"\nResults saved to: {file_path}")
# =========================================================
# INPUT VALIDATION
# =========================================================

def get_valid_experience():

    while True:

        exp = input(
            "Enter experience "
            "(fresher/experienced): "
        ).strip().lower()

        if exp in [
            "fresher",
            "experienced"
        ]:

            return exp

        print("Invalid input. " "Please enter " "'fresher' or 'experienced'.")

# =========================================================
# LOAD SCORING
# =========================================================

def load_scoring_dependencies(role):

    role = role.lower()

    base_path = os.path.join(
        DOMAIN_BASE_PATH,role)

    domain_path = os.path.join(base_path,"domain.json")

    prompt_path = os.path.join(base_path,"prompt.txt")

    if not os.path.exists(domain_path):

        raise FileNotFoundError(
            f"Missing domain.json at "
            f"{domain_path}")

    if not os.path.exists(prompt_path):

        raise FileNotFoundError(
            f"Missing prompt.txt at "
            f"{prompt_path}"
        )

    with open(domain_path, "r") as f:

        domain_data = json.load(f)

    with open(prompt_path, "r") as f:

        prompt_template = f.read()

    return (
        domain_data,
        prompt_template)

# =========================================================
# LEGACY FOLLOWUP PIPELINE
# =========================================================

class LegacyFollowupPipeline:

    def __init__(self):

        self.total_questions = 6

    def run(self,role,experience):

        print("\n===== FOLLOWUP PIPELINE " "STARTED =====\n")

        # -------------------------------------
        # CORE COMPONENTS
        # -------------------------------------

        state = InterviewState(role,experience)

        generator = (
            RoleBasedQuestionGenerator(role,experience)
        )

        flow = InterviewFlow(state,generator)

        # -------------------------------------
        # FOLLOWUP COMPONENTS
        # -------------------------------------

        analyzer = ResponseAnalyzer()
        followup_generator = (FollowUpGenerator())
        decision = DecisionTree()

        # -------------------------------------
        # SCORING ENGINE
        # -------------------------------------

        scoring_engine = None
        try:

            (
                domain_data,
                prompt_template
            ) = load_scoring_dependencies(role)

            scoring_engine = (
                AdvancedScoringEngine(domain_data,prompt_template))

            print("Scoring Engine Initialized")

        except Exception as e:

            print(f"Scoring Engine Disabled: {e}")

        print("\n--- Interview Started ---")

        # -------------------------------------
        # MAIN LOOP
        # -------------------------------------

        for i in range(
            self.total_questions):

            print(
                f"\nPhase: "
                f"{state.current_phase.upper()}")

            question = (flow.get_next_question())

            if not question:

                print("No question available.")

                break

            print(f"\nQ{i+1}: {question}")

            answer = input(
                "Your Answer: "
            ).strip()

            # =================================
            # MAIN SCORING
            # =================================

            try:

                score = (
                    scoring_engine.evaluate(question,answer)
                    if scoring_engine
                    else 5)

            except Exception as e:

                print(f"Scoring failed: {e}")
                score = 5

            # =================================
            # FOLLOWUP LOGIC
            # =================================

            level = analyzer.analyze(answer)

            if decision.should_followup(level):

                followup_q = (
                    followup_generator.generate(
                        question,
                        answer,
                        level
                    )
                )

                if followup_q:

                    print(
                        f"\nFollow-up: "
                        f"{followup_q}"
                    )

                    followup_answer = input(
                        "Your Answer: "
                    ).strip()

                    try:

                        followup_score = (
                            scoring_engine.evaluate(
                                followup_q,
                                followup_answer
                            )
                            if scoring_engine
                            else 5)

                    except Exception as e:

                        print(f"Follow-up "
                            f"scoring failed: {e}")

                        followup_score = 5

                    state.update(
                        followup_q,
                        followup_answer,
                        followup_score,
                        followup=True)

            # =================================
            # SAVE MAIN RESPONSE
            # =================================

            state.update(
                question,
                answer,
                score)

            flow.progress()

        # -------------------------------------
        # RESULTS
        # -------------------------------------

        print("\n--- Interview Completed ---\n")

        results = state.get_results()

        print("===== INTERVIEW SUMMARY =====")

        print(json.dumps(
                results,
                indent=4))

        save_results(results)
        return results

# =========================================================
# LEGACY CLI ENTRY
# =========================================================

def run():

    print(
        "\n===== HR Interview Engine =====\n")

    role = input(
        "Enter role: "
    ).strip()

    experience = (
        get_valid_experience())

    pipeline = (
        LegacyFollowupPipeline())

    pipeline.run(
        role=role,
        experience=experience)
# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":

    run()