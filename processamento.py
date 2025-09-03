import pandas as pd
from bs4 import BeautifulSoup
import re

# Listas de palavras para análise de sentimento
# Adapte estas listas para o seu contexto
palavras_positivas = ['inovação', 'sucesso', 'crescimento', 'desenvolvimento', 'melhoria', 'avanço']
palavras_negativas = ['desafio', 'problema', 'preocupação', 'risco', 'falha', 'atraso']

def limpar_texto(texto):
    """Remove tags HTML e caracteres especiais."""
    # Remove tags HTML
    soup = BeautifulSoup(texto, 'html.parser')
    texto_limpo = soup.get_text()
    # Remove caracteres especiais
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
    
    # ... (código da Etapa 1) ...

def processar_dados(noticias):
    """Processa as notícias e adiciona a classificação de sentimento."""
    df = pd.DataFrame(noticias)
    df['descricao_limpa'] = df['descricao'].apply(limpar_texto)
    df['sentimento'] = df['descricao_limpa'].apply(classificar_sentimento)
    return df

if __name__ == "__main__":
    # ... (coleta das notícias) ...

    df_noticias = processar_dados(todas_noticias)
    print("\nDataFrame com notícias processadas:")
    print(df_noticias.head())