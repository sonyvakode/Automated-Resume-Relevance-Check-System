import io, pdfplumber

def extract_text_from_file(uploaded_file):
    name = getattr(uploaded_file, "name", "uploaded_file")
    lower = name.lower()
    try:
        if lower.endswith(".pdf"):
            return extract_text_pdf(uploaded_file)
        elif lower.endswith(".docx"):
            return extract_text_docx(uploaded_file)
        else:
            # assume txt or others
            content = uploaded_file.read()
            if isinstance(content, bytes):
                try:
                    return content.decode("utf-8", errors="ignore")
                except:
                    return str(content)
            return str(content)
    finally:
        try:
            uploaded_file.seek(0)
        except:
            pass

def extract_text_pdf(file_obj):
    text = []
    with pdfplumber.open(file_obj) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

def extract_text_docx(file_obj):
    try:
        from docx import Document
        content = file_obj.read()
        import io
        f = io.BytesIO(content)
        doc = Document(f)
        parts = []
        for p in doc.paragraphs:
            parts.append(p.text)
        return "\n".join(parts)
    except Exception:
        return ""
