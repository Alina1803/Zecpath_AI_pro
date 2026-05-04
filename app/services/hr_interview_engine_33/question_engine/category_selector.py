import random


class CategorySelector:
    """
    Selects appropriate interview categories based on:
    - Interview phase
    - Role type (technical / non-technical)
    - Experience level
    - Avoids repeating categories
    """

    def __init__(self, role: str, experience: str):
        self.role = role.lower()
        self.experience = experience.lower()
        self.used_categories = set()

        # ✅ MUST MATCH hr_questions.json categories
        self.phase_categories = {
            "introduction": [
                "self_introduction"
            ],

            "core": [
                "career_journey",
                "strengths_weaknesses",
                "teamwork",
                "conflict_resolution"
            ],

            "evaluation": [
                "career_goals",
                "adaptability",
                "motivation",
                "communication"
            ],

            "closing": [
                "availability"
            ]
        }

        # ✅ Role-based category extensions
        self.role_category_map = {
            "technical": [
                "problem_solving",
                "learning_ability"
            ],
            "non_technical": [
                "communication",
                "adaptability"
            ]
        }

    # ------------------------------
    # PUBLIC METHOD
    # ------------------------------
    def get_category(self, phase: str) -> str:
        """
        Returns next category intelligently
        """

        phase = phase.lower()

        # ✅ Copy list to avoid mutation bug
        base_categories = list(self.phase_categories.get(phase, []))

        # ✅ Add role-based categories during evaluation
        if phase == "evaluation":
            role_type = self._detect_role_type()
            base_categories += self.role_category_map.get(role_type, [])

        # ✅ Remove duplicates
        base_categories = list(set(base_categories))

        # ✅ Remove already used categories
        available = [
            cat for cat in base_categories
            if cat not in self.used_categories
        ]

        # ✅ Reset if all used
        if not available:
            available = base_categories

        selected = random.choice(available)

        self.used_categories.add(selected)

        return selected

    # ------------------------------
    # INTERNAL HELPER
    # ------------------------------
    def _detect_role_type(self) -> str:
        """
        Detects if role is technical or non-technical
        """

        technical_keywords = [
            "engineer", "developer", "data",
            "analyst", "scientist", "software",
            "it", "ai", "ml"
        ]

        for keyword in technical_keywords:
            if keyword in self.role:
                return "technical"

        return "non_technical"