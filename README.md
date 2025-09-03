# Painel de Monitoramento de Inteligência Artificial no Piauí

## Visão Geral do Projeto

Este projeto consiste em um painel simplificado para monitorar menções sobre "Inteligência Artificial no Piauí" em fontes de notícias públicas. O painel coleta notícias via RSS, realiza uma análise de sentimento baseada em regras e visualiza os dados em um dashboard interativo usando **Streamlit**.

O principal objetivo é demonstrar um fluxo de trabalho completo, desde a coleta de dados até a visualização final, focando em habilidades como web scraping, processamento de texto, análise de dados e criação de dashboards.

## Funcionalidades

* **Coleta de Dados:** Coleta os 10-15 artigos mais recentes do Google Notícias usando palavras-chave como "Inteligência Artificial Piauí" ou "SIA Piauí".
* **Análise de Sentimento:** Classifica cada notícia como `Positivo`, `Negativo` ou `Neutro` com base em um dicionário de palavras-chave.
* **Visualização Interativa:** Apresenta os resultados em um dashboard que inclui:
    * Um gráfico de pizza mostrando a distribuição dos sentimentos.
    * Uma nuvem de palavras com os termos mais frequentes.
    * Uma tabela interativa com os dados brutos (título, link e sentimento).

## Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado.

## Instalação

1.  Clone este repositório para o seu ambiente local:
    ```bash
    git clone SEU_LINK_DO_REPOSITORIO
    cd nome-do-seu-repositorio
    ```
2.  Instale as bibliotecas necessárias listadas no arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Como Executar o Projeto

Após a instalação, basta executar o script principal com o Streamlit:

```bash
streamlit run app.py