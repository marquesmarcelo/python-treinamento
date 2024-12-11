import chromadb
from chromadb.utils import embedding_functions
from typing import List, Tuple
from application.interfaces.vector_store_interface import VectorStoreInterface

class ChromaVectorStore(VectorStoreInterface):
    def __init__(self, persist_directory: str = "chroma_db"):
        # Configuração do ChromaDB com persistência
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection_name = "pdf_segments"
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        self.collection = self._get_or_create_collection()

    def _get_or_create_collection(self):
        """Cria ou recupera a coleção do banco."""
        existing_collections = [col["name"] for col in self.client.list_collections()]
        if self.collection_name not in existing_collections:
            return self.client.create_collection(
                name=self.collection_name, embedding_function=self.embedding_fn
            )
        return self.client.get_collection(name=self.collection_name)

    def add_to_index(self, segments: List[str], metadatas: List[dict]) -> None:
        """Adiciona segmentos de texto ao banco de vetores com metadados."""
        self.collection.add(
            documents=segments,
            metadatas=metadatas,
            ids=[f"segment_{i}" for i in range(len(segments))],
        )
        print(f"{len(segments)} segmentos adicionados ao banco de vetores.")

    def get_all_hashes(self) -> List[str]:
        """Retorna todas as hashes dos PDFs armazenados no banco."""
        metadatas = self.collection.get()["metadatas"]
        return [metadata["hash"] for metadata in metadatas if "hash" in metadata]

    def query(self, query_text: str, top_k: int) -> Tuple[List[str], List[dict]]:
        """Consulta o banco de vetores e retorna os segmentos mais similares com metadados."""
        results = self.collection.query(
            query_texts=[query_text], n_results=top_k
        )
        return results["documents"], results["metadatas"]
