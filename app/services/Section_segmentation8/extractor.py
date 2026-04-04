from pdfminer.high_level import extract_text as pdf_extract
from docx import Document

path = r"E:\Zecpath_AI_pro\data\raw"

def extract_text_from_pdf(path):
    return pdf_extract(path)

def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_text(path):   # ✅ correct
    if path.endswith(".pdf"):
        return extract_text_from_pdf(path)
    elif path.endswith(".docx"):
        return extract_text_from_docx(path)
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()