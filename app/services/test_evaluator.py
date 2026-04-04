from typing import Dict, List
import traceback


class TestEvaluator:

    # ------------------------------
    # MCQ Evaluation
    # ------------------------------
    def evaluate_mcq(self, candidate_answers: Dict, correct_answers: Dict) -> Dict:
        total_questions = len(correct_answers)
        correct_count = 0

        for question_id, correct_answer in correct_answers.items():
            if candidate_answers.get(question_id) == correct_answer:
                correct_count += 1

        score_percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0

        return {
            "total_questions": total_questions,
            "correct_answers": correct_count,
            "score_percentage": round(score_percentage, 2)
        }

    # ------------------------------
    # Coding Evaluation (Basic)
    # ------------------------------
    def evaluate_coding(self, submitted_code: str, test_cases: List[Dict]) -> Dict:
        """
        test_cases format:
        [
            {"input": 5, "expected_output": 25},
            {"input": 3, "expected_output": 9}
        ]
        """

        passed = 0
        results = []

        try:
            local_env = {}
            exec(submitted_code, {}, local_env)

            if "solution" not in local_env:
                return {
                    "passed": 0,
                    "total": len(test_cases),
                    "score_percentage": 0,
                    "error": "Function 'solution' not defined"
                }

            solution_func = local_env["solution"]

            for case in test_cases:
                output = solution_func(case["input"])
                is_correct = output == case["expected_output"]

                if is_correct:
                    passed += 1

                results.append({
                    "input": case["input"],
                    "expected": case["expected_output"],
                    "output": output,
                    "passed": is_correct
                })

        except Exception as e:
            return {
                "passed": 0,
                "total": len(test_cases),
                "score_percentage": 0,
                "error": traceback.format_exc()
            }

        total_cases = len(test_cases)
        score_percentage = (passed / total_cases) * 100 if total_cases > 0 else 0

        return {
            "passed": passed,
            "total": total_cases,
            "score_percentage": round(score_percentage, 2),
            "details": results
        }

    # ------------------------------
    # Combined Evaluation
    # ------------------------------
    def evaluate_full_test(
        self,
        mcq_answers: Dict,
        mcq_correct: Dict,
        submitted_code: str,
        coding_test_cases: List[Dict]
    ) -> Dict:

        mcq_result = self.evaluate_mcq(mcq_answers, mcq_correct)
        coding_result = self.evaluate_coding(submitted_code, coding_test_cases)

        final_score = (
            0.4 * mcq_result["score_percentage"] +
            0.6 * coding_result["score_percentage"]
        )

        return {
            "mcq_result": mcq_result,
            "coding_result": coding_result,
            "final_test_score": round(final_score, 2)
        }