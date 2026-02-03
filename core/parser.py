import pdfplumber
from docx import Document

def parse_file(file, file_type):
    if file_type == "pdf":
        with pdfplumber.open(file) as pdf:
            return "\n".join(p.extract_text() or "" for p in pdf.pages)
    elif file_type == "docx":
        doc = Document(file)
        return "\n".join(p.text for p in doc.paragraphs)
    else:
        return file.read().decode("utf-8")
