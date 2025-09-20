import fitz  # PyMuPDF
import docx2txt
from io import BytesIO

def extract_text(file):
    """Extract text from PDF or DOCX file"""
    filename = file.name.lower()
    if filename.endswith(".pdf"):
        pdf_text = ""
        pdf_bytes = BytesIO(file.read())
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        for page in doc:
            pdf_text += page.get_text()
        return pdf_text
    elif filename.endswith(".docx"):
        docx_bytes = BytesIO(file.read())
        text = docx2txt.process(docx_bytes)
        return text
    else:
        return file.read().decode("utf-8", errors="ignore")
