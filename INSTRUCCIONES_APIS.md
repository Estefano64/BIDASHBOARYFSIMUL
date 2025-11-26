# 🚀 GUÍA RÁPIDA - APIs Gratuitas Tier FREE

## ⚡ Inicio Rápido (5 minutos)

### Paso 1: Instalar Dependencias
```bash
pip install newsapi-python alpha-vantage praw tweepy vaderSentiment streamlit plotly yfinance pandas numpy
```

### Paso 2: Obtener API Keys (GRATIS)

#### 1️⃣ NewsAPI (2 minutos)
1. Visita: https://newsapi.org/register
2. Ingresa tu email y nombre
3. Verifica tu email
4. Copia tu API key: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
5. **Límite:** 100 requests/día, 10,000 artículos/día

#### 2️⃣ Alpha Vantage (1 minuto)
1. Visita: https://www.alphavantage.co/support/#api-key
2. Ingresa tu email
3. Copia tu API key inmediatamente: `XXXXXXXXXXXX`
4. **Límite:** 25 requests/día, 25,000 noticias/día (usa &limit=1000)

#### 3️⃣ Reddit API - PRAW (3 minutos)
1. Visita: https://www.reddit.com/prefs/apps
2. Scroll hasta abajo, click "Create App" o "Create Another App"
3. Llena el formulario:
   - **name:** `ArequipaMiningAnalysis`
   - **App type:** Marca "script"
   - **description:** `Mining sentiment analysis`
   - **about url:** (dejar vacío)
   - **redirect uri:** `http://localhost:8080`
4. Click "Create app"
5. Copia:
   - **client_id:** Está debajo del nombre (14 caracteres)
   - **client_secret:** Dice "secret" (27 caracteres)
6. **Límite:** Ilimitado (60 requests/minuto)

#### 4️⃣ Twitter API v2 (5 minutos)
1. Visita: https://developer.twitter.com/en/portal/dashboard
2. Sign in con tu cuenta de Twitter
3. Click "Create Project" (si es tu primera vez)
4. Llena el formulario:
   - **Project name:** `Mining Sentiment Analysis`
   - **Use case:** Exploring the API
   - **Description:** `Analyzing sentiment about mining in Arequipa`
5. Crea una App dentro del proyecto
6. En "Keys and tokens", genera un "Bearer Token"
7. Copia el Bearer Token (empieza con `AAAA...`)
8. **Límite:** 500,000 tweets/mes (Essential tier)

#### 5️⃣ Yahoo Finance (GRATIS, sin API key)
- No requiere API key
- Ilimitado
- Ya está configurado con `yfinance`

---

## 📝 Paso 3: Configurar API Keys

### Opción A: Directamente en el Notebook
Abre `sentimiento_apis_reales.ipynb` y modifica:

```python
API_KEYS = {
    # NewsAPI
    'newsapi': 'TU_API_KEY_DE_NEWSAPI_AQUI',

    # Alpha Vantage
    'alphavantage': 'TU_API_KEY_DE_ALPHAVANTAGE_AQUI',

    # Reddit (PRAW)
    'reddit': {
        'client_id': 'TU_CLIENT_ID_REDDIT',
        'client_secret': 'TU_CLIENT_SECRET_REDDIT',
        'user_agent': 'ArequipaMiningAnalysis/1.0'
    },

    # Twitter
    'twitter_bearer': 'TU_BEARER_TOKEN_DE_TWITTER'
}
```

### Opción B: Variables de Entorno (Más Seguro)
```python
import os

API_KEYS = {
    'newsapi': os.getenv('NEWSAPI_KEY'),
    'alphavantage': os.getenv('ALPHAVANTAGE_KEY'),
    'reddit': {
        'client_id': os.getenv('REDDIT_CLIENT_ID'),
        'client_secret': os.getenv('REDDIT_CLIENT_SECRET'),
        'user_agent': 'ArequipaMiningAnalysis/1.0'
    },
    'twitter_bearer': os.getenv('TWITTER_BEARER_TOKEN')
}
```

