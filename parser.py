import fitz  # PyMuPDF
import docx2txt

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file"""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(docx_path):
    """Extract text from a DOCX file"""
    return docx2txt.process(docx_path)

def parse_resume(file_path):
    """Detect file type and extract text"""
    if file_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")
