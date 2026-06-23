import pdfplumber
import pytesseract
from pdf2image import convert_from_path

# Windows only (optional)
pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract\tesseract.exe"


def extract_text_from_pdf(file_path):

    text = ""

    try:

        print("\n========== PDF DEBUG ==========")

        print("Resume Path:", file_path)

        print("==================================================")

        # ====================================
        # TRY EMBEDDED TEXT
        # ====================================

        with pdfplumber.open(file_path) as pdf:

            print("PDF FILE:", file_path)

            print("TOTAL PAGES:", len(pdf.pages))

            for i, page in enumerate(pdf.pages):

                try:

                    page_text = page.extract_text()

                    page_len = len(page_text) if page_text else 0

                    print(
                        f"PAGE {i+1} LENGTH:",
                        page_len,
                    )

                    if page_text:

                        text += page_text + "\n"

                except Exception as e:

                    print(
                        f"PAGE {i+1} ERROR:",
                        e,
                    )

        # ====================================
        # RETURN IF TEXT FOUND
        # ====================================

        if text.strip():

            print(f"PDF Text Length: {len(text)}")

            print(
                "PDF Preview:\n",
                text[:500],
            )

            return text.strip()

        # ====================================
        # OCR FALLBACK
        # ====================================

        print("No embedded text → Using OCR")

        images = convert_from_path(
            file_path,
            dpi=300,
        )

        ocr_output = ""

        for i, img in enumerate(images):

            try:

                ocr_text = pytesseract.image_to_string(
                    img,
                    lang="eng",
                )

                print(
                    f"OCR PAGE {i+1}:",
                    len(ocr_text),
                )

                ocr_output += ocr_text + "\n"

            except Exception as e:

                print(
                    f"OCR PAGE {i+1} ERROR:",
                    e,
                )

        text = ocr_output

        print(f"PDF Text Length: {len(text)}")

        print(
            "PDF Preview:\n",
            text[:500],
        )

        return text.strip()

    except Exception as e:

        print(
            "\nPDF Read Error:",
            e,
        )

        return ""
