import re
import logging

logger = logging.getLogger(__name__)


class GrammarEvaluator:

    def __init__(self):

        logger.info(
            "✅ Lightweight GrammarEvaluator Loaded"
        )

    # =====================================================
    # MAIN EVALUATION
    # =====================================================

    def evaluate(self, text: str) -> float:

        if not text or not text.strip():

            return 0.0

        words = text.split()

        word_count = len(words)

        unique_words = len(set(words))

        # =================================================
        # BASE SCORE
        # =================================================

        score = 85

        # =================================================
        # SHORT ANSWER PENALTY
        # =================================================

        if word_count < 5:

            score -= 20

        elif word_count < 15:

            score -= 10

        # =================================================
        # REPETITION PENALTY
        # =================================================

        repetition_ratio = (

            (word_count - unique_words)

            / max(word_count, 1)
        )

        if repetition_ratio > 0.3:

            score -= 10

        # =================================================
        # LONG SENTENCE PENALTY
        # =================================================

        sentences = re.split(
            r"[.!?]",
            text
        )

        sentences = [
            s.strip()
            for s in sentences
            if s.strip()
        ]

        avg_sentence_length = (

            word_count

            / max(len(sentences), 1)
        )

        if avg_sentence_length > 25:

            score -= 10

        # =================================================
        # LOWERCASE START PENALTY
        # =================================================

        if text and text[0].islower():

            score -= 5

        # =================================================
        # FINAL SCORE
        # =================================================

        score = max(
            min(score, 100),
            40
        )

        return round(score, 2)


# =========================================================
# TESTING
# =========================================================

if __name__ == "__main__":

    evaluator = GrammarEvaluator()

    sample = (
        "I have worked with FastAPI, "
        "Docker and scalable backend systems."
    )

    result = evaluator.evaluate(sample)

    print(result)