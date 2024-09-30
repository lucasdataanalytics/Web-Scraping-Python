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