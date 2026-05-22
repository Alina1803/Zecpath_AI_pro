import json
import os
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

from app.services.technical_interview_engine_46.engines.role_mapper import RoleMapper

from app.services.technical_interview_engine_46.engines.experience_engine import ExperienceEngine

from app.services.technical_interview_engine_46.engines.question_engine import QuestionEngine

from app.services.technical_interview_engine_46.engines.followup_engine import FollowUpEngine

from app.services.technical_interview_engine_46.engines.technical_evaluator import TechnicalEvaluator

from app.services.technical_interview_engine_46.engines.coding_evaluator import CodingEvaluator

from app.services.technical_interview_engine_46.engines.confidence_engine import ConfidenceEngine

from app.services.technical_interview_engine_46.engines.communication_engine import TechnicalCommunicationEngine

from app.services.technical_interview_engine_46.engines.scoring_engine import ScoringEngine

from app.services.technical_interview_engine_46.engines.report_generator import ReportGenerator


# =====================================================
# FASTAPI APP
# =====================================================

app = FastAPI(
    title="Technical Interview AI Engine",
    version="46.0"
)

# =====================================================
# OUTPUT DIRECTORY
# =====================================================

OUTPUT_DIR = os.path.join(
    "data","processed","output_46")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================================
# REQUEST MODEL
# =====================================================

class InterviewRequest(BaseModel):

    candidate_id: str

    candidate_name: str

    resume_text: str

    answer: str

    coding_answer: str

    duration_seconds: int


# =====================================================
# SAVE REPORT
# =====================================================


def save_report(report_data):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S")

    filename = (
        f"technical_interview_report_{timestamp}.json")

    filepath = os.path.join(
        OUTPUT_DIR,filename)

    with open(filepath, "w") as file:

        json.dump(
            report_data,
            file,
            indent=4)

    return filepath


# =====================================================
# INTERVIEW API
# =====================================================

@app.post("/technical-interview/run")


def run_interview(request: InterviewRequest):

    # =================================================
    # ROLE DETECTION
    # =================================================

    role_mapper = RoleMapper()

    role_data = role_mapper.detect(
        request.resume_text)

    role = (
        role_data["role"]
        if role_data
        else "Python Developer")

    # =================================================
    # EXPERIENCE ANALYSIS
    # =================================================

    experience_engine = ExperienceEngine()

    experience_result = (
        experience_engine.analyze(
            request.resume_text))

    experience_level = (
        experience_result["level"])

    # =================================================
    # QUESTION GENERATION
    # =================================================

    question_engine = QuestionEngine()

    question = question_engine.get_question(
        skill="Python",
        difficulty="intermediate",
        filename="python_questions.json"
    )

    # =================================================
    # TECHNICAL EVALUATION
    # =================================================

    technical_result = (
        TechnicalEvaluator.evaluate(
            request.answer
        )
    )

    # =================================================
    # FOLLOW-UP QUESTION
    # =================================================

    followup_engine = FollowUpEngine()

    followup_question = (
        followup_engine.generate(
            question,
            request.answer,
            technical_result["quality"]
        )
    )

    # =================================================
    # CODING EVALUATION
    # =================================================

    coding_score = (
        CodingEvaluator.evaluate(
            request.coding_answer
        )
    )

    # =================================================
    # CONFIDENCE ANALYSIS
    # =================================================

    confidence_result = (
        ConfidenceEngine.analyze(
            request.answer,
            request.duration_seconds
        )
    )

    # =================================================
    # COMMUNICATION ANALYSIS
    # =================================================

    communication_engine = (
        TechnicalCommunicationEngine()
    )

    communication_result = (
        communication_engine.evaluate(
            request.answer
        )
    )

    # =================================================
    # FINAL SCORING
    # =================================================

    scoring_engine = ScoringEngine()

    final_result = scoring_engine.calculate({

        "technical_score":
            technical_result[
                "technical_score"
            ] * 10,

        "coding_score":
            coding_score * 10,

        "communication_score":
            communication_result[
                "final_score"
            ],

        "confidence_score":
            confidence_result[
                "confidence_score"
            ],

        "system_design_score":
            75,

        "semantic_score":
            82,

        "domain_score":
            80,

        "experience_level":
            experience_level
    })

    # =================================================
    # FINAL REPORT
    # =================================================

    report_data = {

        "candidate_id":
            request.candidate_id,

        "candidate_name":
            request.candidate_name,

        "role":
            role,

        "experience_level":
            experience_level,

        "question":
            question,

        "followup_question":
            followup_question,

        "technical_score":
            final_result[
                "technical_score"
            ],

        "coding_score":
            final_result[
                "coding_score"
            ],

        "communication_score":
            final_result[
                "communication_score"
            ],

        "confidence_score":
            final_result[
                "confidence_score"
            ],

        "system_design_score":
            final_result[
                "system_design_score"
            ],

        "semantic_score":
            final_result[
                "semantic_score"
            ],

        "domain_score":
            final_result[
                "domain_score"
            ],

        "final_score":
            final_result[
                "final_score"
            ],

        "performance":
            final_result[
                "performance"
            ],

        "recommendation":
            final_result[
                "recommendation"
            ],

        "decision":
            final_result[
                "decision"
            ],

        "strengths":
            final_result[
                "strengths"
            ],

        "weaknesses":
            final_result[
                "weaknesses"
            ],

        "risks":
            final_result[
                "risks"
            ],

        "generated_at":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
    }

    # =================================================
    # SAVE OUTPUT
    # =================================================

    saved_path = save_report(
        report_data
    )

    # =================================================
    # RETURN RESPONSE
    # =================================================

    return {

        "status": "success",

        "message":
            "Technical interview completed",

        "saved_to":
            saved_path,

        "report":
            report_data
    }


# =====================================================
# ROOT API
# =====================================================

@app.get("/")


def root():

    return {

        "message":
            "Technical Interview AI Engine Running"
    }


# =====================================================
# RUN SERVER
# =====================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "",
        host="127.0.0.1",
        port=8000,
        reload=True
    )