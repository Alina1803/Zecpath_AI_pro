from fastapi import APIRouter

router = APIRouter(
    prefix="/screening",
    tags=["Screening AI"],
)


@router.post("/run")
async def run_screening():

    return {"status": "success"}
