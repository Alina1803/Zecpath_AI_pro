import os
import json
from datetime import datetime

from app.services.hr_interview_engine_33.state_manager.interview_state import InterviewState
from app.services.hr_interview_engine_33.question_engine.role_based_generator import RoleBasedQuestionGenerator
from app.services.hr_interview_engine_33.flow_engine.interview_flow import InterviewFlow
from app.services.screening_engine_26.scoring_engine import AdvancedScoringEngine

OUTPUT_DIR = os.path.join("Data", "processed", "output_33")
DOMAIN_BASE_PATH = os.path.join("Data", "domain_knowledge")

def create_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_results(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(OUTPUT_DIR, f"interview_{timestamp}.json")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"\n Results saved to: {file_path}")


def get_valid_experience():
    while True:
        exp = input("Enter experience (fresher/experienced): ").strip().lower()
        if exp in ["fresher", "experienced"]:
            return exp
        print(" Invalid input. Please enter 'fresher' or 'experienced'.")


def load_scoring_dependencies(role):
    role = role.lower()
    base_path = os.path.join(DOMAIN_BASE_PATH, role)

    domain_path = os.path.join(base_path, "domain.json")
    prompt_path = os.path.join(base_path, "prompt.txt")

    if not os.path.exists(domain_path):
        raise FileNotFoundError(f"Missing domain.json at {domain_path}")

    if not os.path.exists(prompt_path):
        raise FileNotFoundError(f"Missing prompt.txt at {prompt_path}")

    with open(domain_path, "r") as f:
        domain_data = json.load(f)

    with open(prompt_path, "r") as f:
        prompt_template = f.read()

    return domain_data, prompt_template


def is_hr_question(question):
    hr_keywords = [
        "background", "career", "goal", "strength",
        "weakness", "relocation", "join", "why"
    ]
    return any(k in question.lower() for k in hr_keywords)


def simple_hr_score(answer):
    """
    Basic HR scoring fallback
    """
    if len(answer.strip()) < 5:
        return 3
    elif len(answer.split()) < 5:
        return 5
    else:
        return 7

def run():

    print("\n===== HR Interview Engine (Day 33) =====\n")

    role = input("Enter role: ").strip()
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

    print("\n--- Interview Started ---")

    for i in range(TOTAL_QUESTIONS):

        print(f"\n Phase: {state.current_phase.upper()}")

        question = flow.get_next_question()

        if not question:
            print(" No question available.")
            break

        print(f"\nQ{i+1}: {question}")
        answer = input("Your Answer: ").strip()

        # ==============================
        # SCORING LOGIC
        # ==============================

        score = None

        # HR Questions
        if is_hr_question(question):
            score = simple_hr_score(answer)

        # Domain Questions
        else:
            if scoring_engine:
                try:
                    score = scoring_engine.evaluate(question, answer)

                    # fallback if engine returns None
                    if score is None:
                        score = 5

                except Exception as e:
                    print(f" Scoring failed: {e}")
                    score = 5
            else:
                score = 5

        # Update state
        state.update(question, answer, score)
        flow.progress()

    print("\n--- Interview Completed ---\n")

    results = state.get_results()

    print("===== INTERVIEW SUMMARY =====")
    print(json.dumps(results, indent=4))

    # Save results
    create_output_dir()
    save_results(results)


# ==============================
# ENTRY POINT
# ==============================

if __name__ == "__main__":
    run()