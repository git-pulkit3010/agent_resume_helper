# resume_loader.py

import os
import pdfplumber
import docx


def extract_text_from_pdf(file_path):
    text = ''
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text.strip()

   
def extract_text_from_doc(file_path):
    # DOC is legacy; we use textract or unoconv
    try:
        text = textract.process(file_path)
        return text.decode('utf-8').strip()
    except Exception as e:
        raise RuntimeError(f"Error reading DOC file: {e}")

def load_resume(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("The resume file was not found.")

    ext = file_path.lower().split('.')[-1]
    if ext == 'pdf':
        return extract_text_from_pdf(file_path)
    elif ext == 'docx':
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX only.")

