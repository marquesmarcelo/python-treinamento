import hashlib
import requests
import json
from typing import List
from domain.models.chat_message import ChatMessage
from application.interfaces.chat_model_interface import ChatModelInterface
from infrastructure.file_loader.pdf_loader_pypdf import PDFLoader
from application.interfaces.vector_store_interface import VectorStoreInterface
from domain.models.file_content import FileContent

class LlamaRestClient(ChatModelInterface):
    def __init__(self, api_url: str, vector_store: VectorStoreInterface):
        """
        Configura o cliente para a API REST do Llama.
        :param api_url: URL base da API REST.
        """
        self.api_url = api_url
        self.vector_store = vector_store

    def _calculate_pdf_hash(self, pdf_path: str) -> str:
        """
        Calcula a hash SHA-256 do PDF.
        :param pdf_path: Caminho do arquivo PDF.
        :return: Hash do conteúdo do PDF.
        """
        hasher = hashlib.sha256()
        with open(pdf_path, "rb") as pdf_file:
            hasher.update(pdf_file.read())
        return hasher.hexdigest()
    
    def add_pdf(self, pdf_path: str):
        """
        Adiciona texto de um PDF ao banco de vetores, se ainda não existir.
        :param pdf_path: Caminho do arquivo PDF.
        """
        try:
            # Calcula a hash do PDF
            pdf_hash = self._calculate_pdf_hash(pdf_path)

            # Verifica se o PDF já está no banco
            existing_hashes = self.vector_store.get_all_hashes()
            
            if pdf_hash in existing_hashes:
                print(f"O PDF '{pdf_path}' já foi processado. Ignorando...")
                return

            # Extrai texto do PDF e processa
            raw_text = PDFLoader.load_text_from_pdf(pdf_path)
            pdf_content = FileContent.from_raw_text(raw_text)

            # Cria metadados para cada segmento
            metadatas = [{"source": pdf_path, "segment_index": i, "hash": pdf_hash} for i in range(len(pdf_content.segments))]
            
            # Adiciona os segmentos e metadados ao banco de vetores
            self.vector_store.add_to_index(pdf_content.segments, metadatas)
            print(f"PDF '{pdf_path}' adicionado ao banco de vetores.")
        except Exception as e:
            raise RuntimeError(f"Erro ao processar o PDF '{pdf_path}': {e}")

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