**En Linux/Mac:**
```bash
export NEWSAPI_KEY="tu_api_key"
export ALPHAVANTAGE_KEY="tu_api_key"
export REDDIT_CLIENT_ID="tu_client_id"
export REDDIT_CLIENT_SECRET="tu_client_secret"
export TWITTER_BEARER_TOKEN="tu_bearer_token"
```

**En Windows:**
```cmd
set NEWSAPI_KEY=tu_api_key
set ALPHAVANTAGE_KEY=tu_api_key
set REDDIT_CLIENT_ID=tu_client_id
set REDDIT_CLIENT_SECRET=tu_client_secret
set TWITTER_BEARER_TOKEN=tu_bearer_token
```

---

## ▶️ Paso 4: Ejecutar

### Opción 1: Jupyter Notebook
```bash
jupyter notebook sentimiento_apis_reales.ipynb
```

Ejecuta las celdas en orden:
1. ✅ Importar librerías
2. ✅ Configurar API keys
3. ✅ Probar NewsAPI
4. ✅ Probar Alpha Vantage
5. ✅ Probar Reddit
6. ✅ Probar Twitter
7. ✅ Obtener precios (Yahoo Finance)
8. ✅ Combinar y analizar

### Opción 2: Dashboard Streamlit
```bash
streamlit run app_streamlit.py
```

Se abrirá en `http://localhost:8501`

**Features del Dashboard:**
- 📊 Vista general del sistema
- 📰 Análisis de noticias con sentimiento
- 💰 Gráficos de precios de metales
- 📈 Correlación sentimiento-precio
- ⚙️ Configuración de fuentes en sidebar

---

## 📊 Capacidades Tier FREE

| API | Requests/Día | Datos/Request | Total/Día | Ventajas |
|-----|--------------|---------------|-----------|----------|
| **NewsAPI** | 100 | 100 artículos | 10,000 | Medios peruanos |
| **Alpha Vantage** | 25 | 1,000 noticias | 25,000 | Sentimiento IA |
| **Reddit** | Ilimitado* | Variable | ~5,000+ | Comunidades |
| **Twitter** | ~16,666** | 100/request | ~16,666 | Tiempo real |
| **Yahoo Finance** | ∞ | ∞ | ∞ | Precios reales |

\* 60 requests/minuto
\*\* 500,000/mes ÷ 30 días

**TOTAL: ~56,666+ registros de sentimiento por día**

---

## 🎯 Ejemplos de Uso

### 1. Obtener Noticias de Arequipa
```python
df_newsapi = obtener_noticias_newsapi(
    query='minería Arequipa OR Cerro Verde OR Caylloma',
    days_back=30,
    max_articles=100
)
```

### 2. Sentimiento Financiero con IA
```python
df_alphavantage = obtener_noticias_alphavantage(
    tickers=['GOLD', 'SILVER', 'COPPER'],
    limit=1000  # ¡Usar el máximo!
)
```

### 3. Posts de Reddit
```python
df_reddit = obtener_posts_reddit(
    subreddits=['Peru', 'Arequipa', 'mining', 'Gold'],
    query='minería OR copper OR oro',
    limit=50
)
```

### 4. Tweets en Español
```python
df_twitter = obtener_tweets(
    query='(minería OR mining) (Arequipa OR Peru) -is:retweet lang:es',
    max_results=100
)
```

### 5. Precios de Metales
```python
df_precios = obtener_precios_metales(days=90)
# Oro, Plata, Cobre - Últimos 90 días
```

---

## 💡 Tips y Trucos

### Maximizar Alpha Vantage
```python
# Usar el parámetro limit=1000 para obtener 1000 noticias por request
# En lugar de 50 por defecto
obtener_noticias_alphavantage(tickers=['GOLD'], limit=1000)
```

### NewsAPI - Fuentes Peruanas
```python
# Especificar dominio
newsapi.get_everything(
    q='minería Arequipa',
    domains='gestion.pe,elcomercio.pe,rpp.pe',
    language='es'
)
```

### Reddit - Buscar en Múltiples Subreddits
```python
# Usar el operador OR en query
obtener_posts_reddit(
    subreddits=['Peru', 'Arequipa'],
    query='minería OR cobre OR Cerro Verde'
)
```

### Twitter - Filtros Avanzados
```python
# Excluir retweets, solo español, hashtags específicos
query = '(#MineríaArequipa OR #CerroVerde) -is:retweet lang:es'
```

