# python-treinamento

Repositório criado para aprendizado da linguagem Python

## Preparação da máquina do desenvolvedor

Criar conta no site github (https://github.com/)

Instalar na máquina de desenvolvimento (máquina Windows):

1 - WSL com Docker (https://github.com/codeedu/wsl2-docker-quickstart)

2 - Visual Studio Code (https://code.visualstudio.com/Download)

3 - Dbeaver (https://dbeaver.io/download/)

4 - Modelio UML (https://www.modelio.org/index.htm)

5 - QGis (https://www.qgis.org/download/)

Dentro da VM Linux no WSL instalar os seguintes pacotes:

```bash
apt install git
```

Instalar o virtualenv em um prompt
```bash
pip install virtualenv
```

Executar o comando abaixo no powershell com permissão de administrator para permitir a execução de Scripts Python no Windows

```powershell
Set-ExecutionPolicy -Scope LocalMachine -ExecutionPolicy RemoteSigned
```