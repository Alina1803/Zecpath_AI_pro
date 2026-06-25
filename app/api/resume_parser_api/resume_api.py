from fastapi import (
    APIRouter,
    UploadFile,
    File,
)

import tempfile
import os

from app.services.parsers.resume_parser import (
    parse_resume,
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume Parser"],
)


@router.post("/parse")
async def parse_resume_api(file: UploadFile = File(...)):

    temp_path = None

    try:

        ext = os.path.splitext(file.filename)[1]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=ext,
        ) as temp:

            temp.write(await file.read())

            temp_path = temp.name

        result = parse_resume(temp_path)

        return {
            "status": "success",
            "data": result,
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e),
        }

    finally:

        if temp_path and os.path.exists(temp_path):

            os.remove(temp_path)
