# Integração VisualStudio com Github

## Crie um Token de Acesso no GitHub

No GitHub, clique na sua foto de perfil (canto superior direito) e selecione Configurações.

Vá até a seção Developer Settings.

Clique em Personal Access Tokens > Tokens (classic) > Generate new token (classic).

Escolha os escopos necessários (ex.: repo para acesso a repositórios privados).

Clique em Generate Token e copie o token gerado. Guarde-o com segurança, pois ele não será exibido novamente.

## Configurar o VS Code

Instale as Extensões Necessárias

* Abra o VS Code e vá para a aba Extensões (ícone de quadrado no painel esquerdo).
* Instale a extensão GitHub Pull Requests.
* Instale a extensão Python Extension Pack.
* Instale a extensão Markdown All in One.

##  Clone ou Abra o Repositório

### Clone um Repositório:

No VS Code, pressione Ctrl+Shift+P (Windows/Linux) ou Cmd+Shift+P (Mac) para abrir a paleta de comandos.

Digite e selecione Git: Clone.

Insira a URL do repositório GitHub (ex.: https://github.com/username/repository.git).

Escolha um diretório para clonar.

### Abra um Repositório Existente:

Abra o diretório do projeto no VS Code.

Certifique-se de que o Git está inicializado e configurado para o repositório.

## Configure o Token de Acesso no Git

Abra o terminal integrado no VS Code (`Ctrl+```) ou use qualquer terminal.

Use o comando para armazenar o token:

```bash
git config --global credential.helper store
```

Ao realizar a próxima ação de pull, push, ou clone, insira o token como senha:

* Nome de usuário: insira o mesmo usado no GitHub.
* Senha: insira o token gerado no GitHub.

## Testar a Conexão

Execute um comando como git pull ou git push para verificar se o repositório pode ser acessado.

O token será armazenado para futuras conexões.

##  Integração Completa com o GitHub

Para habilitar a integração total com o GitHub:

* Pressione Ctrl+Shift+P e procure Sign in to GitHub.
* Será exibida uma opção para login com o navegador ou token pessoal. Escolha Token.
* Insira o token gerado.