from application.interfaces.vector_store_interface import VectorStoreInterface
from infrastructure.pdf_loader.pdf_loader_pypdf import PDFLoader
from domain.services.text_splitter import TextSplitter

class FileInteraction:
    def __init__(self, vector_store: VectorStoreInterface):
        self.vector_store = vector_store

    def process_pdf(self, file_path: str) -> None:
        # Carregar o texto do PDF
        pdf_text = PDFLoader.load_pdf(file_path)

        # Dividir o texto em partes
        splitter = TextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = splitter.split_text(pdf_text)

        # Adicionar ao banco de vetores
        self.vector_store.add_texts(chunks)
