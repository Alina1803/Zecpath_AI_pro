import os
import uuid
import logging

from datetime import datetime

from app.readers.pdf_reader import extract_text_from_pdf
from app.services.parsers.resume_parser import parse_resume
from app.services.scoring import calculate_score
from app.services.feature_store import extract_features
from app.services.technical_interview_engine_46.run_engine46 import (
    InterviewRequest,
    run_interview,
)

from app.services.hr_interview_engine_33.run_interview import LegacyInterviewEngine

from app.services.behavioural_engine48.scoring_engine import behavioral_pipeline

from app.services.machine_test_50.scoring_pipeline import machine_test_pipeline

from app.services.integrity_engine_49.scoring_pipeline import integrity_pipeline

from app.services.unified_scoring_engine_41.pipeline.unified_pipeline import (
    unified_pipeline,
)

from app.services.report_engine_28.report_generator import ReportGenerator

from app.services.simulation_56.candidate_generator import generate_candidates

from app.services.simulation_56.ai_human_comparison import AIHumanComparison

from app.services.simulation_56.consistency_checker import ConsistencyChecker

from app.services.simulation_56.performance_analyzer import PerformanceAnalyzer

from app.services.simulation_56.drift_detector import DriftDetector

from app.services.simulation_56.production_validator import ProductionValidator

from app.services.simulation_56.analytics.funnel_analyzer import FunnelAnalyzer

from app.services.simulation_56.reports.recommendation_engine import (
    RecommendationEngine,
)

from app.services.simulation_56.reports.performance_dashboard import (
    PerformanceDashboard,
)

from app.services.simulation_56.reports.simulation_report_generator import (
    SimulationReportGenerator,
)

logger = logging.getLogger(__name__)


