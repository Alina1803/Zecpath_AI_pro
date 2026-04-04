import pdfplumber
from pdf2image import convert_from_path
import pytesseract
from docx import Document

def read_pdf(file_path):
    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    except:
        pass

    # If empty → use OCR
    if not text.strip():
        try:
            images = convert_from_path(file_path)
            for img in images:
                text += pytesseract.image_to_string(img)
        except Exception as e:
            print(f"OCR failed: {e}")

    return text

def read_docx(file_path):
    try:
        doc = Document(file_path)
        text = []

        for para in doc.paragraphs:
            if para.text.strip():
                text.append(para.text)

        return "\n".join(text)

    except Exception as e:
        print(f"DOCX read error: {e}")
        return ""