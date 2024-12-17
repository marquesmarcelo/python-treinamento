# Plano de Estudos

## Material de estudo

Introdução à Programação com Python: http://antigo.scl.ifsp.edu.br/portal/arquivos/2016.05.04_Apostila_Python_-_PET_ADS_S%C3%A3o_Carlos.pdf

Python para Estatísticos: https://tmfilho.github.io/pyestbook/intro.html

Programação Aplicada ao SIG: https://github.com/marcellobenigno/curso_pyqgis

## Ementa

- [x] Aula 1: Introdução e Configuração do Ambiente
* Objetivo: Preparar o ambiente para desenvolvimento em Python.
  - [x] Instalação do Python e configuração do PATH.
  - [x] Instalação de um editor de texto ou IDE (Visual Studio Code, PyCharm ou similar).
  - [x] Configuração do Colab (para quem vai trabalhar na nuvem porém sem suporte a postgres).
  - [x] Configuração do sistema de controle de versão (git)
  - [x] Uso básico do terminal/console.

- [x] Aula 2: Fundamentos de Python
* Objetivo: Revisar os conceitos básicos de Python.
  - [x] Conceitos básicos sobre linguagem de programação.
  - [x] Variáveis e tipos de dados.
  - [x] Manipulação de strings.

- [ ] Aula 3: Fundamentos de Python - continuação
* Objetivo: Revisar os conceitos básicos de Python.
  - [ ] Operadores matemáticos básicos.
  - [ ] Coleções (listas, tuplas e dicionários).
  - [ ] Condições e Laços.

- [ ] Aula 4: Fundamentos de Python - continuação
* Objetivo: Revisar os conceitos básicos de Python.
  - [ ] Funções.
  - [ ] Módulos e Importação.
  - [ ] Instalação de módulos/bibliotecas com pip.
  - [ ] Virtualenv.

- [ ] Aula 5: Orientação a Objetos em Python
* Objetivo: Revisar os conceitos básicos sobre orientação a objetos usando Python.
  - [ ] Classes
  - [ ] Herança e Polimorfismo
  - [ ] Erros e Exceções

- [ ] Aula 6: Computação Matemática e Científica
* Objetivo: Compreender as principais bibliotecas usada no Python para matemática e computação científica.
  - [ ] NumPy
  - [ ] SciPy
  - [ ] Pandas
  - [ ] Matplotlib

--- Em elaboração.

- [ ] Aula 7: Conexão com Arquivos Excel Usando Pandas
* Objetivo: Demonstrar como ler e escrever dados em arquivos Excel.
  - [ ] Leitura de arquivos .xlsx com pandas.read_excel.
  - [ ] Escrita em planilhas Excel com pandas.to_excel.
  - [ ] Manipulação de múltiplas abas.

- [ ] Aula 8: Conexão com Banco de Dados PostgreSQL
* Objetivo: Aprender a se conectar e manipular dados no PostgreSQL usando Pandas.
  - [ ] Configuração da conexão com psycopg2 ou sqlalchemy.
  - [ ] Leitura de dados de tabelas PostgreSQL com pandas.read_sql.
  - [ ] Exportação de DataFrames para PostgreSQL com to_sql.
  
- [ ] Aula 9: Pipeline de Análise de Dados
* Objetivo: Construir um fluxo completo de análise de dados.
  - [ ] Etapas de ETL (Extract, Transform, Load) usando Pandas.
  - [ ] Automatização de rotinas com scripts Python.
  
  ---- conteúdo curso Python Geo

- [ ] Aula 10: Introdução a Python e GIS

Módulo Python GIS 1

1. Apresentação do Módulo

1.1 Introdução ao Geoprocessamento

1.2 Instalação de Programas necessários

2. PyQGIS

2.1 MapCanvas

2.2 Carregando Vetores e Rasters

2.3 Carregando camadas do banco de dados com Python

2.4 Salvando camadas no banco de dados

2.5 Projeto / Exercício

3. Geopandas

3.1 Introdução ao Pandas

3.2 Introdução ao Geopandas

3.3 Entendendo o Geodataframe

3.4 Filtro de dados

3.5 Ferramentas básicas de Geoprocessamento no Geopandas

3.6 Cálculos com Geopandas

3.7 Criando e Salvando arquivos

3.8 Projeto / Exercício

4. GDAL / OGR

4.1 Introdução ao GDAL/OGR

4.2 Entendendo layers, drivers e datasources

4.3 Vetores e rasters

4.4 Ferramentas de Terminal

4.5 Projeto / Exercício

5. Python + Banco de Dados

5.1 Conectando ao banco

5.2 Criando tabelas espaciais

5.3 Populando tabelas espaciais

5.4 Consultas espaciais

5.5 Geoprocessamento no BD

5.6 Projeto / Exercício

Módulo Python GIS 2

1. Apresentação do Módulo

1.1 Instalações necessárias

1.2 Interpolação de dados

1.3 Mapa de nutrientes

1.4 Mapa de pluviometria/temperatura

1.5 Automatizando processos com Python

2. Estatísticas Zonais

2.1 Entendendo a estatística Zonal

2.2 Executando a ferramenta

2.3 Automatizando processo com Python

3. Integrando processos de Interpolação e Estat. Zonal

3.1 Criando script python unificado

4. Caderno de mapas

4.1 Entendendo o caderno de mapas

4.2 Entendendo o Compositor de Impressão

4.3 QGIS - Atlas

4.4 Funções e Itens de mapas dinâmicos

4.5 Automatizando a geração e exportação de mapas dinâmicos com Python

5. Plugins

5.1 Entendendo plugins

5.2 Estrutura padrão de um plugin

5.3 Configurando ambiente para desenvolvimento de plugins

5.4 Criando seu primeiro plugin

6. Integrando Caderno de mapas e Plugins

6.1 Criando script unificado