class PipelineOrchestrator:

    def __init__(self):
        logger.info("Day 56 Full System Simulation Initialized")

    def extract_keywords(self, jd_text):
        return list(set(word.lower() for word in jd_text.split() if len(word) > 2))

    def process_candidate(self, candidate):

        profile = candidate.get("profile_type", "balanced")

        if profile == "strong_ats":
            final_score = 85

        elif profile == "strong_technical":
            final_score = 88

        elif profile == "strong_hr":
            final_score = 82

        elif profile == "high_risk":
            final_score = 55

        else:
            final_score = 75

        if final_score >= 75:
            decision = "Selected"

        elif final_score >= 60:
            decision = "Hold"

        else:
            decision = "Rejected"

        return {
            "candidate_id": candidate.get("candidate_id", str(uuid.uuid4())),
            "ats": final_score,
            "screening": final_score,
            "hr": final_score,
            "technical": final_score,
            "final_score": final_score,
            "decision": decision,
        }

    def run_pipeline(self, resume_path, jd_text, candidate_name="Simulation Candidate"):
        performance = PerformanceAnalyzer()
        performance.start()

        start_time = datetime.utcnow()

        result = {
            "candidate_id": str(uuid.uuid4()),
            "timestamp": start_time.isoformat(),
            "status": "Started",
        }

        try:

            # ==========================================
            # STEP 1 : PDF EXTRACTION DEBUG
            # ==========================================

            print("\n========== PDF DEBUG ==========")
            print("Resume Path:", resume_path)
            print("File Exists:", os.path.exists(resume_path))

            if os.path.exists(resume_path):
                print("File Size:", os.path.getsize(resume_path), "bytes")

            pdf_text = extract_text_from_pdf(resume_path)

            print("PDF Text Length:", len(pdf_text))
            print("PDF Preview:")
            print(pdf_text[:500])

            print("================================")

            # ==========================================
            # STEP 1B : RESUME PARSER
            # ==========================================

            if not pdf_text:

                raise Exception("Resume extraction failed")

            try:

                # New parser → accepts extracted text
                parsed_resume = parse_resume(pdf_text)

            except Exception:

                logger.warning("Resume parser fallback → using file path")

                # Old parser compatibility
                parsed_resume = parse_resume(resume_path)

            # Guarantee raw_text exists
            if isinstance(
                parsed_resume,
                dict,
            ):

                parsed_resume["raw_text"] = parsed_resume.get("raw_text") or pdf_text

            logger.info("========== PARSED RESUME ==========")

            logger.info(parsed_resume)

            print("\n========== PARSED RESUME ==========")

            print(parsed_resume)

            print("===================================")

            # ==========================================
            # STEP 2 : ATS
            # ==========================================

            jd_data = {
                "text": jd_text,
                "keywords": self.extract_keywords(jd_text),
            }

            features = extract_features(parsed_resume)

            logger.info("========== ATS FEATURES ==========")
            logger.info(features)
            logger.info("==================================")

            print("\n========== ATS FEATURES ==========")
            print(features)
            print("==================================")

            ats_result = calculate_score(parsed_resume, jd_data)

            print("\n========== ATS RESULT ==========")
            print(ats_result)
            print("================================")

            if isinstance(ats_result, dict):
                ats_score = ats_result.get("overall_score", 0)
            else:
                ats_score = ats_result
                ats_result = {"overall_score": ats_score}

            logger.info(f"ATS RESULT: {ats_result}")

            result["ats"] = ats_result

            # ==========================================
            # STEP 3 : ELIGIBILITY
            # ==========================================

            if ats_score < 60:

                logger.warning(f"Low ATS ({ats_score}) → Continuing for simulation")

                result["status"] = "ATS_LOW_CONTINUED"

            else:

                result["status"] = "ATS_PASSED"

            # ==========================================
            # STEP 4 : SCREENING
            # ==========================================

            screening_result = {"score": 78, "status": "Passed"}

            result["screening"] = screening_result

            # ==========================================
            # STEP 5 : HR INTERVIEW
            # ==========================================

            try:

                hr_engine = LegacyInterviewEngine()

                hr_output = hr_engine.run(
                    role="backend developer", experience="fresher"
                )

                hr_score = hr_output.get("average_score", 8) * 10

                hr_result = {
                    "overall_score": hr_score,
                    "decision": hr_output.get("decision", "HOLD"),
                }

            except Exception as e:

                logger.warning(f"HR Engine Failed: {e}")

                hr_result = {"overall_score": 80, "decision": "PASS"}

            result["hr"] = hr_result

            # ==========================================
            # STEP 6 : TECHNICAL
            # ==========================================

            tech_request = InterviewRequest(
                candidate_id=result["candidate_id"],
                candidate_name=candidate_name,
                resume_text=str(parsed_resume),
                answer="Python uses garbage collection.",
                coding_answer="""
def reverse_string(text):
    return text[::-1]
""",
                duration_seconds=120,
            )

            technical_response = run_interview(tech_request)

            technical_result = technical_response.get("report", {})

            logger.info(type(technical_result))
            logger.info(technical_result)

            result["technical"] = technical_result

            technical_score = technical_result.get("final_score", 80)

            # ==========================================
            # STEP 7 : MACHINE TEST
            # ==========================================

            try:

                machine_result = machine_test_pipeline(parsed_resume)

                if not isinstance(machine_result, dict):
                    machine_result = {"final_score": 85}

            except Exception as e:

                logger.warning(f"Machine Test Failed: {e}")

                machine_result = {"final_score": 85}

            result["machine_test"] = machine_result

            # ==========================================
            # STEP 8 : BEHAVIOR
            # ==========================================

            try:

                class BehaviorData:
                    eye_focus = 85
                    head_stability = 80
                    engagement = 88
                    distraction = 10

                behavior_result = behavioral_pipeline(BehaviorData())

                if not isinstance(behavior_result, dict):
                    behavior_result = {
                        "behavior_score": 84,
                        "risk": "Low",
                    }

            except Exception as e:

                logger.warning(f"Behavioral Engine Failed: {e}")

                behavior_result = {
                    "behavior_score": 84,
                    "risk": "Low",
                }

            result["behavior"] = behavior_result
            # ==========================================
            # STEP 9 : INTEGRITY
            # ==========================================

            try:

                class IntegrityData:
                    tab_switch = 0
                    copy_paste = 0
                    multiple_faces = False
                    window_blur = False
                    idle_time = 0
                    focus_loss = 0

                integrity_result = integrity_pipeline(IntegrityData())

                if not isinstance(integrity_result, dict):
                    integrity_result = {
                        "score": 88,
                        "risk": "Low",
                    }

            except Exception as e:

                logger.warning(f"Integrity Engine Failed: {e}")

                integrity_result = {
                    "score": 88,
                    "risk": "Low",
                }

            result["integrity"] = integrity_result

            # ==========================================
            # STEP 10 : UNIFIED SCORE
            # ==========================================

            try:

                unified_result = unified_pipeline(
                    candidate_id=result["candidate_id"],
                    ats=ats_score,
                    screening=screening_result["score"],
                    hr=hr_result["overall_score"],
                    tech=technical_score,
                    machine_test=machine_result("final_score"),
                    behavior=behavior_result("behavior_score"),
                    integrity=integrity_result("score"),
                    role="fresher",
                )

                if not isinstance(unified_result, dict):
                    unified_result = {"final_score": unified_result}

                final_score = unified_result.get(
                    "final_score",
                    0,
                )

            except Exception as e:

                logger.warning(f"Unified Pipeline Failed: {e}")

                final_score = round(
                    (
                        ats_score
                        + screening_result["score"]
                        + hr_result["overall_score"]
                        + technical_score
                        + machine_result.get("final_score", 85)
                    )
                    / 5,
                    2,
                )

                unified_result = {"final_score": final_score}

            result["unified_score"] = unified_result
            result["final_score"] = final_score

            # ==========================================
            # STEP 11 : DECISION
            # ==========================================

            if final_score >= 75:
                decision = "Selected"

            elif final_score >= 60:
                decision = "Hold"

            else:
                decision = "Rejected"

            result["decision"] = decision

            # ==========================================
            # STEP 12 : RECRUITER REPORT
            # ==========================================

            report_generator = ReportGenerator()

            result["recruiter_report"] = report_generator.generate(
                {
                    "candidate_id": result["candidate_id"],
                    "final_score": final_score,
                    "flags": [],
                }
            )

            # ==========================================
            # STEP 13 : CANDIDATE GENERATOR
            # ==========================================

            candidates = generate_candidates(50)

            result["candidate_generation"] = {"generated": len(candidates)}

            # ==========================================
            # STEP 14 : AI HUMAN COMPARISON
            # ==========================================

            comparison_result = AIHumanComparison.compare(
                [{"decision": "Selected"}], [{"decision": "Selected"}]
            )

            result["ai_human_comparison"] = comparison_result

            # ==========================================
            # STEP 15 : CONSISTENCY
            # ==========================================

            result["consistency"] = ConsistencyChecker.check(
                {
                    "ats": ats_score,
                    "technical": technical_score,
                    "hr": hr_result["overall_score"],
                    "behavior_risk": "Low",
                    "final_score": final_score,
                }
            )

            # ==========================================
            # STEP 16 : PERFORMANCE
            # ==========================================

            result["performance"] = performance.stop()

            # ==========================================
            # STEP 17 : DRIFT
            # ==========================================

            result["drift"] = DriftDetector.detect(
                [
                    ats_score,
                    screening_result["score"],
                    hr_result["overall_score"],
                    final_score,
                ]
            )

            # ==========================================
            # STEP 18 : PRODUCTION VALIDATION
            # ==========================================

            result["production_validation"] = ProductionValidator.validate()

            # ==========================================
            # STEP 19 : FUNNEL
            # ==========================================

            result["funnel"] = FunnelAnalyzer.generate(
                [
                    {
                        "ats": ats_score,
                        "screening": screening_result["score"],
                        "hr": hr_result["overall_score"],
                        "technical": technical_score,
                        "decision": decision,
                    }
                ]
            )

            # ==========================================
            # STEP 20 : RECOMMENDATIONS
            # ==========================================

            result["recommendations"] = RecommendationEngine.generate(comparison_result)

            # ==========================================
            # STEP 21 : DASHBOARD
            # ==========================================

            PerformanceDashboard.display(result)

            # ==========================================
            # STEP 22 : SIMULATION REPORT
            # ==========================================

            os.makedirs("reports", exist_ok=True)

            report_path = f"reports/simulation_" f"{result['candidate_id']}.json"

            SimulationReportGenerator.generate(
                result,
                report_path,
            )

            result["simulation_report"] = {"saved_to": report_path}

            result["processing_time_seconds"] = (
                datetime.utcnow() - start_time
            ).total_seconds()

            result["status"] = "Completed"

            # ==========================================
            # FINAL CLEAN RESPONSE
            # ==========================================

            final_output = {
                "candidate_id": result["candidate_id"],
                "scores": {
                    "ats": ats_score,
                    "screening": screening_result["score"],
                    "hr": hr_result["overall_score"],
                    "technical": technical_score,
                    "machine_test": machine_result.get(
                        "final_score",
                        82,
                    ),
                },
                "behavior": {
                    "risk_level": behavior_result.get(
                        "risk",
                        "Low Risk",
                    )
                },
                "integrity": {
                    "risk_level": integrity_result.get(
                        "risk",
                        "Moderate Risk",
                    )
                },
                "final_score": round(
                    final_score,
                    2,
                ),
                "decision": decision,
            }

            logger.info("FINAL OUTPUT")
            logger.info(final_output)

            print("\n========== FINAL OUTPUT ==========")
            print(final_output)
            print("==================================")

            return final_output

        except Exception as e:

            logger.exception(str(e))

            result["status"] = "Failed"
            result["error"] = str(e)

            return result
