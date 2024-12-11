from typing import List  # Import necessário para o tipo List
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from application.interfaces.vector_store_interface import VectorStoreInterface

class LangChainVectorStore(VectorStoreInterface):
    def __init__(self, openai_api_key: str):
        """
        Configura o banco de vetores com embeddings da OpenAI.
        :param openai_api_key: Chave de API da OpenAI.
        """
        self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        self.vector_store = None

    def add_texts(self, texts: List[str]) -> None:
        """
        Adiciona textos ao banco de vetores.
        :param texts: Lista de textos a serem armazenados.
        """
        self.vector_store = FAISS.from_texts(texts, self.embeddings)

    def query(self, query: str) -> List[str]:
        """
        Busca no banco de vetores com base na consulta.
        :param query: Consulta a ser realizada.
        :return: Lista de trechos relevantes.
        """
        if not self.vector_store:
            raise ValueError("O banco de vetores está vazio.")
        results = self.vector_store.similarity_search(query, k=1)
        return [result.page_content for result in results]
