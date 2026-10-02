import requests
from bs4 import BeautifulSoup

def buscar_descripcion_web(nombre_herramienta):
    """
    Función base del Spider que buscará la definición de una herramienta en la web.
    """
    url = f"https://es.wikipedia.org/wiki/{nombre_herramienta.replace(' ', '_')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            parrafos = soup.find_all("p")
            for p in parrafos:
                texto = p.get_text().strip()
                if len(texto) > 40:
                    return texto
        return "No se encontró una descripción automática."
    except Exception as e:
        return f"Error al buscar en la web: {str(e)}"