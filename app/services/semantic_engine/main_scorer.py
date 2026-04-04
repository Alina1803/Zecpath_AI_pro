import os
import json
from app.services.semantic_engine.section_matcher import match_skills, match_experience, match_projects
from app.services.semantic_engine.pdf_docx import read_pdf, read_docx
from app.services.semantic_engine.embedding_model import get_embedding
from sentence_transformers import SentenceTransformer

INPUT_FOLDER = "data/raw"
OUTPUT_FOLDER = "data/processed/output-12"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

model = SentenceTransformer("all-MiniLM-L6-v2")

def read_file(file_path):
    ext = file_path.lower().split('.')[-1]

    try:
        if ext == "pdf":
            return read_pdf(file_path)

        elif ext == "docx":
            return read_docx(file_path)

        elif ext == "txt":
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()

        else:
            print(f"Unsupported file: {file_path}")
            return ""

    except Exception as e:
        print(f"File read error: {e}")
        return ""

def process_file(file_path):
    ext = file_path.lower().split('.')[-1]

    if ext == "pdf":
        text = read_pdf(file_path)

    elif ext == "docx":
        text = read_docx(file_path)

    else:
        print(f"Unsupported file: {file_path}")
        return None

    embedding = get_embedding(text, model)

    return {
        "file": os.path.basename(file_path),
        "text": text[:1000],  # limit size
        "embedding": embedding
    }

def score_resume_to_jd(resume_json, jd_json):
    
    resume_skills = resume_json.get("skills", [])
    resume_exp = resume_json.get("experience_summary", "")
    resume_projects = resume_json.get("projects", [])

    jd_skills = jd_json.get("skills", [])
    jd_desc = jd_json.get("description", "")

    score_skills = match_skills(resume_skills, jd_skills)
    score_exp = match_experience(resume_exp, jd_desc)
    score_proj = match_projects(resume_projects, jd_desc)

    final_score = (
        0.4 * score_skills +
        0.3 * score_exp +
        0.3 * score_proj
    )

    return {
        "semantic_score": round(final_score, 3),
        "breakdown": {
            "skills": score_skills,
            "experience": score_exp,
            "projects": score_proj
        }
    }

def main():
    for file in os.listdir(INPUT_FOLDER):
        file_path = os.path.join(INPUT_FOLDER, file)

        print(f"Processing: {file}")

        data = process_file(file_path)

        if data:
            output_file = os.path.join(
                OUTPUT_FOLDER,
                file.replace(".pdf", ".json").replace(".docx", ".json")
            )

            with open(output_file, "w") as f:
                json.dump(data, f, indent=4)

            print(f"Saved: {output_file}")


if __name__ == "__main__":
    main()