import pdfplumber
import pytesseract
import docx

from pdf2image import convert_from_path

POPPLER_PATH = r"D:\Poppler-25.12.0\poppler-25.12.0\Library\bin"

TESSERACT_PATH = r"D:\tesseract\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = (
    TESSERACT_PATH
)

# ==========================================
# TXT LOADER
# ==========================================
def load_txt(file_path):

    with open(

        file_path,
        "r",
        encoding="utf-8"

    ) as f:

        return f.read()


# ==========================================
# DOCX LOADER
# ==========================================
def load_docx(file_path):

    try:

        doc = docx.Document(file_path)

        return "\n".join(

            paragraph.text

            for paragraph in doc.paragraphs
        )

    except Exception as e:

        print(
            f"⚠️ DOCX read failed: {e}"
        )

        return ""


# ==========================================
# PDF TEXT EXTRACTION
# ==========================================
def load_pdf_text(file_path):

    text = ""

    try:

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                extracted = (
                    page.extract_text()
                    or ""
                )

                text += extracted + "\n"

    except Exception as e:

        print(
            f"⚠️ PDF extraction failed: {e}"
        )

    return text


# ==========================================
# OCR EXTRACTION
# ==========================================
def load_pdf_ocr(file_path):

    text = ""

    try:

        images = convert_from_path(

            file_path,

            poppler_path=POPPLER_PATH
        )

        for img in images:

            extracted = pytesseract.image_to_string(
                img
            )

            text += extracted + "\n"

    except Exception as e:

        print(
            f"⚠️ OCR error: {e}"
        )

    return text


# ==========================================
# SMART FILE LOADER
# ==========================================
def load_file(file_path):

    # --------------------------------------
    # TXT
    # --------------------------------------
    if file_path.endswith(".txt"):

        return load_txt(file_path)

    # --------------------------------------
    # DOCX
    # --------------------------------------
    elif file_path.endswith(".docx"):

        return load_docx(file_path)

    # --------------------------------------
    # PDF
    # --------------------------------------
    elif file_path.endswith(".pdf"):

        # ----------------------------------
        # NORMAL EXTRACTION
        # ----------------------------------
        text = load_pdf_text(file_path)

        # ----------------------------------
        # OCR FALLBACK
        # ----------------------------------
        if len(text.strip()) < 100:

            print(
                f"🔍 Using OCR for: {file_path}"
            )

            text = load_pdf_ocr(file_path)

        return text

    
    raise ValueError(

        f"Unsupported format: {file_path}"
    )