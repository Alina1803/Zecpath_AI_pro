from fastapi import FastAPI
from app.services.drive_service import download_file_from_drive
from app.utils.fake_data_generator import generate_resume, save_sample_data

app = FastAPI(title="Zecpath AI Resume System")

file_id = "https://drive.google.com/drive/folders/10S7B4NN0sYGeK-pXaqVfkCOr7OXoen4Z?usp=sharing"

# ✅ 1. Generate fake resume (single)
@app.get("/generate-fake-resume/")
def get_fake_resume():
    return generate_resume()


# ✅ 2. Generate multiple fake resumes and save to file
@app.get("/generate-fake-dataset/")
def create_fake_dataset():
    save_sample_data(5)
    return {"message": "Fake dataset generated and saved in data/sample_resumes.json"}


# ✅ 3. Download resume from Google Drive
@app.get("/download-from-drive/")
def download_resume(file_id: str):
    file_path = f"data/raw/{file_id}.pdf"
    
    download_file_from_drive(file_id, file_path)
    
    return {
        "message": "File downloaded successfully",
        "file_path": file_path
    }