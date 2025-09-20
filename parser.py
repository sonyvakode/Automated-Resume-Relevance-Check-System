import fitz  # PyMuPDF for PDF parsing
import docx2txt

def extract_text(file):
    """Extract text from PDF or DOCX"""
    name = file.name.lower()
    if name.endswith(".pdf"):
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in pdf:
            text += page.get_text()
        return text
    elif name.endswith(".docx"):
        return docx2txt.process(file)
    else:
        return file.getvalue().decode("utf-8")
