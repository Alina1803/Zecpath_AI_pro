import unittest

from app.services.demo_45.final_hr_engine import run_final_hr_pipeline

class TestFinalHRSystem(unittest.TestCase):

    def setUp(self):

        self.candidate_data = {
            "candidate_id": "C1001",
            "role": "Backend Developer",
            "experience": "2 Years"
        }

    def test_pipeline_execution(self):

        result = run_final_hr_pipeline(
            self.candidate_data
        )

        self.assertIn("candidate", result)

        self.assertIn("scores", result)

        self.assertIn("summary", result)

    def test_final_score_exists(self):

        result = run_final_hr_pipeline(
            self.candidate_data
        )

        self.assertIn(
            "final_score",
            result["scores"]
        )

    def test_decision_generation(self):

        result = run_final_hr_pipeline(
            self.candidate_data
        )

        self.assertIn(
            result["scores"]["decision"],
            ["HIRE", "REVIEW", "REJECT"]
        )


if __name__ == "__main__":

    unittest.main()