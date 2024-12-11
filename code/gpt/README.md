# Configurações Iniciais

## Instalação do servidor REST do Ollama localmente usando docker e WSL

Abrir o WSL (usei o Ubuntu)

Configurar o repositório

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
    | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
    | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
    | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update
```

Instalar o NVIDIA Container Toolkit packages (você precisa ter uma placa de vídeo da NVIDIA)

```bash
sudo apt-get install -y nvidia-container-toolkit
```
```bash
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Executar um modelo localmente. Estou colocando o llama3.2 por conta do tamanho de 2GB. Quanto maior o modelo, mais memória é necessário.

```bash
docker exec -it ollama ollama run llama3.2
```

## Configuração da OpenAI - ChatGPT

Conta na OpenAI: Certifique-se de que você tenha uma conta na OpenAI.

API Key: Acesse a página de configurações da OpenAI (`https://platform.openai.com/api-keys`) gere uma chave de API.

# Instalação de pacotes no projeto

Instale o openai: Certifique-se de que o pacote Python da OpenAI esteja instalado. Você pode instalá-lo com:

```bash
pip install openai pypdf chromadb sentence-transformers
```