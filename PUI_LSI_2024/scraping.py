import requests
from bs4 import BeautifulSoup


# Función para scrapeo genérico de noticias
def scrape_news(url):
    try:
        # Realizamos la solicitud GET a la página web
        response = requests.get(url)
        response.raise_for_status()  # Verificamos si hubo errores en la solicitud

        # Creamos el objeto BeautifulSoup para analizar el contenido HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extraemos el título de la página
        title = soup.title.text
        print(f'Título de la página ({url}): {title}\n')

        # Extraemos todos los enlaces de la página
        links = soup.find_all('a')
        for index, link in enumerate(links, start=1):
            link_text = link.text.strip()
            link_url = link['href']
            print(f'Elemento {index}:')
            print(f'Texto: {link_text}')
            print(f'Enlace: {link_url}\n')

    except requests.exceptions.RequestException as e:
        print(f"No se pudo obtener datos de {url}. Error: {e}")


# URL de Diario Panorama
url = 'https://www.nuevodiarioweb.com.ar/'

# Realizamos el scrapeo de la página de Diario Panorama
scrape_news(url)
