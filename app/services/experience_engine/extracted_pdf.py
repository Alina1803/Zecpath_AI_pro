import os
import pdfplumber


def extract_text_from_pdf(pdf_path, save_txt=False):
    """
    Extract text from PDF using pdfplumber
    """

    extracted_text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:
                text = page.extract_text()

                if text:
                    extracted_text += text + "\n"

    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""

    # Optional: Save extracted text
    if save_txt:

        os.makedirs("data/processed", exist_ok=True)

        file_name = os.path.basename(pdf_path).replace(".pdf", ".txt")

        output_path = os.path.join("data/processed", file_name)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(extracted_text)

    return extracted_text