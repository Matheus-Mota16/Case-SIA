# Decisões de Projeto

Este documento detalha as principais decisões tomadas durante o desenvolvimento do projeto "Monitoramento de IA no Piauí". Cada escolha foi feita para otimizar a clareza, a simplicidade e a eficiência do projeto.

### Decisão 1: Unificação do Código em um Único Arquivo (`app.py`)

* **Razão:** Em projetos de pequeno porte como este, a unificação do código em um único arquivo simplifica a estrutura e o fluxo de trabalho. Isso elimina a necessidade de gerenciar múltiplos arquivos e resolver erros de importação. A abordagem "tudo em um" torna o código mais fácil de ser compartilhado, lido e executado por outras pessoas.

### Decisão 2: Uso de Análise de Sentimento Baseada em Regras

* **Razão:** Em vez de usar modelos complexos de aprendizado de máquina, optamos por uma análise de sentimento baseada em listas de palavras-chave. Esta escolha tem uma série de vantagens: é **transparente** (a lógica é clara para qualquer um que leia o código), **rápida** (não exige processamento pesado) e **direta** (o resultado é facilmente compreendido). Embora seja menos sofisticada do que modelos de IA, ela atende perfeitamente ao objetivo de um monitoramento rápido e demonstra a funcionalidade principal de forma clara.

### Decisão 3: Escolha do Streamlit para a Interface do Usuário

* **Razão:** O Streamlit foi a ferramenta ideal, pois permite criar painéis interativos usando apenas Python. Isso eliminou a necessidade de desenvolver uma interface web complexa com HTML, CSS e JavaScript, acelerando drasticamente o processo de desenvolvimento. A sintaxe simples e a capacidade de atualizar a página em tempo real ao salvar o código tornam a experiência de desenvolvimento extremamente eficiente.

### Decisão 4: Implementação da Paleta de Cores do Piauí

* **Razão:** A integração das cores da bandeira do Piauí (`#ffcd00`, `#006a25`, `#002d72`) teve dois objetivos: **estético** e **simbólico**. Esteticamente, a paleta única personaliza a aplicação. Simbolicamente, ela conecta o projeto diretamente ao seu foco regional, o que é um diferencial importante para o público-alvo.

### Decisão 5: Melhorias na Estética e Usabilidade

* **Razão:** Para melhorar a experiência do usuário, foram adicionados elementos de design como:
    * **Barra Lateral (`st.sidebar`):** Usada para mover avisos de limitação e créditos para uma área separada, mantendo o conteúdo principal organizado.
    * **Colunas (`st.columns`):** Foram utilizadas para dispor elementos lado a lado (como o gráfico de pizza e a nuvem de palavras), otimizando o espaço e tornando o layout mais dinâmico.
    * **Expansores (`st.expander`):** Permitem que a tabela de dados brutos seja "escondida" por padrão, o que evita que o painel pareça muito longo e permite ao usuário ver os dados detalhados apenas quando desejar.