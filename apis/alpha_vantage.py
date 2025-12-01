"""
Módulo para obtener datos de Alpha Vantage
"""
import requests
import pandas as pd
from datetime import datetime
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import API_KEYS

BASE_URL = 'https://www.alphavantage.co/query'

def obtener_sentimiento_noticias(tickers='GOLD', limite=50):
    """
    Obtener sentimiento de noticias desde Alpha Vantage
    
    Args:
        tickers: Ticker o palabra clave (GOLD, GLD, etc.)
        limite: Número de noticias (max 1000, pero gratis solo 50)
    """
    try:
        params = {
            'function': 'NEWS_SENTIMENT',
            'tickers': tickers,
            'limit': min(limite, 50),  # API gratis limitada
            'apikey': API_KEYS['alphavantage']
        }
        
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if 'feed' not in data:
            print(f"⚠️ Alpha Vantage: {data.get('Note', 'Sin datos')}")
            return pd.DataFrame()
        
        # Procesar feed de noticias
        noticias = []
        for item in data['feed']:
            # Extraer sentimiento
            sentiment_score = float(item.get('overall_sentiment_score', 0))
            sentiment_label = item.get('overall_sentiment_label', 'Neutral')
            
            noticias.append({
                'fecha': pd.to_datetime(item['time_published'], format='%Y%m%dT%H%M%S'),
                'titulo': item.get('title', ''),
                'resumen': item.get('summary', ''),
                'texto': f"{item.get('title', '')} {item.get('summary', '')}",
                'fuente': item.get('source', 'Alpha Vantage'),
                'url': item.get('url', ''),
                'sentimiento': sentiment_score,
                'sentimiento_label': sentiment_label,
                'relevancia': float(item.get('relevance_score', 0))
            })
        
        df = pd.DataFrame(noticias)
        
        if not df.empty:
            df = df.sort_values('fecha', ascending=False)
            print(f"✅ Alpha Vantage: {len(df)} noticias con sentimiento obtenidas")
        
        return df
        
    except Exception as e:
        print(f"❌ Error en Alpha Vantage: {str(e)}")
        return pd.DataFrame()

def obtener_datos_commodity(simbolo='GOLD', intervalo='daily'):
    """
    Obtener datos de commodities (oro, plata, etc.)
    
    Args:
        simbolo: GOLD, SILVER, COPPER, etc.
        intervalo: daily, weekly, monthly
    """
    try:
        funcion_map = {
            'daily': 'TIME_SERIES_DAILY',
            'weekly': 'TIME_SERIES_WEEKLY',
            'monthly': 'TIME_SERIES_MONTHLY'
        }
        
        params = {
            'function': funcion_map.get(intervalo, 'TIME_SERIES_DAILY'),
            'symbol': simbolo,
            'apikey': API_KEYS['alphavantage']
        }
        
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        # Nota: La API gratis tiene límites estrictos (5 requests/min)
        time.sleep(12)  # Esperar entre requests
        
        print(f"✅ Alpha Vantage: Datos de {simbolo} obtenidos")
        return data
        
    except Exception as e:
        print(f"❌ Error obteniendo datos de {simbolo}: {str(e)}")
        return {}

def obtener_indicadores_economicos(indicador='REAL_GDP'):
    """
    Obtener indicadores económicos
    
    Indicadores disponibles:
    - REAL_GDP: PIB real
    - INFLATION: Inflación
    - UNEMPLOYMENT: Desempleo
    - FEDERAL_FUNDS_RATE: Tasa de interés Fed
    """
    try:
        params = {
            'function': indicador,
            'interval': 'quarterly',
            'apikey': API_KEYS['alphavantage']
        }
        
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        print(f"✅ Alpha Vantage: Indicador {indicador} obtenido")
        return data
        
    except Exception as e:
        print(f"❌ Error obteniendo {indicador}: {str(e)}")
        return {}

if __name__ == '__main__':
    # Prueba
    print("Probando Alpha Vantage...")
    
    print("\n1. Sentimiento de noticias sobre oro:")
    df_sentiment = obtener_sentimiento_noticias('GOLD', limite=10)
    
    if not df_sentiment.empty:
        print(f"\n✅ {len(df_sentiment)} noticias con sentimiento")
        print("\nPrimeras 3 noticias:")
        print(df_sentiment[['fecha', 'titulo', 'sentimiento', 'sentimiento_label']].head(3))
        print(f"\nSentimiento promedio: {df_sentiment['sentimiento'].mean():.3f}")
    else:
        print("\n❌ No se obtuvieron datos de sentimiento")
