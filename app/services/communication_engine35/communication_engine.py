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

    # =====================================================
    # INVALID / NOISE TRANSCRIPT DETECTION
    # =====================================================

    def is_invalid_response(self, text: str):

        if not text:
            return True

        text = str(text).strip().lower()

        # ================================================
        # EMPTY / SYMBOL RESPONSES
        # ================================================

        invalid_patterns = [

            ".",
            "..",
            ". .",
            "...",
            "music",
            "music music",
            "thank you",
            "bye",
            "okay",
            "ok",
            "hmm",
            "uh",
            "noise",
            "[music]"
        ]

        if text in invalid_patterns:
            return True

        # ================================================
        # VERY SHORT RESPONSE
        # ================================================

        word_count = len(text.split())

        if word_count <= 2:
            return True

        return False

    # =====================================================
    # MAIN EVALUATION
    # =====================================================

    def evaluate(self, text: str):

        # ================================================
        # NORMALIZE INPUT
        # ================================================

        text = str(text).strip()

        # ================================================
        # HANDLE INVALID RESPONSES
        # ================================================

        if self.is_invalid_response(text):

            return {

                "component_scores": {

                    "fluency": 0,

                    "grammar": 0,

                    "vocabulary": 0,

                    "clarity": 0,

                    "filler": 0,

                    "structure": 0
                },

                "final_score": 0,

                "status": "invalid_response",

                "reason": (
                    "Noise / Empty / Very Short "
                    "candidate response detected"
                )
            }

        # ================================================
        # COMPONENT SCORING
        # ================================================

        scores = {

            "fluency": (
                self.fluency.evaluate(text)
            ),

            "grammar": (
                self.grammar.evaluate(text)
            ),

            "vocabulary": (
                self.vocab.evaluate(text)
            ),

            "clarity": (
                self.clarity.evaluate(text)
            ),

            "filler": (
                self.filler.evaluate(text)
            ),

            "structure": (
                self.structure.evaluate(text)
            )
        }

        # ================================================
        # FINAL SCORE
        # ================================================

        final_score = (
            self.aggregator.aggregate(scores)
        )

        final_score = (
            self.normalizer.normalize(final_score)
        )

        # ================================================
        # LOW QUALITY RESPONSE PENALTY
        # ================================================

        word_count = len(text.split())

        if word_count < 8:

            final_score = max(
                0,
                final_score - 20
            )

        # ================================================
        # FINAL OUTPUT
        # ================================================

        return {

            "component_scores": scores,

            "final_score": round(
                final_score,
                2
            ),

            "status": "success",

            "word_count": word_count
        }