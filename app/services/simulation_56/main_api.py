from fastapi import FastAPI, UploadFile, File, Form, HTTPException

from tempfile import NamedTemporaryFile
import shutil

from app.services.simulation_56.pipeline_orchestrator import PipelineOrchestrator

app = FastAPI(title="Zecpath AI", version="56.0")

orchestrator = PipelineOrchestrator()


@app.get("/")
def root():
    return {"message": "Zecpath AI Running"}


@app.post("/run-pipeline")
async def run_pipeline(
    resume: UploadFile = File(...),
    jd_text: str = Form(...),
    candidate_name: str = Form("Simulation Candidate"),
):
    try:

        with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:

            shutil.copyfileobj(resume.file, temp_file)

            resume_path = temp_file.name

        result = orchestrator.run_pipeline(
            resume_path=resume_path, jd_text=jd_text, candidate_name=candidate_name
        )

        return result

    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health():
    return {"status": "healthy"}
