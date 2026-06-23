from app.services.optimization_stability42.optimization_refinement_54.threshold_optimizer import (
    ThresholdOptimizer,
)

from app.services.optimization_stability42.optimization_refinement_54.consistency_engine import (
    ConsistencyEngine,
)

from app.services.optimization_stability42.optimization_refinement_54.intent_refiner import (
    IntentRefiner,
)

from app.services.optimization_stability42.optimization_refinement_54.false_positive_analyzer import (
    FalsePositiveAnalyzer,
)

from app.services.optimization_stability42.optimization_refinement_54.refinement_report_generator import (
    RefinementReportGenerator,
)

# ==========================================
# FASTAPI APP
# ==========================================
from fastapi import FastAPI

app = FastAPI(title="Zecpath Optimization & Refinement Engine", version="54.0")


# ==========================================
# OPTIMIZATION PIPELINE
# ==========================================


class OptimizationPipeline:

    def run(self, candidate):

        threshold = ThresholdOptimizer().optimize(
            candidate.get("score", 0), candidate.get("integrity_risk", "Low Risk")
        )

        consistency = ConsistencyEngine().evaluate(
            candidate.get("ats", 0),
            candidate.get("technical", 0),
            candidate.get("hr", 0),
        )

        intent = IntentRefiner().detect(candidate.get("answer", ""))

        false_positive = FalsePositiveAnalyzer().analyze(
            candidate.get("score", 0),
            candidate.get("communication", 0),
            candidate.get("integrity_risk", "Low Risk"),
        )

        final = {
            "threshold_result": threshold,
            "consistency": consistency,
            "intent": intent,
            "false_positive": false_positive,
        }

        return RefinementReportGenerator().generate(final)


# ==========================================
# PIPELINE INSTANCE
# ==========================================

pipeline = OptimizationPipeline()


# ==========================================
# HEALTH CHECK
# ==========================================


@app.get("/")
def home():

    return {"message": "Day 54 Optimization Engine Running"}


# ==========================================
# OPTIMIZATION API
# ==========================================


@app.post("/optimize")
def optimize(candidate: dict):

    return pipeline.run(candidate)