---

## ⚠️ Límites y Restricciones

### NewsAPI Tier FREE
- ❌ Solo últimos 30 días (no histórico)
- ❌ No se puede sortear por relevancia
- ✅ 100 requests/día es suficiente para análisis diario

### Alpha Vantage Tier FREE
- ⚠️ Solo 25 requests/día
- ✅ Pero 1,000 noticias por request = 25,000 total
- 💡 Tip: Hacer 1 request al día con limit=1000

### Twitter Essential (FREE)
- ❌ Solo últimos 7 días
- ❌ No acceso a métricas avanzadas
- ✅ 500K tweets/mes es MUCHO para análisis

### Reddit PRAW
- ⚠️ 60 requests/minuto (muy generoso)
- ✅ Prácticamente ilimitado si espacias requests
- 💡 Usar time.sleep(1) entre requests

---

## 🔒 Seguridad

### ⚠️ NUNCA subir API keys a GitHub

1. **Crear `.gitignore`:**
```bash
echo "config.py" >> .gitignore
echo ".env" >> .gitignore
```

2. **Usar archivo config.py:**
```python
# config.py (NO subir a GitHub)
NEWSAPI_KEY = "tu_api_key"
ALPHAVANTAGE_KEY = "tu_api_key"
# ...

# En tu notebook
from config import NEWSAPI_KEY, ALPHAVANTAGE_KEY
```

3. **O usar python-dotenv:**
```bash
pip install python-dotenv
```

```python
# .env (NO subir a GitHub)
NEWSAPI_KEY=tu_api_key
ALPHAVANTAGE_KEY=tu_api_key

# En tu notebook
from dotenv import load_dotenv
import os

load_dotenv()
newsapi_key = os.getenv('NEWSAPI_KEY')
```

---

## 🐛 Troubleshooting

### Error: "Invalid API key"
- ✅ Verifica que copiaste la key completa (sin espacios)
- ✅ Algunas APIs requieren activación por email

### Error: "Rate limit exceeded"
- ⚠️ Llegaste al límite diario
- 💡 Espera 24 horas o usa otra API
- 💡 Implementa caching para no repetir requests

### Error: "No results found"
- ✅ Cambia el query (ej: 'minería' en lugar de 'mining')
- ✅ Amplía el rango de fechas
- ✅ Prueba con diferentes keywords

### Reddit: "Invalid credentials"
- ✅ Verifica client_id (14 caracteres)
- ✅ Verifica client_secret (27 caracteres)
- ✅ User agent debe ser descriptivo

### Twitter: "403 Forbidden"
- ✅ Verifica que copiaste el Bearer Token completo
- ✅ Asegúrate de tener Essential tier activado
- ✅ El token empieza con "AAAA..."

---

## 📈 Próximos Pasos

1. ✅ Configurar todas las APIs (15 minutos)
2. ✅ Ejecutar `sentimiento_apis_reales.ipynb`
3. ✅ Verificar que obtienes datos reales
4. ✅ Ejecutar dashboard Streamlit: `streamlit run app_streamlit.py`
5. ✅ Presentar el lunes con datos 100% REALES

---

## 🎉 ¡Listo!

Ahora tienes acceso a:
- ✅ 56,666+ registros de sentimiento por día
- ✅ Datos 100% REALES de 5 fuentes
- ✅ Dashboard interactivo con Streamlit
- ✅ Precios de metales en tiempo real
- ✅ Análisis de correlación sentimiento-precio

**Para tu presentación del lunes:**

*"Implementamos un sistema de análisis de sentimiento con datos 100% REALES utilizando 5 APIs gratuitas tier FREE: NewsAPI para 10,000 noticias diarias de medios peruanos, Alpha Vantage para 25,000 análisis de sentimiento con IA, Reddit para monitoreo ilimitado de comunidades, Twitter para 500,000 tweets mensuales en tiempo real, y Yahoo Finance para precios ilimitados. El sistema puede procesar hasta 56,000+ menciones diarias correlacionadas con precios reales de oro, plata y cobre, todo presentado en un dashboard interactivo con Streamlit."*

🚀 **¡Éxito en tu presentación!**
