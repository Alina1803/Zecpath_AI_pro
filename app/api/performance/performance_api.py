from fastapi import APIRouter

from app.services.performance.performance_optimized import (
    fast_decision,
)

from app.services.performance.memory_optimization import (
    memory_efficient_processing,
)

from app.services.performance.optimized_api import (
    optimized_response,
)

router = APIRouter(
    prefix="/performance",
    tags=["Performance"],
)


@router.post("/run")
async def run_pipeline(score: float):

    # Decision
    decision = fast_decision(score)

    # Memory optimization
    processed = list(memory_efficient_processing([1, 2, 3]))

    # Final optimized response
    return optimized_response(
        {
            "decision": decision,
            "memory": processed,
        }
    )
