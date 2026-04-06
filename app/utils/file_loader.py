import pdfplumber
import docx
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

# 🔥 Set path (IMPORTANT for Windows)

POPPLER_PATH = r"D:\Poppler-25.12.0\Library\bin"
TESSERACT_PATH = r"D:\tesseract\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_docx(path):
    try:
        import docx
        doc = docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        print(f"⚠️ DOCX read failed: {path} → {e}")
        return ""

# 🔥 NORMAL PDF EXTRACTION
def load_pdf_text(file_path):
    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except:
        pass

    return text


# 🔥 OCR FALLBACK (VERY POWERFUL)
def load_pdf_ocr(file_path):
    text = ""

    try:
        images = convert_from_path(file_path)

        for img in images:
            text += pytesseract.image_to_string(img)

    except Exception as e:
        print(f"OCR error: {e}")

    return text


# 🔥 SMART LOADER
def load_file(file_path):
    if file_path.endswith(".txt"):
        return load_txt(file_path)

    elif file_path.endswith(".docx"):
        return load_docx(file_path)

    elif file_path.endswith(".pdf"):
        text = load_pdf_text(file_path)

        # 🔥 If text is too small → use OCR
        if len(text.strip()) < 100:
            print("🔍 Using OCR for:", file_path)
            text = load_pdf_ocr(file_path)

        return text

    else:
        raise ValueError(f"Unsupported file format: {file_path}")