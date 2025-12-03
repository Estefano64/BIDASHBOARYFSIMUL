"""
Configuración de APIs
Carga las claves de forma segura desde el archivo .env o usa las predefinidas
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# API Keys (con fallback a claves predefinidas)
API_KEYS = {
    'newsapi': os.getenv('NEWSAPI_KEY', 'uvS6HzVfbJavtwuiyQ40cCOAlEysfYaR'),  # API key configurada
    'alphavantage': os.getenv('ALPHAVANTAGE_KEY'),
    'twitter_key': os.getenv('TWITTER_API_KEY'),
    'twitter_secret': os.getenv('TWITTER_API_SECRET'),
    'reddit_client_id': os.getenv('REDDIT_CLIENT_ID'),
    'reddit_secret': os.getenv('REDDIT_SECRET')
}

# Verificar que las claves están configuradas
def verificar_apis():
    """Verificar qué APIs están disponibles"""
    disponibles = {}
    
    if API_KEYS['newsapi']:
        disponibles['NewsAPI'] = True
    else:
        disponibles['NewsAPI'] = False
    
    if API_KEYS['alphavantage']:
        disponibles['AlphaVantage'] = True
    else:
        disponibles['AlphaVantage'] = False
    
    if API_KEYS['twitter_key'] and API_KEYS['twitter_secret']:
        disponibles['Twitter'] = True
    else:
        disponibles['Twitter'] = False
    
    if API_KEYS['reddit_client_id'] and API_KEYS['reddit_secret']:
        disponibles['Reddit'] = True
    else:
        disponibles['Reddit'] = False
    
    return disponibles

if __name__ == '__main__':
    print("Estado de APIs:")
    for api, estado in verificar_apis().items():
        print(f"  {api}: {'✅ Disponible' if estado else '❌ No configurada'}")
