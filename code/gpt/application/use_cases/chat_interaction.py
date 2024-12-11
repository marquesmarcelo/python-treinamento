from typing import List
from domain.models.chat_message import ChatMessage
from application.interfaces.chat_model_interface import ChatModelInterface

class ChatInteraction:
    def __init__(self, chat_model: ChatModelInterface):
        self.chat_model = chat_model

    def send_message(self, messages: List[ChatMessage]) -> str:
        """
        Envia mensagens ao modelo e retorna a resposta.
        :param messages: Lista de mensagens (usuário e contexto).
        :return: Resposta do modelo.
        """
        return self.chat_model.chat(messages)
