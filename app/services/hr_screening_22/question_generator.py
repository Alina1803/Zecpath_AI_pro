import json
import random


def generate_ca_questions():

    # ==========================================
    # LOAD CATEGORY MAPPING
    # ==========================================

    try:

        with open(
            "app/services/hr_screening_22/dataset/category_mapping.json",
            "r",
            encoding="utf-8"
        ) as f:

            category_data = json.load(f)

    except Exception as e:

        print(f"Category Mapping Load Error: {e}")

        return []

    # ==========================================
    # GET SKILLS
    # ==========================================

    skills = (
        category_data
        .get("skills", {})
        .get("skills", [])
    )

    # ==========================================
    # FALLBACK SKILLS
    # ==========================================

    if not skills:

        skills = [
            "GST",
            "Income Tax",
            "Audit"
        ]

    # ==========================================
    # SHUFFLE QUESTIONS
    # ==========================================

    random.shuffle(skills)

    # ==========================================
    # GENERATE QUESTIONS
    # ==========================================

    questions = []

    for skill in skills:

        questions.append(
            f"Do you have experience in {skill}?"
        )

    return questions