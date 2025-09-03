# =================================================================
# 1. BLOCO DE IMPORTAÇÕES
# Todas as bibliotecas necessárias para o projeto
# =================================================================
import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
import os

# =================================================================
# 2. BLOCO DE VARIÁVEIS E FUNÇÕES DE PROCESSAMENTO E COLETA
# Contém as listas de palavras e todas as funções lógicas do projeto
# =================================================================

# --- Variáveis: Listas de palavras-chave para a análise de sentimento ---
palavras_positivas = ['inovação', 'sucesso', 'crescimento', 'desenvolvimento', 'melhoria', 'avanço', 'futuro']
palavras_negativas = ['desafio', 'problema', 'preocupação', 'risco', 'falha', 'atraso']

# --- Funções de Processamento de Dados ---
def limpar_texto(texto):
    """Remove tags HTML e caracteres especiais."""
    soup = BeautifulSoup(texto, 'html.parser')
    texto_limpo = soup.get_text()
    texto_limpo = re.sub(r'[^\w\s]', '', texto_limpo)
    return texto_limpo.lower()

def classificar_sentimento(texto):
    """Classifica o sentimento baseado em palavras-chave."""
    texto_limpo = limpar_texto(texto)
    pontuacao = 0
    
    for palavra in palavras_positivas:
        if palavra in texto_limpo:
            pontuacao += 1
            
    for palavra in palavras_negativas:
        if palavra in texto_limpo:
            pontuacao -= 1
    
    if pontuacao > 0:
        return 'Positivo'
    elif pontuacao < 0:
        return 'Negativo'
    else:
        return 'Neutro'
        
def processar_dados(noticias):
    """Processa as notícias e adiciona a classificação de sentimento."""
    df = pd.DataFrame(noticias)
    df['descricao_limpa'] = df['descricao'].apply(limpar_texto)
    df['sentimento'] = df['descricao_limpa'].apply(classificar_sentimento)
    return df

# --- Função de Coleta de Dados ---
def coletar_noticias(pesquisa):
    """Coleta notícias do Google Notícias via RSS."""
    url_rss = f"https://news.google.com/rss/search?q={pesquisa}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url_rss, headers=headers)
        response.raise_for_status()
        xml_data = response.content
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return []

    root = ET.fromstring(xml_data)
    noticias = []
    for item in root.findall('.//item'):
        titulo = item.find('title').text
        link = item.find('link').text
        descricao = item.find('description').text
        noticias.append({
            'titulo': titulo,
            'link': link,
            'descricao': descricao
        })
        
    return noticias

# --- Função para salvar arquivos ---
def salvar_dados_em_arquivos(df):
    """Salva o DataFrame processado em arquivos CSV e JSON."""
    caminho_csv = 'dados_inteligencia_artificial_piaui.csv'
    df.to_csv(caminho_csv, index=False)
    print(f"Dados salvos com sucesso em {caminho_csv}")

    caminho_json = 'dados_inteligencia_artificial_piaui.json'
    df.to_json(caminho_json, orient='records', indent=4)
    print(f"Dados salvos com sucesso em {caminho_json}")

# =================================================================
# 3. BLOCO DA APLICAÇÃO STREAMLIT (DASHBOARD)
# Contém a função que cria a interface visual
# =================================================================
def main():
    st.title("Monitoramento de IA no Piauí ✨")
    
    # Coleta e processamento de dados para o dashboard
    with st.spinner("Coletando e processando notícias..."):
        noticias_ia = coletar_noticias("Inteligencia Artificial Piauí")
        noticias_sia = coletar_noticias("SIA Piauí")
        todas_noticias = (noticias_ia + noticias_sia)[:15]
        df_noticias = processar_dados(todas_noticias)
        
    st.success("Dados coletados e processados!")

    # Adicionando a barra lateral para informações secundárias
    st.sidebar.markdown(
        "***Aviso de Limitação:*** *Esta análise de sentimento é baseada em regras simples e "
        "pode não capturar sarcasmo ou contextos complexos.*"
    )
    st.sidebar.markdown(
        "***Créditos:*** *A estrutura básica de coleta de dados e processamento de texto "
        "foi desenvolvida com o auxílio de um modelo de linguagem de IA, adaptada e validada "
        "manualmente.*"
    )

    # 2. Gráfico de Pizza de Sentimento e Métrica de Contagem
    st.header("Análise Geral 📈")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sentimento_counts = df_noticias['sentimento'].value_counts().reset_index()
        sentimento_counts.columns = ['Sentimento', 'Contagem']
        
        # --- Alteração para a paleta de cores do Piauí e mapeamento explícito ---
        cores_piaui_map = {'Positivo': '#006a25', 'Neutro': '#ffcd00', 'Negativo': '#002d72'}
        
        fig = px.pie(sentimento_counts, values='Contagem', names='Sentimento', 
                    title='Distribuição de Sentimento', 
                    color='Sentimento',
                    color_discrete_map=cores_piaui_map)
        st.plotly_chart(fig)

    with col2:
        st.metric(label="Total de Artigos Analisados", value=len(df_noticias))
        
        st.subheader("Nuvem de Palavras-Chave ☁️")
        text_for_wordcloud = " ".join(df_noticias['descricao_limpa'].astype(str))
        if text_for_wordcloud:
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_for_wordcloud)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            st.pyplot(plt)
        else:
            st.warning("Não há texto suficiente para gerar a nuvem de palavras.")
            
    # 4. Tabela Interativa em um expander
    with st.expander("Ver Dados Detalhados 📊"):
        st.dataframe(df_noticias[['titulo', 'link', 'sentimento']])
    
# =================================================================
# 4. BLOCO DE EXECUÇÃO PRINCIPAL
# Este bloco executa o código quando o script é rodado diretamente
# =================================================================
if __name__ == "__main__":
    main()
