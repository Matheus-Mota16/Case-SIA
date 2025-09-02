import requests
import xml.etree.ElementTree as ET

def coletar_noticias(pesquisa):
    """Coleta notícias do Google Notícias via RSS."""
    url_rss = f"https://news.google.com/rss/search?q={pesquisa}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url_rss, headers=headers)
        response.raise_for_status()  # Lança um erro para requisições com falha
        xml_data = response.content
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return []

    # Processar o XML
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

if __name__ == "__main__":
    pesquisa1 = "Inteligencia Artificial Piauí"
    pesquisa2 = "SIA Piauí"

    noticias_ia = coletar_noticias(pesquisa1)
    noticias_sia = coletar_noticias(pesquisa2)

    todas_noticias = noticias_ia + noticias_sia

    # Limita a 15 notícias
    if len(todas_noticias) > 15:
        todas_noticias = todas_noticias[:15]

    print(f"Coletadas {len(todas_noticias)} notícias.")