from app.services.answer_engine_25.intent_classifier import IntentClassifier
from app.services.answer_engine_25.entity_extractor import EntityExtractor
from app.services.answer_engine_25.response_analyzer import ResponseAnalyzer


class AnswerEngine:

    def __init__(self):
        self.intent = IntentClassifier()
        self.extractor = EntityExtractor()
        self.analyzer = ResponseAnalyzer()

    def process(self, text):

        intent = self.intent.classify(text)

        skills = self.extractor.extract_skills(text)
        experience = self.extractor.extract_experience(text)
        salary = self.extractor.extract_salary(text)
        availability = self.extractor.extract_availability(text)

        off_topic = self.analyzer.is_off_topic(text)
        vague = self.analyzer.is_vague(text)

        return {
            "intent": intent,
            "skills": skills,
            "experience": experience,
            "salary": salary,
            "availability": availability,
            "off_topic": off_topic,
            "is_vague": vague
        }