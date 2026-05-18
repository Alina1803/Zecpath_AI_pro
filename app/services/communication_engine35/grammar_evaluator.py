import language_tool_python
import re
import os
import logging
from app.core.language_tool_manager import get_language_tool


# =========================================================
# LOGGING
# =========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


# =========================================================
# TEMP DIRECTORY
# =========================================================

TEMP_DIR = "G:\\temp"

os.makedirs(TEMP_DIR, exist_ok=True)

os.environ["TMPDIR"] = TEMP_DIR
os.environ["TEMP"] = TEMP_DIR


# =========================================================
# OPTIONAL LOCAL LANGUAGETOOL PATH
# =========================================================

os.environ["LANGUAGETOOL_HOME"] = r"G:\LanguageTool"


# =========================================================
# GRAMMAR EVALUATOR
# =========================================================

class GrammarEvaluator:

    def __init__(self):

        try:

            # =========================================
            # SINGLETON LANGUAGETOOL INSTANCE
            # =========================================

            self.tool = get_language_tool()

            logging.info(
                "✅ Shared LanguageTool Instance Loaded"
            )

        except Exception:

            logging.error(
                "❌ Failed To Initialize LanguageTool",
                exc_info=True
            )

            self.tool = None

    # =====================================================
    # MAIN EVALUATION
    # =====================================================

    def evaluate(self, text: str) -> float:

        # =========================================
        # EMPTY INPUT
        # =========================================

        if not text or not text.strip():

            return 0.0

        # =========================================
        # FALLBACK MODE
        # =========================================

        if self.tool is None:

            logging.warning(
                "⚠️ Grammar Tool Not Available → Using Fallback"
            )

            return 50.0

        # =========================================
        # RUN GRAMMAR CHECK
        # =========================================

        try:

            matches = self.tool.check(text)

        except Exception:

            logging.error(
                "⚠️ Grammar Check Failed",
                exc_info=True
            )

            return 50.0

        # =========================================
        # ERROR ANALYSIS
        # =========================================

        grammar_errors = 0
        spelling_errors = 0
        style_issues = 0

        for m in matches:

            issue_type = getattr(
                m,
                "ruleIssueType",
                ""
            )

            if issue_type == 'misspelling':

                spelling_errors += 1

            elif issue_type == 'grammar':

                grammar_errors += 1

            else:

                style_issues += 1

        # =========================================
        # SENTENCE ANALYSIS
        # =========================================

        sentences = re.split(
            r'[.!?]',
            text
        )

        sentences = [
            s.strip()
            for s in sentences
            if s.strip()
        ]

        incomplete_sentences = sum(

            1 for s in sentences

            if len(s.split()) < 3
        )

        # =========================================
        # WEIGHTED ERROR CALCULATION
        # =========================================

        weighted_errors = (

            grammar_errors * 1.0 +

            spelling_errors * 0.8 +

            style_issues * 0.5 +

            incomplete_sentences * 0.7
        )

        word_count = max(
            len(text.split()),
            1
        )

        error_density = (
            weighted_errors / word_count
        )

        # =========================================
        # FINAL SCORE
        # =========================================

        score = (
            1 - error_density
        ) * 100

        score = max(
            min(score, 100),
            0
        )

        return round(score, 2)


# =========================================================
# TESTING
# =========================================================

if __name__ == "__main__":

    evaluator = GrammarEvaluator()

    sample_text = (
        "I think I am confident "
        "but maybe I need improve grammar"
    )

    score = evaluator.evaluate(
        sample_text
    )

    print(
        "Grammar Score:",
        score
    )