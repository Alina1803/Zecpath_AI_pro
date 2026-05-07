from fastapi import APIRouter
from app.models.schemas45 import ReportResponse

# Create router
router = APIRouter()


@router.get(
    "/report/{candidate_id}",
    response_model=ReportResponse
)
def get_report(candidate_id: str):
    """
    Generate final HR interview report

    Path Parameter:
    - candidate_id

    Returns:
    - report generation status
    """

    return {
        "candidate_id": candidate_id,
        "status": "Completed",
        "message": "Final HR interview report generated successfully"
    }