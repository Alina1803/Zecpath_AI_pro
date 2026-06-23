import os
import pdfplumber


def extract_text_from_file(file_path: str) -> str:
    """
    Backward compatible:
    - TXT → old behavior
    - PDF → pdfplumber first
    - If PDF has no text → OCR fallback via file_loader
    """

    extension = os.path.splitext(file_path)[1].lower()

    try:

        # =====================================
        # PDF
        # =====================================
        if extension == ".pdf":

            text = ""

            try:
                with pdfplumber.open(file_path) as pdf:

                    print("=" * 50)
                    print("PDF FILE:", file_path)
                    print("TOTAL PAGES:", len(pdf.pages))
                    print("=" * 50)

                    for i, page in enumerate(pdf.pages):

                        page_text = page.extract_text()

                        print(
                            f"PAGE {i+1} LENGTH:",
                            len(page_text) if page_text else 0,
                        )

                        if page_text:
                            text += page_text + "\n"

            except Exception as e:
                print("pdfplumber error:", e)

            # ---------------------------------
            # OCR FALLBACK ONLY IF EMPTY
            # ---------------------------------
            if len(text.strip()) < 50:

                print("Using OCR fallback...")

                try:
                    from app.utils.file_loader import load_pdf_ocr

                    text = load_pdf_ocr(file_path)

                except Exception as e:
                    print("OCR failed:", e)

            return text

        # =====================================
        # TXT / OTHER
        # =====================================
        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore",
        ) as file:

            return file.read()

    except Exception as e:

        print("File Loader Error:", e)

        return ""
