"""
Módulo para obtener tweets sobre oro desde Twitter/X API v2
NOTA: Requiere plan de pago Basic ($100/mes) o superior
"""
import requests
import pandas as pd
from datetime import datetime, timedelta
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import API_KEYS

# Twitter API v2 endpoints
BASE_URL = 'https://api.twitter.com/2'

def obtener_bearer_token():
    """
    Obtener Bearer Token para Twitter API v2
    Requiere API Key y API Secret
    """
    try:
        auth_url = 'https://api.twitter.com/oauth2/token'
        
        # Autenticación con API Key y Secret
        response = requests.post(
            auth_url,
            auth=(API_KEYS['twitter_key'], API_KEYS['twitter_secret']),
            data={'grant_type': 'client_credentials'},
            headers={'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
        )
        
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            print(f"❌ Error obteniendo Bearer Token: {response.status_code}")
            print(f"   {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def buscar_tweets_oro(query='gold OR oro', max_tweets=100):
    """
    Buscar tweets sobre oro
    
    NOTA: Esta función requiere Twitter API v2 con plan de pago
    Plan gratuito NO permite búsqueda de tweets
    
    Args:
        query: Query de búsqueda
        max_tweets: Máximo de tweets (hasta 100 por request en plan Basic)
    
    Returns:
        DataFrame con tweets
    """
    try:
        # Obtener Bearer Token
        bearer_token = obtener_bearer_token()
        
        if not bearer_token:
            print("⚠️ No se pudo obtener Bearer Token")
            print("   Twitter API v2 requiere plan de pago ($100/mes)")
            return pd.DataFrame()
        
        # Endpoint de búsqueda (solo disponible en planes de pago)
        search_url = f"{BASE_URL}/tweets/search/recent"
        
        # Parámetros
        params = {
            'query': f"{query} -is:retweet lang:en",
            'max_results': min(max_tweets, 100),
            'tweet.fields': 'created_at,public_metrics,lang',
            'expansions': 'author_id',
            'user.fields': 'username,verified'
        }
        
        headers = {
            'Authorization': f'Bearer {bearer_token}'
        }
        
        response = requests.get(search_url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            if 'data' not in data:
                print("⚠️ No se encontraron tweets")
                return pd.DataFrame()
            
            tweets = []
            for tweet in data['data']:
                tweets.append({
                    'fecha': pd.to_datetime(tweet['created_at']),
                    'texto': tweet['text'],
                    'likes': tweet['public_metrics']['like_count'],
                    'retweets': tweet['public_metrics']['retweet_count'],
                    'respuestas': tweet['public_metrics']['reply_count'],
                    'fuente': 'Twitter/X',
                    'idioma': tweet.get('lang', 'en')
                })
            
            df = pd.DataFrame(tweets)
            print(f"✅ {len(df)} tweets obtenidos de Twitter/X")
            return df
            
        elif response.status_code == 403:
            print("❌ Error 403: Acceso denegado")
            print("   Tu plan de Twitter API NO incluye búsqueda de tweets")
            print("   Necesitas upgrade a plan Basic ($100/mes)")
            print("   https://developer.twitter.com/en/products/twitter-api")
            return pd.DataFrame()
            
        elif response.status_code == 429:
            print("⚠️ Límite de rate alcanzado. Espera unos minutos.")
            return pd.DataFrame()
            
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return pd.DataFrame()
            
    except Exception as e:
        print(f"❌ Error obteniendo tweets: {str(e)}")
        return pd.DataFrame()

def obtener_tweets_usuario(username='GoldTelegraph', max_tweets=50):
    """
    Obtener tweets de un usuario específico
    NOTA: También requiere plan de pago
    """
    try:
        bearer_token = obtener_bearer_token()
        
        if not bearer_token:
            return pd.DataFrame()
        
        # Primero obtener el user ID
        user_url = f"{BASE_URL}/users/by/username/{username}"
        
        headers = {
            'Authorization': f'Bearer {bearer_token}'
        }
        
        response = requests.get(user_url, headers=headers)
        
        if response.status_code != 200:
            print(f"❌ Usuario @{username} no encontrado")
            return pd.DataFrame()
        
        user_id = response.json()['data']['id']
        
        # Obtener tweets del usuario
        tweets_url = f"{BASE_URL}/users/{user_id}/tweets"
        
        params = {
            'max_results': min(max_tweets, 100),
            'tweet.fields': 'created_at,public_metrics'
        }
        
        response = requests.get(tweets_url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            tweets = []
            for tweet in data.get('data', []):
                tweets.append({
                    'fecha': pd.to_datetime(tweet['created_at']),
                    'texto': tweet['text'],
                    'likes': tweet['public_metrics']['like_count'],
                    'retweets': tweet['public_metrics']['retweet_count'],
                    'usuario': username,
                    'fuente': 'Twitter/X'
                })
            
            return pd.DataFrame(tweets)
        else:
            print(f"❌ Error obteniendo tweets de @{username}")
            return pd.DataFrame()
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return pd.DataFrame()

if __name__ == '__main__':
    print("="*60)
    print("PRUEBA DE TWITTER/X API")
    print("="*60)
    
    print("\n⚠️ NOTA IMPORTANTE:")
    print("   Twitter API v2 requiere plan de pago para:")
    print("   - Búsqueda de tweets")
    print("   - Tweets de usuarios")
    print("   - Streaming")
    print("\n   Plan Free: Solo lectura de perfil")
    print("   Plan Basic: $100/mes - 10,000 tweets/mes")
    print("   Plan Pro: $5,000/mes - 1M tweets/mes")
    
    print("\n" + "="*60)
    print("Intentando buscar tweets...")
    print("="*60)
    
    df_tweets = buscar_tweets_oro(query='gold price', max_tweets=10)
    
    if not df_tweets.empty:
        print(f"\n✅ {len(df_tweets)} tweets obtenidos")
        print("\nPrimeros 3 tweets:")
        for idx, row in df_tweets.head(3).iterrows():
            print(f"\n{idx+1}. {row['texto'][:80]}...")
            print(f"   ❤️ {row['likes']} | 🔄 {row['retweets']}")
    else:
        print("\n❌ No se obtuvieron tweets")
        print("\n💡 SOLUCIÓN:")
        print("   1. Ir a: https://developer.twitter.com/en/portal/products")
        print("   2. Upgrade a Basic ($100/mes)")
        print("   3. Actualizar tu app con el nuevo plan")
        print("   4. Volver a intentar")
