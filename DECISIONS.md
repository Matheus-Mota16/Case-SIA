### DECISIONS.md

Este arquivo justifica as escolhas de design e implementação, mostrando o raciocínio por trás das decisões técnicas.

```markdown
# Documentação de Decisões do Projeto

Este documento explica as principais decisões de design e implementação tomadas durante a construção do painel de monitoramento.

## 1. Abordagem de Análise de Sentimento: Baseada em Regras

**Decisão:** Optou-se por uma abordagem de análise de sentimento baseada em regras simples em vez de treinar um modelo de Machine Learning (ML).

**Justificativa:** Para os propósitos deste projeto, que é uma demonstração de fluxo de trabalho completo em uma escala pequena, a simplicidade e a rapidez da abordagem baseada em regras são ideais. Um modelo de ML exigiria:
* **Coleta e Rotulagem de Dados:** Seria necessário coletar e rotular manualmente centenas ou milhares de notícias para criar um conjunto de dados de treinamento.
* **Complexidade Adicional:** Aumentaria a complexidade do código e a quantidade de bibliotecas necessárias (por exemplo, `scikit-learn`, `nltk`).
* **Requisitos de Processamento:** O modelo treinado precisaria ser armazenado e carregado, o que adicionaria tempo de execução.

A abordagem de regras, embora menos sofisticada, cumpre o objetivo de classificar o sentimento de forma satisfatória para a escala do projeto, permitindo que o foco permaneça no fluxo de trabalho geral.

## 2. Tratamento de Erros e Disponibilidade de Dados

**Decisão:** Implementar um tratamento de erros básico para a requisição de dados e garantir que o dashboard lide graciosamente com a falta de notícias.

**Justificativa:** O Google Notícias pode ocasionalmente não retornar resultados para as palavras-chave ou a requisição pode falhar por outros motivos (ex: problemas de rede). É crucial que o aplicativo não "quebre" nessas situações.

* **Tratamento de Requisições:** A função de coleta de dados utiliza um bloco `try-except` com `response.raise_for_status()`. Em caso de erro, uma lista vazia é retornada, permitindo que o restante do script continue a ser executado sem falha.
* **Robustez do Dashboard:** A lógica no `app.py` foi projetada para lidar com DataFrames vazios. Se não houver notícias, a tabela e os gráficos exibirão zero resultados ou mensagens de aviso apropriadas, como "Não há texto suficiente para gerar a nuvem de palavras.", em vez de gerar erros de execução.

Essa decisão garante que a aplicação seja mais robusta e ofereça uma experiência de usuário mais estável, mesmo em condições de dados não ideais.