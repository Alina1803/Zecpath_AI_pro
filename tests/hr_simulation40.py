import random
from datetime import datetime

from app.services.hr_simulation_40.interview_engine import InterviewManager


def simulate_candidate(candidate_type):
    interview = InterviewManager(candidate_type)

    result = interview.run()

    ai_score = result["final_score"]
    human_score = ai_score + random.randint(-5, 5)

    return {
        "candidate_type": candidate_type,
        "timestamp": datetime.now().isoformat(),

        # Interview Data
        "responses": result["responses"],

        # Scores
        "ai_score": ai_score,
        "human_score": human_score,

        # Decisions
        "decision_ai": result["decision"],
    }


def run_simulation(n=40, seed=42):
    """
    Run full simulation with reproducibility
    """
    random.seed(seed)

    types = ["Confident", "Hesitant", "Inexperienced", "Overqualified"]

    results = [
        simulate_candidate(random.choice(types))
        for _ in range(n)
    ]

    return results