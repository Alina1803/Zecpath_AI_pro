from app.services.hr_interview_engine_33.question_engine.category_selector import CategorySelector

class InterviewFlow:

    def __init__(self, state, generator):
        self.state = state
        self.generator = generator
        self.selector = CategorySelector(state.role, state.experience)

        self.phase_categories = {
            "introduction": ["self_intro"],
            "core": ["career_journey", "strengths_weaknesses", "teamwork"],
            "evaluation": ["goals"],
            "closing": ["availability"]
        }

    def get_next_question(self):
        categories = self.phase_categories[self.state.current_phase]

        for category in categories:
            return self.generator.get_question(category)
        
    def progress(self):
        self.state.next_phase()