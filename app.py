import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ... (Cole aqui as funções de coleta, processamento e as listas de palavras-chave) ...

# Função principal para o dashboard
def main():
    st.title("Monitoramento de IA no Piauí")
    st.sidebar.header("Configurações")

    # Coleta e processamento dos dados
    with st.spinner("Coletando e processando notícias..."):
        noticias_ia = coletar_noticias("Inteligencia Artificial Piauí")
        noticias_sia = coletar_noticias("SIA Piauí")
        todas_noticias = (noticias_ia + noticias_sia)[:15]
        df_noticias = processar_dados(todas_noticias)

    st.success("Dados coletados e processados!")

    # 1. Gráfico de Pizza de Sentimento
    st.header("Distribuição de Sentimento")
    sentimento_counts = df_noticias['sentimento'].value_counts().reset_index()
    sentimento_counts.columns = ['Sentimento', 'Contagem']
    fig = px.pie(sentimento_counts, values='Contagem', names='Sentimento', title='Análise de Sentimento das Notícias')
    st.plotly_chart(fig)

    # 2. Nuvem de Palavras
    st.header("Nuvem de Palavras-Chave")
    text_for_wordcloud = " ".join(df_noticias['descricao_limpa'].astype(str))
    if text_for_wordcloud:
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_for_wordcloud)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)
    else:
        st.warning("Não há texto suficiente para gerar a nuvem de palavras.")

    # 3. Tabela Interativa
    st.header("Dados Detalhados")
    st.dataframe(df_noticias[['titulo', 'link', 'sentimento']])

    # Etapa 5: Ética e Transparência
    st.markdown("---")
    st.markdown(
        "***Aviso de Limitação:*** *Esta análise de sentimento é baseada em regras simples e "
        "pode não capturar sarcasmo ou contextos complexos.*"
    )
    st.markdown(
        "***Créditos:*** *A estrutura básica de coleta de dados e processamento de texto "
        "foi desenvolvida com o auxílio de um modelo de linguagem de IA, adaptada e validada "
        "manualmente.*"
    )

if __name__ == "__main__":
    main()
def salvar_dados_em_arquivos(df):
    """Salva o DataFrame processado em arquivos CSV e JSON."""
    
    # 1. Salvar como CSV
    # O index=False evita que o pandas adicione uma coluna de índice
    caminho_csv = 'dados_inteligencia_artificial_piaui.csv'
    df.to_csv(caminho_csv, index=False)
    print(f"Dados salvos com sucesso em {caminho_csv}")

    # 2. Salvar como JSON
    # A opção orient='records' salva cada linha como um objeto JSON separado
    caminho_json = 'dados_inteligencia_artificial_piaui.json'
    df.to_json(caminho_json, orient='records', indent=4)
    print(f"Dados salvos com sucesso em {caminho_json}")

if __name__ == "__main__":
    salvar_dados_em_arquivos(df_noticias)
    main()