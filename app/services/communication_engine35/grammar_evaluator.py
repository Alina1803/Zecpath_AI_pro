import language_tool_python
import re
import os
import logging
import threading


# ✅ Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


# 🔧 Temp directory
TEMP_DIR = "G:\\temp"
os.makedirs(TEMP_DIR, exist_ok=True)

os.environ["TMPDIR"] = TEMP_DIR
os.environ["TEMP"] = TEMP_DIR


# ✅ IMPORTANT: Set local LanguageTool path (used by library internally)
os.environ["LANGUAGETOOL_HOME"] = r"G:\LanguageTool"


class GrammarEvaluator:

    def __init__(self):
        self.tool = None

        def init_tool():
            try:
                self.tool = language_tool_python.LanguageToolPublicAPI('en-US',
                    remote_server='http://localhost:8081')
                logging.info(" Connected to local Language Tool ")

            except Exception:
                logging.error(" LanguageTool init failed", exc_info=True)
                self.tool = None

        # 🔥 Prevent freezing using thread + timeout
        thread = threading.Thread(target=init_tool)
        thread.start()
        thread.join(timeout=15)

        if thread.is_alive():
            logging.error("❌ LanguageTool init TIMEOUT → disabling tool")
            self.tool = None

    def evaluate(self, text: str) -> float:

        if not text or not text.strip():
            return 0.0

        if self.tool is None:
            logging.warning("⚠️ Tool not available, using fallback")
            return 50.0

        try:
            matches = self.tool.check(text)
        except Exception:
            logging.error("⚠️ Grammar check failed", exc_info=True)
            return 50.0

        # 🔍 Error categorization
        grammar_errors = 0
        spelling_errors = 0
        style_issues = 0

        for m in matches:
            issue_type = getattr(m, "ruleIssueType", "")

            if issue_type == 'misspelling':
                spelling_errors += 1
            elif issue_type == 'grammar':
                grammar_errors += 1
            else:
                style_issues += 1

        # 🧠 Sentence analysis
        sentences = re.split(r'[.!?]', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        incomplete_sentences = sum(
            1 for s in sentences if len(s.split()) < 3
        )

        # ⚖️ Weighted errors
        weighted_errors = (
            grammar_errors * 1.0 +
            spelling_errors * 0.8 +
            style_issues * 0.5 +
            incomplete_sentences * 0.7
        )

        word_count = max(len(text.split()), 1)
        error_density = weighted_errors / word_count

        score = (1 - error_density) * 100
        score = max(min(score, 100), 0)

        return round(score, 2)


# ✅ Test
if __name__ == "__main__":
    evaluator = GrammarEvaluator()

    sample_text = "I think I am confident but maybe I need improve grammar"

    score = evaluator.evaluate(sample_text)

    print("Grammar Score:", score)