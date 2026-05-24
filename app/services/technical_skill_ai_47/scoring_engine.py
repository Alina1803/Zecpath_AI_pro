from app.services.technical_skill_ai_47.depth_detector import detect_depth
from app.services.technical_skill_ai_47.logic_engine import logical_score
from app.services.technical_skill_ai_47.realworld_engine import real_world_score
from app.services.technical_skill_ai_47.difficulty_engine import normalize_difficulty
from app.services.technical_skill_ai_47.explain_engine import generate_explanation


# -------------------------------
# Accuracy Score
# -------------------------------

def accuracy_score(is_correct):
    return 1.0 if is_correct else 0.4


# -------------------------------
# Final Technical Score
# -------------------------------

def calculate_technical_score(answer, difficulty, is_correct=True):

    depth = detect_depth(answer)

    logic = logical_score(answer)

    real_world = real_world_score(answer)

    accuracy = accuracy_score(is_correct)

    final = (
        accuracy * 0.35 +
        depth * 0.25 +
        logic * 0.20 +
        real_world * 0.20
    )

    percentage = round(final * 100, 2)

    normalized = normalize_difficulty(
        percentage,
        difficulty
    )

    return {
        "technical_score": normalized,
        "breakdown": {
            "accuracy": round(accuracy, 2),
            "depth": round(depth, 2),
            "logic": round(logic, 2),
            "real_world": round(real_world, 2)
        },
        "explanation": generate_explanation(answer)
    }