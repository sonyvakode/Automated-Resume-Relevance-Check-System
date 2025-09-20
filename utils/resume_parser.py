import fitz  # PyMuPDF
import docx2txt

def extract_text(file):
    filename = file.name.lower()
    if filename.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    elif filename.endswith(".docx"):
        return docx2txt.process(file)
    else:
        return file.read().decode("utf-8")
