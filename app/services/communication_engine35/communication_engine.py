from app.services.communication_engine35.fluency_checker import FluencyChecker
from app.services.communication_engine35.grammar_evaluator import GrammarEvaluator
from app.services.communication_engine35.vocabulary_analyzer import VocabularyAnalyzer
from app.services.communication_engine35.clarity_scorer import ClarityScorer
from app.services.communication_engine35.filler_detector import FillerDetector
from app.services.communication_engine35.structure_analyzer import StructureAnalyzer
from app.services.communication_engine35.score_aggregator import ScoreAggregator
from app.services.communication_engine35.normalization import Normalizer


class CommunicationEngine:

    def __init__(self):
        self.fluency = FluencyChecker()
        self.grammar = GrammarEvaluator()
        self.vocab = VocabularyAnalyzer()
        self.clarity = ClarityScorer()
        self.filler = FillerDetector()
        self.structure = StructureAnalyzer()
        self.aggregator = ScoreAggregator()
        self.normalizer = Normalizer()

    def evaluate(self, text: str):

        scores = {
            "fluency": self.fluency.evaluate(text),
            "grammar": self.grammar.evaluate(text),
            "vocabulary": self.vocab.evaluate(text),
            "clarity": self.clarity.evaluate(text),
            "filler": self.filler.evaluate(text),
            "structure": self.structure.evaluate(text)
        }

        final_score = self.aggregator.aggregate(scores)
        final_score = self.normalizer.normalize(final_score)

        return {
            "component_scores": scores,
            "final_score": final_score
        }
    