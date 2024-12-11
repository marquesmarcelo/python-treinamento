from typing import List
from domain.models.chat_message import ChatMessage
from application.interfaces.chat_model_interface import ChatModelInterface

class ChatInteraction:
    def __init__(self, chat_model: ChatModelInterface):
        self.chat_model = chat_model
        self.vector_store = chat_model.vector_store

    def send_message(self, messages):
        """
        Envia uma mensagem ao modelo, utilizando o banco de vetores para enriquecer o contexto.
        :param messages: Lista de mensagens do usuário.
        :return: Resposta do modelo.
        """
        # Última mensagem do usuário
        user_message = messages[-1].content

        # Consulta ao banco de vetores
        context_segments, metadatas = self.vector_store.query(user_message, top_k=5)
        print("estou aqui", context_segments)
        # Combine o contexto do banco de vetores com a mensagem
        context = "\n".join(context_segments)
        enriched_message = f"Contexto relevante:\n{context}\n\nPergunta do usuário:\n{user_message}"

        # Substitua a última mensagem pelo texto enriquecido
        messages[-1].content = enriched_message

        # Enviar mensagem ao modelo
        return self.chat_model.chat(messages)
