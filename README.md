# Monitoramento de IA no Piauí

Este projeto é um painel de monitoramento de notícias em tempo real sobre Inteligência Artificial, com um foco especial na cobertura midiática no estado do Piauí. A aplicação coleta artigos de notícias do Google News, realiza uma análise de sentimento simples e apresenta os resultados de forma visual e interativa.

### 🌟 Funcionalidades Principais

* **Coleta de Dados:** Busca e extrai as notícias mais recentes do Google News com base nas palavras-chave "Inteligencia Artificial Piauí" e "SIA Piauí".
* **Análise de Sentimento:** Classifica cada artigo como "Positivo", "Negativo" ou "Neutro" usando uma abordagem baseada em regras simples.
* **Visualização Interativa:** Exibe um painel completo com:
    * **Gráfico de Pizza:** Mostra a distribuição dos sentimentos.
    * **Nuvem de Palavras:** Exibe as palavras-chave mais comuns nas notícias.
    * **Tabela Interativa:** Permite explorar os dados brutos de cada notícia.
* **Identidade Visual Regional:** A interface usa a paleta de cores da bandeira do Piauí para uma estética única e regionalizada.

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação central.
* **Streamlit:** Framework para construir a interface do painel de forma rápida e intuitiva.
* **Pandas:** Usado para manipulação e análise eficiente dos dados.
* **Plotly Express:** Biblioteca para a criação de gráficos interativos.
* **WordCloud:** Para gerar a nuvem de palavras.
* **Requests & BeautifulSoup:** Essenciais para a coleta e o processamento dos dados do Google News.

### 🚀 Como Executar o Projeto

1.  **Instale os Pré-requisitos:** Primeiro, certifique-se de que o Python 3.7 ou superior está instalado em seu sistema.
2.  **Instale as Dependências:** Abra seu terminal, navegue até a pasta do projeto e instale todas as bibliotecas necessárias usando o `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Inicie a Aplicação:** Após a instalação, execute o comando abaixo para iniciar o painel interativo. Ele será aberto automaticamente em seu navegador.

    ```bash
    streamlit run app.py
    ```

### 📁 Estrutura do Projeto

* `app.py`: Contém todo o código da aplicação, desde a coleta de dados até a interface do usuário.
* `requirements.txt`: Lista todas as bibliotecas Python que o projeto precisa para rodar.
* `README.md`: Este arquivo, que serve como guia e documentação do projeto.
* `DECISIONS.md`: Explica as principais escolhas de design e arquitetura do projeto.