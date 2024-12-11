from typing import List

class PDFContent:
    def __init__(self, segments: List[str]):
        """
        Representa o conteúdo do PDF como uma lista de segmentos.
        :param segments: Lista de segmentos de texto extraídos do PDF.
        """
        self.segments = segments

    @staticmethod
    def from_raw_text(raw_text: str) -> 'PDFContent':
        """
        Converte texto bruto em uma instância de PDFContent.
        :param raw_text: Texto bruto extraído do PDF.
        :return: Instância de PDFContent contendo os segmentos do texto.
        """
        # Divide o texto bruto em segmentos (exemplo: por linhas)
        segments = raw_text.split("\n")
        return PDFContent(segments)

