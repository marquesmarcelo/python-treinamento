# Usando o virtualenv

O virtualenv é uma ferramenta no Python que permite criar ambientes virtuais isolados para projetos. Esses ambientes garantem que cada projeto tenha suas próprias dependências (bibliotecas e versões), separadas do Python global instalado no sistema. Isso é particularmente útil para evitar conflitos de versões de bibliotecas quando você trabalha em múltiplos projetos.

## Testando o virtualenv

Abra o Terminal do Visual Studio

```cmd
virtualenv env
```
Isso criará uma pasta com os arquivos do ambiente virtual.

## Ativando e reativando o ambiente virtual

Depois de criar o ambiente ou de reabrir o vistual studio, no Terminal, você precisa ativá-lo:

* Linux/MacOS:
```bash
source ./env/bin/activate
```

* Windows:
```powershell
.\env\Scripts\activate
```

Quando ativado, você verá o nome do ambiente no início do prompt, indicando que está trabalhando nele.

## Instalar as seguintes bibliotecas

```bash
pip install numpy pandas matplotlib
```

## Escrever o arquivo requirements.txt

O arquivo `requirements.txt` é amplamente utilizado em projetos Python para gerenciar e compartilhar as dependências do projeto. Ele contém uma lista de bibliotecas e suas versões específicas que o projeto utiliza, permitindo que você configure o ambiente de desenvolvimento de maneira rápida e consistente.

```bash
pip freeze > requirements.txt
```

Use o comando `pip freeze > requirements.txt` periodicamente para manter o arquivo atualizado.

Use pip `install -r requirements.txt` ao configurar o ambiente em outra máquina ou após recriar o virtual environment.

## Como Reinstalar as Dependências do requirements.txt

Se você deseja replicar o ambiente ou restaurar dependências em um novo ambiente virtual, use o arquivo requirements.txt:

Ative o ambiente virtual onde deseja instalar as dependências.

Execute:

```bash
pip install -r requirements.txt
```