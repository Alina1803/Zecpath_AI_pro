import os

from app.services.ai_conversation_system_29.flows.decision_tree import decide_next_step
from app.services.ai_conversation_system_29.flows.state_machine import ConversationState
from app.services.ai_conversation_system_29.flows.fallback_handler import fallback_response
from app.services.ai_conversation_system_29.questions.question_bank import get_questions
from app.services.ai_conversation_system_29.evaluation.evaluator import evaluate_answer
from app.services.ai_conversation_system_29.evaluation.scoring import score_answer
from app.services.ai_conversation_system_29.responses.templates import get_feedback
from app.services.ai_conversation_system_29.responses.retry_messages import retry_message
from app.utils.logger import log
from app.utils.helpers import clean_input


def save_output(interview_log, total_score):
    output_dir = "data/processed"
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "output_29.txt")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("AI Interview Output\n")
        file.write("=" * 40 + "\n\n")

        for line in interview_log:
            file.write(line + "\n")

        file.write(f"\nFinal Score: {total_score}\n")

    print(f"\n📁 Output saved to: {output_file}")


def run_interview():
    state = ConversationState()
    questions = get_questions()

    retry_count = 0
    total_score = 0
    interview_log = []

    print("AI Interviewer: Welcome! Let's begin your interview.\n")
    interview_log.append("Interview Started")

    for i, question in enumerate(questions):
        print(f"AI: {question}")
        interview_log.append(f"Q{i+1}: {question}")

        while True:
            user_input = input("You: ")
            user_input = clean_input(user_input)

            interview_log.append(f"Candidate: {user_input}")

            action = decide_next_step(user_input)
            current_state = state.transition(action)

            log(f"Q{i} | State: {current_state}, Action: {action}")

            # Silence handling
            if action == "handle_silence":
                retry_count += 1
                message = retry_message(retry_count)
                print("AI:", message)

                interview_log.append(f"AI: {message}")

                if retry_count >= 3:
                    end_msg = fallback_response(retry_count)
                    print("AI:", end_msg)
                    print("AI: Interview terminated due to no response.")

                    interview_log.append(f"AI: {end_msg}")
                    save_output(interview_log, total_score)
                    return
                continue

            # Evaluation
            result = evaluate_answer(user_input)
            score = score_answer(result)
            total_score += score

            feedback = get_feedback(result)

            print("AI:", feedback)

            interview_log.append(f"Evaluation: {result}")
            interview_log.append(f"Score: {score}")
            interview_log.append(f"AI Feedback: {feedback}")

            retry_count = 0
            break

    print("\n✅ Interview Completed")
    print("📊 Total Score:", total_score)

    interview_log.append("Interview Completed")
    interview_log.append(f"Final Score: {total_score}")

    save_output(interview_log, total_score)


if __name__ == "__main__":
    run_interview()