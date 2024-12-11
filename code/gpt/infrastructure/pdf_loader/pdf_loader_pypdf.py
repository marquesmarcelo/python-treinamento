from PyPDF2 import PdfReader

class PDFLoader:
    @staticmethod
    def load_pdf(file_path: str) -> str:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
