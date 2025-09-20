import fitz  # PyMuPDF
from docx import Document
import io

def extract_text(file):
    filename = file.name.lower()
    if filename.endswith(".pdf"):
        return extract_pdf_text(file)
    elif filename.endswith(".docx"):
        return extract_docx_text(file)
    else:
        return ""

def extract_pdf_text(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_docx_text(file):
    doc = Document(io.BytesIO(file.read()))
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text
