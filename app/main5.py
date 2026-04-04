import os

from app.readers.pdf_reader import extract_text_from_pdf
from app.readers.docx_reader import extract_text_from_docx
from app.processors.text_cleaner import clean_text
from app.processors.normalizer import normalize_text
from app.utils.file_handler import save_output

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed/output_5"

def process_file(file_path):
    file_name = os.path.basename(file_path)

    print(f"Processing: {file_name}")

    if file_name.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)

    elif file_name.endswith(".docx"):
        text = extract_text_from_docx(file_path)

    else:
        print("Unsupported file format")
        return

    if not text:
        print(f"Skipping empty file: {file_name}")
        return

    # Cleaning
    cleaned = clean_text(text)

    # Normalization
    normalized = normalize_text(cleaned)

    # Save output
    save_output(file_name, normalized)


def run_pipeline():
    for file in os.listdir(RAW_FOLDER):
        file_path = os.path.join(RAW_FOLDER, file)
        process_file(file_path)


if __name__ == "__main__":
    run_pipeline()