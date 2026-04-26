import random


class CategorySelector:
    """
    Selects appropriate interview categories based on:
    - Interview phase
    - Role type
    - Experience level
    - Previously asked categories (to avoid repetition)
    """

    def __init__(self, role: str, experience: str):
        self.role = role.lower()
        self.experience = experience.lower()
        self.used_categories = set()

        # Define base categories per phase
        self.phase_categories = {
            "introduction": ["self_intro"],
            "core": [
                "career_journey",
                "strengths_weaknesses",
                "teamwork"
            ],
            "evaluation": ["goals"],
            "closing": ["availability"]
        }

        # Role-based category extensions
        self.role_category_map = {
            "technical": ["problem_solving", "learning_ability"],
            "non_technical": ["communication", "adaptability"]
        }

    # ------------------------------
    # PUBLIC METHOD
    # ------------------------------
    def get_category(self, phase: str) -> str:
        """
        Returns the next category based on logic
        """

        phase = phase.lower()

        base_categories = self.phase_categories.get(phase, [])

        # Add role-based categories if in evaluation phase
        if phase == "evaluation":
            role_type = self._detect_role_type()
            base_categories += self.role_category_map.get(role_type, [])

        # Remove already used categories
        available = [
            cat for cat in base_categories
            if cat not in self.used_categories
        ]

        # Reset if exhausted
        if not available:
            available = base_categories

        selected = random.choice(available)

        self.used_categories.add(selected)

        return selected

    # ------------------------------
    # INTERNAL HELPERS
    # ------------------------------
    def _detect_role_type(self) -> str:
        """
        Basic heuristic to classify role
        """

        technical_keywords = [
            "engineer", "developer", "data", "analyst",
            "scientist", "software", "it", "ai", "ml"
        ]

        for keyword in technical_keywords:
            if keyword in self.role:
                return "technical"

        return "non_technical"