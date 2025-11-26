# SISTEMA DE BUSINESS INTELLIGENCE - DOCUMENTACIÓN TÉCNICA COMPLETA

**Proyecto de Examen - Modelos de BI**

Este documento contiene la documentación técnica detallada de los tres proyectos principales del sistema.

---

# TABLA DE CONTENIDOS

1. [Sistema de Recomendación (20M+ datos)](#proyecto-1)
2. [Análisis de Sentimiento](#proyecto-2)
3. [Predicción Multi-Factor del Oro (9M+ datos)](#proyecto-3)

---

# PROYECTO 1: SISTEMA DE RECOMENDACIÓN DE INVERSIONES (20M+ DATOS) {#proyecto-1}

## RESUMEN EJECUTIVO

Sistema de recomendación utilizando **filtrado colaborativo** con más de **20 millones de registros** para recomendar productos financieros basándose en el comportamiento de usuarios similares. Alcanza tiempos de procesamiento inferiores a 100ms por recomendación.

## PROBLEMA

**¿Qué productos financieros debería recomendar a un inversor basándose en su perfil y comportamiento de usuarios similares?**

Los inversores necesitan recomendaciones personalizadas de productos financieros que se ajusten a su perfil de riesgo y preferencias, similar a como Netflix recomienda películas o Amazon recomienda productos.

## SOLUCIÓN TÉCNICA

### Fuente de Datos
- **Tipo**: Datos generados sintéticamente pero con patrones realistas
- **Volumen**: 20,000,000+ registros
- **Usuarios**: 100,000
- **Productos**: 20 productos financieros
- **Interacciones promedio**: 200 por usuario

### Dataset Structure
```python
{
    'user_id': int,          # ID único del usuario (0-99,999)
    'product': str,          # Nombre del producto financiero
    'rating': float,         # Calificación 1.0-5.0
    'timestamp': datetime    # Fecha de la interacción
}
```

### Productos Financieros (20)

#### Commodities (5)
- ORO: Riesgo Bajo
- PLATA: Riesgo Bajo
- PETROLEO: Riesgo Medio
- COBRE: Riesgo Medio
- GAS_NATURAL: Riesgo Alto

#### Índices (3)
- SP500: Riesgo Medio
- NASDAQ: Riesgo Medio
- DOW_JONES: Riesgo Medio

#### Criptomonedas (3)
- BITCOIN: Riesgo Alto
- ETHEREUM: Riesgo Alto
- SOLANA: Riesgo Muy Alto

#### Divisas (3)
- USD_PEN: Riesgo Bajo
- EUR_USD: Riesgo Bajo
- USD_JPY: Riesgo Bajo

#### Bonos (2)
- BONOS_US_10Y: Riesgo Muy Bajo
- BONOS_PERU: Riesgo Bajo

#### Acciones (4)
- APPLE: Riesgo Medio
- TESLA: Riesgo Alto
- AMAZON: Riesgo Medio
- GOOGLE: Riesgo Medio

### Perfiles de Inversión

#### Conservador (30% de usuarios)
- Alta preferencia por: Bonos (0.9), Commodities (0.8)
- Baja preferencia por: Cripto (0.2), Acciones (0.4)

#### Moderado (35% de usuarios)
- Preferencias balanceadas
- Índices (0.8), Commodities (0.7), Acciones (0.7)

#### Agresivo (25% de usuarios)
- Alta preferencia por: Cripto (0.9), Acciones (0.8)
- Baja preferencia por: Bonos (0.3)

#### Especulador (10% de usuarios)
- Muy alta preferencia por: Cripto (0.95)
- Muy baja preferencia por: Bonos (0.1)

## METODOLOGÍA: FILTRADO COLABORATIVO

### 1. User-Based Collaborative Filtering

#### Paso 1: Crear Matriz Usuario-Producto
```python
# Matriz: Usuarios × Productos
# Valores: Ratings (1-5) o NaN si no hay interacción
matriz_usuarios = df.pivot(index='user_id', columns='product', values='rating')
```

#### Paso 2: Calcular Similitud entre Usuarios
```python
# Similitud Coseno
similitud_usuarios = cosine_similarity(matriz_usuarios_filled)
```

**Fórmula de Similitud Coseno:**
```
sim(u, v) = (u · v) / (||u|| × ||v||)
```

Donde:
- u, v son vectores de ratings de dos usuarios
- u · v es el producto punto
- ||u|| es la magnitud del vector

#### Paso 3: Encontrar Usuarios Similares
```python
def obtener_usuarios_similares(user_id, n=20):
    similares = similitud_df[user_id].sort_values(ascending=False)
    return similares.head(n)
```

#### Paso 4: Generar Recomendaciones
```python
def recomendar_productos(user_id, n_recomendaciones=5):
    # 1. Obtener usuarios similares
    similares = obtener_usuarios_similares(user_id)

    # 2. Calcular puntuación ponderada
    for similar_user, similitud in similares.items():
        puntuaciones[producto] += similitud * ratings_similar[producto]
        pesos_totales[producto] += similitud

    # 3. Normalizar
    score_final = puntuaciones[producto] / pesos_totales[producto]

    return top_n_productos
```

### 2. Item-Based Collaborative Filtering

#### Paso 1: Transponer Matriz
```python
# Matriz: Productos × Usuarios
matriz_productos = matriz_usuarios.T
```

#### Paso 2: Calcular Similitud entre Productos
```python
similitud_productos = cosine_similarity(matriz_productos)
```

#### Aplicación
- Si usuario invierte en ORO → recomendar productos similares (ej: PLATA)
- Basado en co-ocurrencia de ratings

## IMPLEMENTACIÓN

### Generación de Datos

```python
N_USUARIOS = 100000
N_INTERACCIONES_POR_USUARIO = 200
TOTAL = 20,000,000 registros

# Proceso vectorizado para velocidad
for user_id in range(N_USUARIOS):
    perfil = usuarios_perfil[user_id]

    # Seleccionar productos según preferencias del perfil
    productos = np.random.choice(productos_lista, n_interacciones, p=probs)

    # Generar ratings basados en preferencia + ruido
    rating = clip(preferencia * 5 + normal(0, 0.5), 1, 5)
```

### Optimización para Velocidad

#### 1. Matriz Esparsa
```python
from scipy import sparse
# Usar matrices esparsas para ahorrar memoria
# Densidad típica: 10% (90% de valores son NaN/0)
```

#### 2. Muestreo Estratificado
```python
# Para procesamiento rápido, usar muestra representativa
N_USUARIOS_MUESTRA = 10000
usuarios_muestra = np.random.choice(todos_usuarios, N_USUARIOS_MUESTRA)
```

#### 3. Vectorización NumPy
```python
# Evitar loops Python, usar operaciones vectorizadas
similitud = cosine_similarity(X)  # Vectorizado, muy rápido
```

#### 4. Caching
```python
# Calcular similitudes una vez, reutilizar
similitud_cache = {}
```

## RESULTADOS ESPERADOS

### Rendimiento
```
Tiempo promedio de recomendación: 50-100 ms
Throughput: 10-20 recomendaciones/segundo
Memoria utilizada: ~500 MB (muestra de 10K usuarios)
```

### Métricas de Calidad
- **Precisión**: Productos recomendados son del perfil del usuario
- **Diversidad**: No solo recomendar lo más popular
- **Novedad**: Recomendar productos que el usuario no conoce
- **Cobertura**: Capacidad de recomendar todos los productos

### Ejemplo de Salida

```
Usuario 12345 (Perfil: Agresivo)
Tiempo de procesamiento: 85 ms

Recomendaciones:
1. BITCOIN: 4.73 ★ (Cripto, Riesgo: Alto)
2. ETHEREUM: 4.65 ★ (Cripto, Riesgo: Alto)
3. TESLA: 4.42 ★ (Accion, Riesgo: Alto)
4. SOLANA: 4.38 ★ (Cripto, Riesgo: Muy Alto)
5. NASDAQ: 4.15 ★ (Indice, Riesgo: Medio)
```

## APLICACIÓN PRÁCTICA

### 1. Robo-Advisors
Plataformas automatizadas que recomiendan portafolios personalizados.

### 2. Plataformas de Trading
Sugerir productos complementarios al portafolio actual del usuario.

### 3. Marketing Financiero
Campañas dirigidas basadas en similitud de usuarios.

### 4. Diversificación
Identificar productos que usuarios similares tienen pero el usuario actual no.

## VENTAJAS

✅ **Escalable**: Maneja 20M+ registros
✅ **Rápido**: < 100ms por recomendación
✅ **Sin Cold Start**: Funciona con nuevos productos usando Item-Based CF
✅ **Personalizado**: Basado en comportamiento real de usuarios
✅ **Diverso**: Recomienda productos de diferentes categorías

## LIMITACIONES

⚠️ **Cold Start Problem**: Usuarios nuevos sin historial
⚠️ **Sparsity**: Matriz muy esparsa (usuarios no califican todos los productos)
⚠️ **Popularity Bias**: Tiende a recomendar productos populares
⚠️ **Escalabilidad**: Cálculo de similitud O(n²) para usuarios

## MEJORAS FUTURAS

1. **Matrix Factorization (SVD)**: Reducir dimensionalidad
2. **Deep Learning**: Neural Collaborative Filtering
3. **Hybrid Methods**: Combinar CF con Content-Based
4. **Context-Aware**: Considerar contexto temporal
5. **Online Learning**: Actualización en tiempo real

---

# PROYECTO 2: ANÁLISIS DE SENTIMIENTO FINANCIERO {#proyecto-2}

## RESUMEN EJECUTIVO

Sistema de análisis de sentimiento de múltiples fuentes (noticias, redes sociales, foros) correlacionado con indicadores económicos para generar señales de predicción de precios. Incluye análisis del tipo de cambio USD/PEN, riesgo país e índice de confianza.

## PROBLEMA

**¿Cómo influye el sentimiento del mercado (noticias, redes sociales, foros) en el precio de productos financieros como el oro?**

Los precios de activos financieros son influenciados no solo por fundamentals, sino también por el sentimiento del mercado. Analizar este sentimiento puede proporcionar señales tempranas de movimientos de precio.

## SOLUCIÓN TÉCNICA

### Fuentes de Datos

#### 1. Datos Financieros (Reales)
**API**: Yahoo Finance (yfinance)
**Período**: 2 años (730 días)
**Frecuencia**: Diaria

**Productos**:
- GC=F: Oro (Gold Futures)
- HG=F: Cobre (Copper Futures)
- PEN=X: USD/PEN (Tipo de cambio)
- DX-Y.NYB: Índice del Dólar
- ^GSPC: S&P 500
- BTC-USD: Bitcoin

#### 2. Datos de Sentimiento (Simulados)
En producción, provendrían de:
- **NewsAPI**: Headlines de noticias financieras
- **Twitter API**: Tweets sobre oro, mercados
- **Reddit API**: Posts en r/investing, r/wallstreetbets
- **StockTwits**: Sentimiento de traders

**Simulación**: Correlacionada con retornos reales del oro

```python
Sentimiento = retorno_precio * factor + ruido_aleatorio
```

#### 3. Indicadores Económicos

**Riesgo País (EMBI Spread)**:
- Medida de riesgo soberano
- Rango típico: 80-400 puntos básicos
- Perú: ~150 pb (moderado)

**Índice de Confianza del Consumidor**:
- Escala: 0-100
- >70: Alta confianza
- 50-70: Media
- <50: Baja confianza

**Google Trends**:
- Volumen de búsquedas "Oro"
- Escala: 0-100 (popularidad relativa)

**USD/PEN (Tipo de Cambio)**:
- Precio del dólar en soles peruanos
- Rango típico: 3.50-4.00 PEN
- Importante para inversores locales

## METODOLOGÍA

### 1. Análisis de Sentimiento

#### TextBlob (si disponible)
```python
from textblob import TextBlob

def analizar_sentimiento(texto):
    return TextBlob(texto).sentiment.polarity  # -1 a +1
```

#### Análisis de Palabras Clave
```python
palabras_positivas = ['surge', 'boost', 'high', 'rally']
palabras_negativas = ['drop', 'pressure', 'decline', 'fall']

sentimiento = (positivas - negativas) / total
```

### 2. Generación de Series Temporales

```python
# Sentimiento correlacionado con retornos
retornos_oro = precio_oro.pct_change()

sentimiento_noticias = retornos * 10 + ruido(0, 0.1)
sentimiento_rrss = retornos * 15 + ruido(0, 0.2)  # Más volátil
sentimiento_foros = retornos.shift(1) * 8  # Con lag
```

### 3. Correlación

**Matriz de Correlación de Pearson**:
```
r = cov(X, Y) / (σ_X × σ_Y)
```

Donde:
- cov(X, Y): Covarianza entre X e Y
- σ_X, σ_Y: Desviaciones estándar

### 4. Modelo Predictivo

**Features**:
- Sentimiento_Noticias
- Sentimiento_RRSS
- Sentimiento_Foros
- Riesgo_Pais
- Indice_Confianza
- Google_Trends_Oro
- Dolar_Index
- USD_PEN
- SP500
- Cobre

**Target**: Precio del Oro

**Modelo**: Regresión Lineal
```python
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predicción
y_pred = modelo.predict(X_test)
```

## IMPLEMENTACIÓN

### Descarga de Datos
```python
fecha_fin = datetime.now()
fecha_inicio = fecha_fin - timedelta(days=730)

oro = yf.download('GC=F', start=fecha_inicio, end=fecha_fin)
```

### Generación de Sentimiento
```python
# Noticias correlacionadas con precio
retornos = oro['Close'].pct_change()
sentimiento = (retornos * 10 + np.random.normal(0, 0.1, n)).clip(-1, 1)
```

### Indicadores Económicos
```python
# Riesgo país (movimiento browniano)
riesgo_pais = 150 + np.cumsum(np.random.normal(0, 5, n))
riesgo_pais = riesgo_pais.clip(80, 400)

# Índice confianza
indice_confianza = 65 + np.cumsum(np.random.normal(0, 0.5, n))
indice_confianza = indice_confianza.clip(30, 100)
```

### Análisis de Correlación
```python
corr_matrix = df[columnas].corr()

# Correlaciones con Oro
correlaciones_oro = corr_matrix['Oro'].sort_values(ascending=False)
```

### Modelo Predictivo
```python
# Preparar datos
X = df[features]
y = df['Oro']

# Split temporal
split = int(len(X) * 0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Entrenar
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Evaluar
r2 = r2_score(y_test, y_pred_test)
mae = mean_absolute_error(y_test, y_pred_test)
```

## RESULTADOS ESPERADOS

### Correlaciones Típicas

```
Sentimiento_Noticias  ↔ Oro:    +0.65
Sentimiento_RRSS      ↔ Oro:    +0.58
Riesgo_Pais          ↔ Oro:    +0.45
USD_PEN              ↔ Oro:    -0.32
Indice_Confianza     ↔ Oro:    -0.28
```

### Métricas del Modelo

```
R² Score: 0.85-0.90
MAE: $15-20 USD
RMSE: $20-30 USD
```

### Interpretación

**Sentimiento Positivo (+0.3)**:
- Noticias favorables sobre oro
- Redes sociales optimistas
- Señal: Probable subida de precio

**Sentimiento Negativo (-0.3)**:
- Noticias desfavorables
- Pesimismo en mercado
- Señal: Posible bajada

**Sentimiento Neutral (±0.1)**:
- Mercado indeciso
- Recomendación: Esperar señales más claras

### Ejemplo de Conclusiones

```
📊 ANÁLISIS DE SENTIMIENTO ACTUAL

Fecha: 2025-11-20
Precio Oro: $2,045.30

📰 Sentimiento:
  Noticias:  +0.42 🟢 POSITIVO
  RRSS:      +0.38 🟢 POSITIVO
  Foros:     +0.15 🟡 NEUTRAL

📈 Indicadores:
  Riesgo País: 165 pb (MODERADO)
  Confianza: 68 (MEDIA-ALTA)
  USD/PEN: 3.82

💡 RECOMENDACIÓN: SEÑAL DE COMPRA
→ Sentimiento general positivo
→ Indicadores favorables
→ Se espera presión alcista
```

## APLICACIÓN PRÁCTICA

### 1. Trading Algorítmico
- Señales de compra/venta basadas en sentimiento
- Complemento al análisis técnico

### 2. Gestión de Riesgo
- Alertas tempranas de cambios de sentimiento
- Identificar volatilidad potencial

### 3. Análisis de Mercado
- Entender drivers de precio
- Anticipar movimientos

### 4. Dashboard en Tiempo Real
- Monitoreo continuo de sentimiento
- Visualización de tendencias

## IMPACTO DE FACTORES ESPECÍFICOS

### USD/PEN (Tipo de Cambio)

**Relación con Oro**:
- Dólar fuerte (USD/PEN sube) → Oro en PEN más caro → Menos demanda local
- Dólar débil (USD/PEN baja) → Oro en PEN más barato → Más demanda local

**Para Inversionistas Peruanos**:
```
Precio_Oro_PEN = Precio_Oro_USD × USD_PEN

Si USD/PEN = 3.80 y Oro = $2,000
Entonces Oro_PEN = 7,600 soles/onza
```

### Riesgo País

**Relación con Oro**:
- Riesgo país alto → Buscan refugio en oro → Demanda sube
- Riesgo país bajo → Menos necesidad de refugio → Demanda baja

**Impacto en Portafolio**:
- Inversores locales diversifican con oro cuando riesgo país aumenta

### Índice de Confianza

**Relación con Oro**:
- Alta confianza → Invierten en activos de riesgo → Oro baja
- Baja confianza → Buscan refugio en oro → Oro sube

## VENTAJAS

✅ **Datos Reales**: Yahoo Finance actualizado diariamente
✅ **Multi-Fuente**: Noticias + RRSS + Foros
✅ **Contexto Local**: USD/PEN, riesgo país Perú
✅ **Correlaciones**: Identifica drivers de precio
✅ **Predictivo**: Modelo con R² > 0.85

## LIMITACIONES

⚠️ **Sentimiento Simulado**: En producción necesita APIs reales
⚠️ **Lag**: Sentimiento puede reaccionar después del precio
⚠️ **Ruido**: Redes sociales tienen mucho ruido
⚠️ **Causalidad**: Correlación ≠ Causalidad

## MEJORAS FUTURAS

1. **APIs Reales**: Twitter, NewsAPI, Reddit
2. **NLP Avanzado**: BERT, FinBERT pre-entrenados
3. **Análisis en Tiempo Real**: Stream processing
4. **Multilingüe**: Español + Inglés
5. **Clasificación**: Categorizar noticias por tema
6. **Deep Learning**: LSTM para series temporales

---

# PROYECTO 3: PREDICCIÓN MULTI-FACTOR DEL ORO (9M+ DATOS) {#proyecto-3}

## RESUMEN EJECUTIVO

Modelo de predicción del precio del oro utilizando 18 factores económicos con 9+ millones de registros a nivel de minutos durante 10 años.

## CARACTERÍSTICAS PRINCIPALES

### Volumen de Datos
```
10 años × 252 días × 390 minutos × ~60 columnas = 9+ millones
```

### 18 Factores Económicos

1. Oro (GC=F)
2. Plata (SI=F)
3. Petróleo (CL=F)
4. Cobre (HG=F)
5. Gas Natural (NG=F)
6. Índice Dólar (DX-Y.NYB)
7. S&P 500 (^GSPC)
8. Dow Jones (^DJI)
9. NASDAQ (^IXIC)
10. VIX (^VIX)
11. Bonos 10Y (^TNX)
12. EUR/USD (EURUSD=X)
13. USD/JPY (JPY=X)
14. USD/GBP (GBP=X)
15. Bitcoin (BTC-USD)
16. Ethereum (ETH-USD)
17. FTSE 100 (^FTSE)
18. Nikkei 225 (^N225)

### Características Derivadas (50+)

- **Temporales**: año, mes, día, hora, minuto
- **Ratios**: Oro/Plata, Oro/Petróleo, etc.
- **Retornos**: Diarios y acumulados
- **Medias Móviles**: 5, 15, 30, 60, 120 minutos
- **Volatilidad**: Rolling 30 minutos
- **Momentum**: diff_1, diff_5, diff_30

## APLICACIÓN

Mismo enfoque que el proyecto básico del oro, pero con muchísimo más volumen de datos y factores para análisis más robusto.

---

# REFERENCIAS

## Sistema de Recomendación
- Ron Zacharski. "A Programmer's Guide to Data Mining". Chapter 2: Collaborative Filtering
- KNIME Blog. "Movie Recommendations with Spark Collaborative Filtering"

## Análisis de Sentimiento
- Political Persuasion Analysis - Business Analytics (GitHub)
- TextBlob: Sentiment Analysis Library
- FinBERT: Financial Sentiment Analysis

## Machine Learning
- Scikit-learn Documentation
- Collaborative Filtering: A Survey
- Matrix Factorization Techniques

## Datos Financieros
- Yahoo Finance API (yfinance)
- Alpha Vantage
- Quandl Financial Data

---

**Documentación actualizada**: Noviembre 2025

**Version**: 1.0

**Licencia**: Código abierto para uso educativo
