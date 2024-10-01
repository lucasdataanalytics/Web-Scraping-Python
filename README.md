# Web-Scraping-Python

Este projeto realiza a extração de dados de livros de Data Science na plataforma do Mercado Livre. Os dados coletados são processados usando `Pandas` e visualizados através de um dashboard interativo utilizando `Streamlit`.

## Funcionalidades

- **Coleta de dados**: Realiza o web scraping de informações sobre livros de Data Science disponíveis no Mercado Livre.
- **Transformação dos dados**: Processamento e limpeza dos dados utilizando a biblioteca `Pandas`.
- **Visualização**: Criação de um dashboard interativo com `Streamlit` para análise dos dados coletados.

## Requisitos

Certifique-se de ter as seguintes dependências instaladas no seu ambiente:

- Python 3.x
- Scrapy
- Pandas
- Streamlit

## Estrutura do Projeto

- **/src:** Contém os arquivos principais de código-fonte, incluindo scripts de web scraping, transformação e o dashboard do Streamlit.
- **/data:** Diretório onde os dados coletados serão salvos.
- **transformacao:** Contém os scripts de transformação de dados usando Pandas.
- **dashboard:** Contém os arquivos do dashboard desenvolvido em Streamlit.

## Como Executar o Projeto

### 1. Executar o Web Scraping
Para rodar o scraper e salvar os dados em formato .jsonl, utilize o seguinte comando dentro da pasta do projeto:

```bash
scrapy crawl mercadolivre -o ../../data/data.jsonl
```

### 2. Processar os Dados com Pandas
Para processar e transformar os dados com Pandas, rode o seguinte comando dentro da pasta src:

```bash
python transformacao/main.py
```

### 3. Rodar o Dashboard com Streamlit
Para visualizar os dados em um dashboard interativo, execute o Streamlit dentro da pasta src:

```bash
streamlit run dashboard/app.py
```
## Configurando o Ambiente Virtual (.venv)

Para isolar as dependências do projeto, criamos um ambiente virtual usando o venv. Siga os passos abaixo para configurar e ativar o ambiente:

### Criar o Ambiente Virtual
No diretório do projeto, execute o seguinte comando para criar o ambiente virtual:

```bash
python -m venv .venv
```
### Ativar o Ambiente Virtual
No diretório do projeto, execute o seguinte comando para criar o ambiente virtual:

```bash
.venv\Scripts\activate
```

### Arquivo .gitignore

Para evitar o versionamento de arquivos indesejados, utilizamos o seguinte modelo de .gitignore recomendado pela [Toptal]('https://www.toptal.com/developers/gitignore/api/python) para projetos Python

## Comandos Scrapy

### Criar um Novo Projeto Scrapy
Para iniciar um novo projeto Scrapy, execute o comando abaixo no diretório onde deseja criar o projeto:

```bash
scrapy startproject nome_do_projeto
```
Este comando cria a estrutura inicial do projeto com diretórios como spiders, settings.py, entre outros.

### Gerar um Spider
Para criar um novo spider, execute o comando abaixo substituindo nome_do_spider pelo nome do spider e dominio.com pelo domínio a ser rastreado:

```bash
scrapy genspider nome_do_spider dominio.com
```
Este comando cria a estrutura inicial do projeto com diretórios como spiders, settings.py, entre outros.