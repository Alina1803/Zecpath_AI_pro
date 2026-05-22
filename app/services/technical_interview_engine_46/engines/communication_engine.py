from app.services.communication_engine35.communication_engine import (
    CommunicationEngine as BaseCommunicationEngine
)


class TechnicalCommunicationEngine:

    def __init__(self):

        self.engine = BaseCommunicationEngine()

    def evaluate(self, text):

        return self.engine.evaluate(text)