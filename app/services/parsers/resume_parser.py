import os
import re
import pdfplumber
import pytesseract

from pdf2image import convert_from_path

# =====================================================
# CONFIG
# =====================================================

POPPLER_PATH = r"D:\Poppler-25.12.0\poppler-25.12.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract\tesseract.exe"

# =====================================================
# TEXT EXTRACTION
# =====================================================


def extract_text_from_file(input_data):
    try:
        if input_data is None:
            return ""

        value = str(input_data)

        # RAW TEXT MODE
        if not os.path.exists(value):
            return value

        extension = os.path.splitext(value)[1].lower()

        # NORMAL FILE
        if extension != ".pdf":
            with open(
                value,
                "r",
                encoding="utf-8",
                errors="ignore",
            ) as f:
                return f.read()

        # PDF MODE
        print("\n==================================================")
        print("PDF FILE:", value)

        text = ""

        with pdfplumber.open(value) as pdf:
            print("TOTAL PAGES:", len(pdf.pages))

            for i, page in enumerate(pdf.pages):
                try:
                    page_text = page.extract_text()

                    size = len(page_text) if page_text else 0

                    print(f"PAGE {i + 1} LENGTH:", size)

                    if page_text:
                        text += page_text + "\n"

                except Exception as e:
                    print(f"PAGE {i + 1} ERROR:", e)

        # OCR FALLBACK
        if not text.strip():

            print("No embedded text → Using OCR")

            images = convert_from_path(
                value,
                poppler_path=POPPLER_PATH,
            )

            for i, image in enumerate(images):
                try:
                    page_text = pytesseract.image_to_string(image)

                    print(
                        f"OCR PAGE {i + 1}:",
                        len(page_text),
                    )

                    text += page_text + "\n"

                except Exception as e:
                    print(
                        f"OCR PAGE {i + 1} ERROR:",
                        e,
                    )

        return text.strip()

    except Exception as e:
        print("\nPDF Read Error:", e)
        return ""


# =====================================================
# CLEAN
# =====================================================


def clean_text(text):
    if not text:
        return ""

    text = text.replace("\r", "\n")

    text = re.sub(
        r"\n+",
        "\n",
        text,
    )

    text = re.sub(
        r"[ \t]+",
        " ",
        text,
    )

    return text.strip()


# =====================================================
# NAME FILTER
# =====================================================

INVALID_NAME_WORDS = {
    "resume",
    "developer",
    "engineer",
    "skills",
    "education",
    "experience",
    "python",
    "java",
}


# =====================================================
# NAME
# =====================================================


def extract_name(text):
    if not text:
        return "Unknown"

    lines = [x.strip() for x in text.split("\n") if x.strip()]

    for line in lines[:15]:

        candidate = re.sub(
            r"[^A-Za-z\s]",
            "",
            line,
        )

        candidate = re.sub(
            r"\s+",
            " ",
            candidate,
        ).strip()

        words = candidate.split()

        if 2 <= len(words) <= 4 and len(candidate) < 40:

            if not any(w.lower() in INVALID_NAME_WORDS for w in words):
                return candidate

    return "Unknown"


# =====================================================
# EMAIL
# =====================================================


def extract_email(text):
    match = re.search(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        text,
    )

    return match.group() if match else "Not Found"


# =====================================================
# PHONE
# =====================================================


def extract_phone(text):
    match = re.search(
        r"(?:\+91[\-\s]?)?(?:91)?[6789]\d{9}",
        text,
    )

    return match.group() if match else "Not Found"


# =====================================================
# SKILLS
# =====================================================


def extract_skills(text):

    skills = [
        "python",
        "java",
        "react",
        "mysql",
        "gst",
        "audit",
        "taxation",
        "finance",
        "excel",
        "aws",
        "docker",
        "sap",
        "accounting",
        "reporting",
    ]

    lower = text.lower()

    return sorted([x for x in skills if x in lower])


# =====================================================
# EXPERIENCE
# =====================================================


def extract_experience(text):
    matches = re.findall(
        r"(\d+)\+?\s*(years?|yrs?)",
        text.lower(),
    )

    if matches:
        return max(int(x[0]) for x in matches)

    return 0


# =====================================================
# CERTIFICATIONS
# =====================================================


def extract_certifications(text):

    certs = [
        "ca",
        "icai",
        "cpa",
        "mba",
        "aws certified",
    ]

    lower = text.lower()

    return [x for x in certs if x in lower]


# =====================================================
# MAIN PARSER
# =====================================================


def parse_resume(input_data):
    try:

        raw = extract_text_from_file(input_data)

        cleaned = clean_text(raw)

        result = {
            "name": extract_name(cleaned),
            "email": extract_email(cleaned),
            "phone": extract_phone(cleaned),
            "skills": extract_skills(cleaned),
            "experience_years": extract_experience(cleaned),
            "certifications": extract_certifications(cleaned),
            "raw_text": cleaned,
        }

        print("\n========== PARSED RESUME ==========")
        print(result)
        print("===================================")

        return result

    except Exception as e:

        print("Resume Parser Error:", e)

        return {
            "name": "Unknown",
            "email": "Not Found",
            "phone": "Not Found",
            "skills": [],
            "experience_years": 0,
            "certifications": [],
            "raw_text": "",
            "error": str(e),
        }
