import io
import os
import shutil

import streamlit as st
from pypdf import PdfReader
import fitz
from PIL import Image
import pytesseract


# ---------------------------------
# Tesseract Configuration
# ---------------------------------

tesseract_path = shutil.which("tesseract")

if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

elif os.path.exists(r"C:\Program Files\Tesseract-OCR\tesseract.exe"):
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )


def load_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF.

    Uses normal PDF text extraction first.
    If the PDF has little or no extractable text,
    falls back to OCR for scanned/image-based PDFs.
    """

    reader = PdfReader(pdf_path)

    text_parts = []

    # ---------------------------------
    # Step 1: Normal text extraction
    # ---------------------------------

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text_parts.append(page_text)

    extracted_text = "\n".join(text_parts).strip()

    # ---------------------------------
    # Step 2: Check if OCR is needed
    # ---------------------------------

    if len(extracted_text) >= 100:
        return extracted_text

    # ---------------------------------
    # Step 3: OCR fallback
    # ---------------------------------

    document = fitz.open(pdf_path)

    ocr_parts = []

    total_pages = len(document)

    progress_text = st.empty()
    progress_bar = st.progress(0)

    for page_number, page in enumerate(document, start=1):

        progress_text.write(
            "OCR processing: " + str(page_number) + " / " + str(total_pages) + " pages"
        )

        pix = page.get_pixmap(
            matrix=fitz.Matrix(1.5, 1.5)
        )

        image = Image.open(
            io.BytesIO(pix.tobytes("png"))
        )

        page_text = pytesseract.image_to_string(image)

        if page_text:
            ocr_parts.append(page_text)

        progress_bar.progress(
            page_number / total_pages
        )

    document.close()

    progress_text.empty()
    progress_bar.empty()

    return "\n".join(ocr_parts).strip()