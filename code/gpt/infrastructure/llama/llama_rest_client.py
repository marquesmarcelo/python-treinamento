import requests
import json
from typing import List
from domain.models.chat_message import ChatMessage
from application.interfaces.chat_model_interface import ChatModelInterface
from infrastructure.pdf_loader.pdf_loader_pypdf import PDFLoader
from application.interfaces.vector_store_interface import VectorStoreInterface
from domain.models.pdf_content import PDFContent

class LlamaRestClient(ChatModelInterface):
    def __init__(self, api_url: str, vector_store: VectorStoreInterface):
        """
        Configura o cliente para a API REST do Llama.
        :param api_url: URL base da API REST.
        """
        self.api_url = api_url

    def add_pdf(self, pdf_path: str):
        """Carrega texto de um PDF e o adiciona ao banco de vetores."""
        raw_text = PDFLoader.load_text_from_pdf(pdf_path)
        pdf_content = PDFContent.from_raw_text(raw_text)
        self.vector_store.add_to_index(pdf_content.segments)
        self.vector_store.save_index()

    def query_pdf(self, query_text: str, top_k: int = 5):
        """Consulta o banco de vetores com um texto e retorna os resultados."""
        indices, distances = self.vector_store.query(query_text, top_k)
        return indices, distances

    def chat(self, messages: List[ChatMessage]) -> str:
        """
        Envia mensagens ao modelo Llama via API REST e retorna a resposta completa unificada.
        :param messages: Lista de mensagens do usuário e contexto.
        :return: Resposta completa do modelo como uma string.
        """
        try:
            # Formatar mensagens para o formato esperado pela API
            formatted_messages = [{"role": msg.role, "content": msg.content} for msg in messages]            
            
            # Criar a requisição para inspecionar
            request = requests.Request(
                method="POST",
                url=f"{self.api_url}/api/chat",
                json={"model": "llama3.2", "messages": formatted_messages},
                headers={"Content-Type": "application/json"},
            )
            
            # Preparar a requisição (montar os detalhes HTTP)
            prepared_request = request.prepare()
            
            # Exibir a requisição montada
            print("----- Requisição Montada -----")
            print(f"URL: {prepared_request.url}")
            print(f"Method: {prepared_request.method}")
            print(f"Headers: {prepared_request.headers}")
            print(f"Body: {prepared_request.body}")
            print("-----------------------------")
            
            # Enviar a requisição
            with requests.Session() as session:
                response = session.send(prepared_request)
            
            # Exibir a resposta
            print("----- Resposta -----")
            print(f"Status Code: {response.status_code}")
            print("Headers da resposta:", response.headers)
            
            # Verificar o tipo de conteúdo da resposta
            content_type = response.headers.get("Content-Type", "")
            if "application/x-ndjson" in content_type:
                # Processar NDJSON para juntar todos os pedaços de conteúdo
                print("Resposta em formato NDJSON detectada.")
                complete_message = ""
                for line in response.text.splitlines():
                    try:
                        json_line = json.loads(line)  # Analisar cada linha como JSON
                        # Concatenar o conteúdo da mensagem
                        complete_message += json_line.get("message", {}).get("content", "")
                    except json.JSONDecodeError as e:
                        raise RuntimeError(f"Erro ao analisar NDJSON: {e}")
                
                return complete_message.strip()  # Remover espaços desnecessários
            else:
                # Processar JSON normal
                try:
                    data = response.json()
                    return data.get("message", {}).get("content", "Erro: Resposta não encontrada na API.")
                except json.JSONDecodeError as e:
                    raise RuntimeError(f"Erro ao analisar JSON: {e}")
            
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Erro ao se comunicar com a API REST do Llama: {e}")
