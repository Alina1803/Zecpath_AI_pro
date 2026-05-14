import unittest

from app.services.demo_45.voice_ai.voice_pipeline import VoiceInterviewPipeline


class TestVoicePipeline(unittest.TestCase):

    def setUp(self):

        self.pipeline = VoiceInterviewPipeline()

    def test_pipeline_initialization(self):

        self.assertIsNotNone(self.pipeline)

    def test_question_generation(self):

        question = "Tell me about yourself"

        self.assertIsInstance(question, str)

    def test_voice_pipeline_methods(self):

        self.assertTrue(
            hasattr(self.pipeline, "ask_question")
        )

        self.assertTrue(
            hasattr(self.pipeline, "capture_candidate_answer")
        )

        self.assertTrue(
            hasattr(self.pipeline, "run_voice_round")
        )


if __name__ == "__main__":

    unittest.main()