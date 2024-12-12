from domain.models.chat_message import ChatMessage
from application.use_cases.chat_interaction import ChatInteraction
from infrastructure.llama.llama_rest_client import LlamaRestClient
from infrastructure.openai.openai_client import OpenAIClient
from infrastructure.vector_store.chroma_vector_store import ChromaVectorStore
from infrastructure.file_loader.file_loader import FileLoader
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

openai_api_key = os.environ.get("OPENAI_API_KEY")
llama_api_url = "http://localhost:11434"  # Substitua pelo URL real da API REST
vector_store = ChromaVectorStore(persist_directory="chroma_db")

def main():
    # Configurar qual modelo usar: "openai", "llama" ou "llama-pdf"
    modelo_escolhido = "llama-pdf"  # Altere para o modelo desejado

    if modelo_escolhido == "openai":
        # Configurar o cliente OpenAI
        chat_model = OpenAIClient(api_key=openai_api_key)
    elif modelo_escolhido in ["llama", "llama-pdf"]:
        # Configurar o cliente Llama com ou sem vetores
        chat_model = LlamaRestClient(api_url=llama_api_url, vector_store=vector_store)
    else:
        raise ValueError(f"Modelo '{modelo_escolhido}' não é suportado.")

    # Criar caso de uso de interação
    chat_interaction = ChatInteraction(chat_model)

    # Modo "llama-pdf": adicionar PDFs ao banco de vetores antes da consulta
    if modelo_escolhido == "llama-pdf":
        # Diretório do script
        diretorio_script = os.path.dirname(os.path.abspath(__file__))

        # Caminho relativo (dois níveis acima)        
        pdf_path = os.path.join(diretorio_script, r"../../assets/base_treinamento.pdf")  # Substitua pelo caminho real do PDF
        print(f"Adicionando arquivo '{pdf_path}' ao banco de vetores...")
        file_loader = FileLoader(pdf_path, vector_store=vector_store)
        
        file_loader.add_file()
        print("Arquivo adicionado com sucesso!")

    # Mensagens de exemplo
    messages = [
        ChatMessage(role="user", content="Porque o céu é azul?")
    ]

    # Enviar mensagem e obter resposta
    resposta = chat_interaction.send_message(messages)
    print(f"Resposta do modelo ({modelo_escolhido}): {resposta}")

if __name__ == "__main__":
    main()