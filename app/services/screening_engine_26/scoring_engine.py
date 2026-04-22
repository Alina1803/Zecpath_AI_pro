from app.services.screening_engine_26.llm_evaluator import evaluate_with_llm
from app.services.screening_engine_26.semantic_matcher import compute_similarity
from app.services.screening_engine_26.domain_evaluator import domain_score
from app.services.screening_engine_26.weights_config import WEIGHTS
from app.services.screening_engine_26.calibration import calibrate

from app.utils.text_preprocessor import TextPreprocessor


class AdvancedScoringEngine:

    # ✅ FIXED constructor
    def __init__(self, domain_data, prompt_template):
        self.domain_data = domain_data
        self.prompt_template = prompt_template

    def evaluate(self, question, answer, expected_answer):

        # ✅ CLEAN TEXT (correct place)
        clean_answer = TextPreprocessor.clean_text(answer)

        # ✅ LLM with prompt
        llm_scores = evaluate_with_llm(
            question,
            clean_answer,
            self.prompt_template
        )

        # ✅ semantic similarity
        semantic = compute_similarity(clean_answer, expected_answer)

        # ✅ domain scoring with config
        domain = domain_score(clean_answer, self.domain_data)

        # ✅ weighted score
        final_score = (
            llm_scores["clarity"] * WEIGHTS["clarity"] +
            llm_scores["relevance"] * WEIGHTS["relevance"] +
            llm_scores["completeness"] * WEIGHTS["completeness"] +
            llm_scores["consistency"] * WEIGHTS["consistency"] +
            semantic * WEIGHTS["semantic"] +
            domain * WEIGHTS["domain"]
        ) * 10

        final_score = calibrate(final_score)

        return {
            "question": question,
            "answer": answer,
            "llm_scores": llm_scores,
            "semantic_score": semantic,
            "domain_score": domain,
            "final_score": final_score,
            "technical_confidence": round((semantic + domain) / 2, 2)
        }