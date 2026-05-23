import pdfplumber
import re


def clean_page_text(text):

    # remove repeated spaces
    text = re.sub(r'[ \t]+', ' ', text)

    # remove excessive line breaks
    text = re.sub(r'\n+', '\n', text)

    return text.strip()


def extract_text(pdf_path):

    pages = []

    with pdfplumber.open(pdf_path) as pdf:

        for page_num, page in enumerate(pdf.pages):

            text = page.extract_text()

            if text:

                cleaned = clean_page_text(text)

                pages.append({
                    "page": page_num + 1,
                    "text": cleaned
                })

    return pages