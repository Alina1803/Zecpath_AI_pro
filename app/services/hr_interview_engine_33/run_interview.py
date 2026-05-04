import os
import json
from datetime import datetime

from app.services.hr_interview_engine_33.state_manager.interview_state import InterviewState
from app.services.hr_interview_engine_33.question_engine.role_based_generator import RoleBasedQuestionGenerator
from app.services.hr_interview_engine_33.flow_engine.interview_flow import InterviewFlow
from app.services.screening_engine_26.scoring_engine import AdvancedScoringEngine


# ✅ Use consistent lowercase path
OUTPUT_DIR = os.path.join("data", "processed", "output_33")
DOMAIN_BASE_PATH = os.path.join("data", "domain_knowledge")


# ----------------------------------
# FILE HELPERS
# ----------------------------------
def create_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_results(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(OUTPUT_DIR, f"interview_{timestamp}.json")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\n Results saved to: {file_path}")


# ----------------------------------
# INPUT VALIDATION
# ----------------------------------
def get_valid_experience():
    while True:
        exp = input("Enter experience (fresher/experienced): ").strip().lower()
        if exp in ["fresher", "experienced"]:
            return exp
        print(" Invalid input. Please enter 'fresher' or 'experienced'.")


# ----------------------------------
# SCORING SETUP
# ----------------------------------
def load_scoring_dependencies(role):
    role = role.lower()
    base_path = os.path.join(DOMAIN_BASE_PATH, role)

    domain_path = os.path.join(base_path, "domain.json")
    prompt_path = os.path.join(base_path, "prompt.txt")

    if not os.path.exists(domain_path) or not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Missing scoring files for role: {role}")

    with open(domain_path, "r") as f:
        domain_data = json.load(f)

    with open(prompt_path, "r") as f:
        prompt_template = f.read()

    return domain_data, prompt_template


# ----------------------------------
# HR FALLBACK SCORING
# ----------------------------------
def simple_hr_score(answer):
    words = answer.strip().split()

    if len(words) < 3:
        return 3
    elif len(words) < 8:
        return 5
    else:
        return 7


# ----------------------------------
# SIMPLE FOLLOW-UP DECISION
# ----------------------------------
class SimpleDecision:
    def should_followup(self, level):
        return level == "low"


# ----------------------------------
# MAIN RUNNER
# ----------------------------------
def run():

    print("\n===== HR Interview Engine (Final Updated) =====\n")

    role = input("Enter role: ").strip().lower()
    experience = get_valid_experience()

    # Core components
    state = InterviewState(role, experience)
    generator = RoleBasedQuestionGenerator(role, experience)
    flow = InterviewFlow(state, generator)

    # Initialize scoring engine
    scoring_engine = None

    try:
        domain_data, prompt_template = load_scoring_dependencies(role)
        scoring_engine = AdvancedScoringEngine(domain_data, prompt_template)
        print(" Scoring Engine Initialized")
    except Exception as e:
        print(f" Scoring Engine Disabled: {e}")

    TOTAL_QUESTIONS = 6
    decision_engine = SimpleDecision()

    print("\n--- Interview Started ---")

    for i in range(TOTAL_QUESTIONS):

        print(f"\n Phase: {state.current_phase.upper()}")

        q_data = flow.get_next_question()

        if not q_data or "question" not in q_data:
            print(" No valid question available.")
            break

        question_text = q_data.get("question", "No question")
        q_type = q_data.get("type", "unknown")

        print(f"\nQ{i+1} [{q_type.upper()}]: {question_text}")
        answer = input("Your Answer: ").strip()

        # ==============================
        # SCORING
        # ==============================
        score = 5

        if q_type == "hr":
            score = simple_hr_score(answer)

        else:
            if scoring_engine:
                try:
                    score = scoring_engine.evaluate(question_text, answer)
                    if score is None:
                        score = 5
                except Exception as e:
                    print(f" Scoring failed: {e}")
                    score = 5

        # ==============================
        # UPDATE STATE
        # ==============================
        state.update(q_data, answer, score)

        # ==============================
        # FOLLOW-UP
        # ==============================
        followup, level = flow.handle_followup(
            q_data,
            answer,
            analyzer=None,
            followup_generator=None,
            decision=decision_engine
        )

        if followup:
            print(f"\n Follow-up: {followup}")
            fu_answer = input("Your Answer: ").strip()
            state.update(q_data, fu_answer, score, followup=True)

        # ==============================
        # NEXT PHASE
        # ==============================
        flow.progress()

    print("\n--- Interview Completed ---\n")

    results = state.get_results()

    print("===== INTERVIEW SUMMARY =====")
    print(json.dumps(results, indent=4))

    create_output_dir()
    save_results(results)


# ----------------------------------
# ENTRY POINT
# ----------------------------------
if __name__ == "__main__":
    run()