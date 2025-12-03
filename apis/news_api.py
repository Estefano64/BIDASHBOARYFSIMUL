"""
Módulo para obtener noticias reales desde NewsAPI
"""
from newsapi import NewsApiClient
import pandas as pd
from datetime import datetime, timedelta
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import API_KEYS

def obtener_noticias_oro(dias=7, idioma='en'):
    """
    Obtener noticias reales sobre oro desde NewsAPI

    Args:
        dias: Número de días hacia atrás para buscar
        idioma: 'en' (inglés) o 'es' (español)

    Returns:
        DataFrame con noticias
    """
    try:
        # Verificar si la API key existe
        if not API_KEYS.get('newsapi'):
            print("⚠️ NewsAPI: API key no configurada. Configura NEWSAPI_KEY en el archivo .env")
            return pd.DataFrame()

        # Inicializar cliente
        newsapi = NewsApiClient(api_key=API_KEYS['newsapi'])
        
        # Calcular fecha de inicio
        fecha_desde = (datetime.now() - timedelta(days=dias)).strftime('%Y-%m-%d')
        
        # Buscar noticias (NewsAPI gratuito: máximo 100 resultados)
        noticias = newsapi.get_everything(
            q='gold OR "gold price" OR "gold market"',
            language=idioma,
            sort_by='publishedAt',
            from_param=fecha_desde,
            page_size=100
        )
        
        # Procesar artículos
        datos = []
        for articulo in noticias.get('articles', []):
            # Combinar título y descripción para análisis
            texto_completo = f"{articulo.get('title', '')} {articulo.get('description', '')}"
            
            datos.append({
                'fecha': pd.to_datetime(articulo['publishedAt']),
                'titulo': articulo.get('title', 'Sin título'),
                'descripcion': articulo.get('description', ''),
                'texto': texto_completo,
                'fuente': articulo['source']['name'],
                'url': articulo.get('url', ''),
                'autor': articulo.get('author', 'Desconocido')
            })
        
        df = pd.DataFrame(datos)
        
        if not df.empty:
            df = df.sort_values('fecha', ascending=False)
            print(f"✅ NewsAPI: {len(df)} noticias obtenidas")
        else:
            print("⚠️ NewsAPI: No se encontraron noticias")
        
        return df
        
    except Exception as e:
        print(f"❌ Error en NewsAPI: {str(e)}")
        return pd.DataFrame()

def obtener_noticias_por_pais(pais='us', dias=7):
    """
    Obtener noticias principales de un país

    Args:
        pais: Código de país (us, gb, ar, pe, etc.)
        dias: Días hacia atrás
    """
    try:
        # Verificar si la API key existe
        if not API_KEYS.get('newsapi'):
            print("⚠️ NewsAPI: API key no configurada")
            return pd.DataFrame()

        newsapi = NewsApiClient(api_key=API_KEYS['newsapi'])
        
        noticias = newsapi.get_top_headlines(
            q='gold',
            country=pais,
            page_size=50
        )
        
        datos = []
        for articulo in noticias.get('articles', []):
            texto_completo = f"{articulo.get('title', '')} {articulo.get('description', '')}"
            
            datos.append({
                'fecha': pd.to_datetime(articulo['publishedAt']),
                'titulo': articulo.get('title', ''),
                'descripcion': articulo.get('description', ''),
                'texto': texto_completo,
                'fuente': articulo['source']['name'],
                'url': articulo.get('url', ''),
                'pais': pais
            })
        
        return pd.DataFrame(datos)
        
    except Exception as e:
        print(f"❌ Error obteniendo noticias de {pais}: {str(e)}")
        return pd.DataFrame()

if __name__ == '__main__':
    # Prueba
    print("Probando NewsAPI...")
    df = obtener_noticias_oro(dias=3)
    if not df.empty:
        print(f"\n✅ {len(df)} noticias obtenidas")
        print("\nPrimeras 3 noticias:")
        print(df[['fecha', 'titulo', 'fuente']].head(3))
    else:
        print("\n❌ No se obtuvieron noticias")
