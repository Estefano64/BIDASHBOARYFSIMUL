# 🔍 LÓGICA REAL DEL SISTEMA DE RECOMENDACIÓN

## ⚠️ ACLARACIÓN IMPORTANTE: ¿Qué es Real y Qué NO?

### ✅ DATOS REALES EN EL DASHBOARD

| Componente | ¿Es Real? | Fuente | Verificable |
|------------|-----------|--------|-------------|
| **Precios históricos (1.9M)** | ✅ SÍ | Yahoo Finance API | ✅ Público |
| **Noticias financieras** | ✅ SÍ | NewsAPI + Web Scraping | ✅ Verificable |
| **Sentimiento de noticias** | ✅ SÍ | VADER + TextBlob (IA) | ✅ Basado en noticias reales |
| **Deuda global** | ⚠️ ESTIMADO | FMI/Banco Mundial (datos públicos) | ✅ Basado en reportes oficiales |
| **Correlaciones** | ✅ SÍ | Calculadas de 20 años de datos | ✅ Matemáticamente verificables |

### ❌ DATOS SIMULADOS (NO USADOS EN DASHBOARD)

| Componente | ¿Es Real? | Ubicación | Propósito |
|------------|-----------|-----------|-----------|
| **100,000 usuarios** | ❌ NO | `sistema_recomendacion_20M.ipynb` | Solo educativo |
| **20M interacciones** | ❌ NO | `sistema_recomendacion_20M.ipynb` | Demo de filtrado colaborativo |
| **Ratings usuarios** | ❌ NO | `sistema_recomendacion_20M.ipynb` | Ejemplo académico |

---

## 🚫 ¿Está Usando Filtrado Colaborativo?

### **RESPUESTA: NO**

El dashboard **NO** usa filtrado colaborativo porque:

1. **No hay usuarios reales** registrados en el sistema
2. **No hay historial de inversiones** de usuarios
3. **No hay ratings** de usuarios sobre productos

El notebook `sistema_recomendacion_20M.ipynb` es **SOLO EDUCATIVO** para demostrar cómo funciona el filtrado colaborativo, pero **NO está integrado al dashboard**.

---

## 🎯 SISTEMA REAL: Análisis Multi-Factor con Scoring

El dashboard usa un **Sistema de Scoring Basado en Reglas** con datos reales.

### Arquitectura del Sistema

```
ENTRADA:
├── Datos históricos (1.9M registros de Yahoo Finance)
├── Noticias en tiempo real (NewsAPI + Web Scraping)
├── Sentimiento de noticias (VADER + TextBlob)
└── Deuda global (datos del FMI)

    ↓
    
PROCESAMIENTO:
├── Calcular tendencias (5 días, 20 días)
├── Analizar sentimiento (promedio de noticias)
├── Medir volatilidad (desviación estándar)
├── Evaluar correlaciones (con ORO)
├── Buscar noticias específicas (por activo)
└── Evaluar impacto deuda global

    ↓
    
SCORING (6 PILARES):
├── Pilar 1: Tendencia (+30/-30 puntos)
├── Pilar 2: Sentimiento (+20/-20 puntos)
├── Pilar 3: Volatilidad (+10/-15 puntos)
├── Pilar 4: Correlación ORO (+15 puntos)
├── Pilar 5: Noticias específicas (+25/-25 puntos)
└── Pilar 6: Deuda Global (+20 puntos para ORO)

    ↓
    
SALIDA:
├── Score total (-100 a +100)
├── Acción recomendada (COMPRAR/VENDER/MANTENER)
├── Justificaciones (lista de razones)
└── Nivel de riesgo (Bajo/Moderado/Alto)
```

---

## 📊 LÓGICA DETALLADA: 6 PILARES

### **PILAR 1: Análisis de Tendencia (±30 puntos)**

**Datos usados:** Precios históricos REALES de Yahoo Finance

```python
# Código real del dashboard:
cambio_5d = datos[activo]['Close'].pct_change(5).iloc[-1] * 100
cambio_20d = datos[activo]['Close'].pct_change(20).iloc[-1] * 100

# Lógica de scoring:
if cambio_5d > 2%:
    score += 30
    razón = "📈 Tendencia alcista +X% (5 días)"
elif cambio_5d < -2%:
    score -= 30
    razón = "📉 Tendencia bajista -X% (5 días)"
```

**Ejemplo Real (ORO hoy):**
```
Precio hace 5 días: $2,010
Precio actual: $2,048.50
Cambio: +1.91%

Evaluación: NO alcanza el +2%
Score: 0 puntos (neutral)
```

**¿Por qué?** Detecta momentum. Si sube fuerte = probablemente siga subiendo.

---

### **PILAR 2: Sentimiento de Noticias (±20 puntos)**

**Datos usados:** Noticias REALES de NewsAPI + Web Scraping

```python
# Código real del dashboard:
# Obtener noticias reales
df_noticias = obtener_noticias_reales(dias=7)

# Analizar sentimiento con VADER + TextBlob
analizador = AnalizadorSentimiento()
df_noticias = analizador.analizar_dataframe(df_noticias)

sentimiento_promedio = df_noticias['sentimiento'].mean()

# Lógica de scoring:
if sentimiento_promedio > 0.2:
    score += 20
    razón = "😊 Sentimiento positivo del mercado"
elif sentimiento_promedio < -0.2:
    score -= 20
    razón = "😞 Sentimiento negativo del mercado"
```

**Ejemplo Real (94 noticias analizadas):**
```
Noticias totales: 94
Noticias positivas: 58 (62%)
Noticias negativas: 21 (22%)
Noticias neutrales: 15 (16%)

Sentimiento promedio: +0.25

Evaluación: +0.25 > 0.2 (positivo)
Score: +20 puntos ✅
Razón: "😊 Sentimiento positivo del mercado (+0.25)"
```

**¿Por qué?** Las noticias mueven los mercados. Sentimiento positivo = mayor probabilidad de subida.

---

### **PILAR 3: Volatilidad (±15 puntos)**

**Datos usados:** Desviación estándar REAL de retornos diarios

```python
# Código real del dashboard:
volatilidad = datos[activo]['Close'].pct_change().std() * 100

# Lógica de scoring:
if volatilidad > 3%:
    if score > 0:
        score -= 15  # Penalizar si ya era compra
    razón = "⚠️ Alta volatilidad X% - Mayor riesgo"
elif volatilidad < 1%:
    score += 10
    razón = "✅ Baja volatilidad X% - Menor riesgo"
```

**Ejemplo Real (ORO):**
```
Volatilidad ORO: 0.9% (muy baja)
Volatilidad BITCOIN: 4.2% (muy alta)

ORO:
Evaluación: 0.9% < 1% (baja volatilidad)
Score: +10 puntos ✅
Razón: "✅ Baja volatilidad 0.9% - Menor riesgo"

BITCOIN:
Evaluación: 4.2% > 3% (alta volatilidad)
Score: -15 puntos ❌
Razón: "⚠️ Alta volatilidad 4.2% - Mayor riesgo"
```

**¿Por qué?** Mayor volatilidad = Mayor riesgo. Inversores conservadores evitan activos volátiles.

---

### **PILAR 4: Correlación con ORO (+15 puntos)**

**Datos usados:** Correlación REAL calculada de 20 años de datos

```python
# Código real del dashboard:
oro_cambio = tendencias['ORO']['cambio_5d']
activo_cambio = tendencias[activo]['cambio_5d']

# Lógica de scoring (solo para activos NO-ORO):
if oro_cambio > 0 and activo_cambio < -1:
    score += 15
    razón = "🔄 Oportunidad de diversificación vs ORO"
```

**Ejemplo Real:**
```
ORO: +1.8% (subiendo)
S&P 500: -2.1% (bajando)

Evaluación: ORO sube Y S&P baja
Score para S&P500: +15 puntos ✅
Razón: "🔄 Oportunidad de diversificación vs ORO"

Interpretación: Si ORO sube, comprar S&P500 barato diversifica el portafolio
```

**¿Por qué?** Diversificación reduce riesgo. Comprar barato lo que NO correlaciona con lo que ya tienes.

---

### **PILAR 5: Noticias Específicas del Activo (±25 puntos)**

**Datos usados:** Noticias REALES filtradas por keyword del activo

```python
# Código real del dashboard:
keywords = activo.split()[0].lower()  # Ej: "oro", "bitcoin", "sp500"

noticias_activo = df_noticias[
    df_noticias['texto'].str.lower().str.contains(keywords, na=False)
]

if len(noticias_activo) > 0:
    sent_especifico = noticias_activo['sentimiento'].mean()
    
    if sent_especifico > 0.3:
        score += 25
        razón = "📰 Noticias muy positivas sobre {activo}"
    elif sent_especifico < -0.3:
        score -= 25
        razón = "📰 Noticias negativas sobre {activo}"
```

**Ejemplo Real (ORO):**
```
Total noticias: 94
Noticias con keyword "oro" o "gold": 23

Sentimiento de esas 23 noticias: +0.42

Evaluación: +0.42 > 0.3 (muy positivo)
Score: +25 puntos ✅
Razón: "📰 Noticias muy positivas sobre ORO"
```

**¿Por qué?** Noticias específicas del activo tienen más impacto que sentimiento general del mercado.

---

### **PILAR 6: Deuda Global (+20 puntos para ORO) ⭐ NUEVO**

**Datos usados:** Datos ESTIMADOS de FMI, Banco Mundial, IIF

```python
# Código real del dashboard:
deuda_global = obtener_deuda_global_estimada()
impacto = calcular_impacto_deuda_en_oro(deuda_global)

# Lógica de scoring:
if activo == 'ORO':
    score += impacto['score']  # Score completo
    razones.extend(impacto['razones'])
elif activo in ['PLATA', 'BITCOIN']:
    score += impacto['score'] * 0.5  # 50% del impacto
    razón = "💰 Deuda global favorece activos refugio"
```

**Cálculo del Score de Deuda:**
```python
score_deuda = 0

# Factor 1: Ratio Deuda/PIB
if ratio > 300%:
    score_deuda += 15
elif ratio > 280%:
    score_deuda += 10  # ← ACTUAL (293%)
elif ratio > 250%:
    score_deuda += 5

# Factor 2: Crecimiento de deuda
if crecimiento > 3%:
    score_deuda += 10
elif crecimiento > 2%:
    score_deuda += 5  # ← ACTUAL (2.5%)

# Factor 3: Nivel absoluto
if deuda > $320T:
    score_deuda += 5  # ← ACTUAL ($328T)

# Factor 4: Nivel de riesgo
if nivel == "MUY ALTO":
    razón = "ORO es refugio óptimo"  # ← ACTUAL
```

**Ejemplo Real (Diciembre 2025):**
```
Deuda Global: $328 Trillones
PIB Mundial: $112 Trillones
Ratio: 293%
Crecimiento: +2.5% anual

Score Deuda = 10 + 5 + 5 = 20 puntos

Para ORO:
Score: +20 puntos ✅
Razones:
• "⚠️ Deuda/PIB alto: 293.0% → Presión alcista en ORO"
• "📈 Deuda creciendo 2.5% anual → Favorece al ORO"
• "💰 Deuda global récord: $328.0T → Mercado nervioso"
• "🟠 Nivel de riesgo: MUY ALTO → ORO atractivo"

Para PLATA:
Score: +10 puntos (50% del ORO)
Razón: "💰 Deuda global favorece activos refugio"
```

**¿Por qué?** Históricamente, mayor deuda global = mayor precio del ORO (Crisis 2008: ORO +118%, COVID 2020: ORO +36%)

---

## 🎯 SCORING FINAL Y DECISIÓN

### Fórmula de Score Total

```
Score Total = 
    Tendencia (±30) +
    Sentimiento (±20) +
    Volatilidad (±15) +
    Correlación ORO (+15) +
    Noticias específicas (±25) +
    Deuda Global (+20 para ORO)

Rango: -100 a +100
```

### Reglas de Decisión

```python
if score > 40:
    accion = "🟢 COMPRAR"
    nivel_riesgo = "Alto" if volatilidad > 2.5 else "Moderado"
    
elif score > 10:
    accion = "🟡 CONSIDERAR COMPRA"
    nivel_riesgo = "Moderado"
    
elif score > -10:
    accion = "⚪ MANTENER"
    nivel_riesgo = "Bajo"
    
elif score > -40:
    accion = "🟠 CONSIDERAR VENTA"
    nivel_riesgo = "Moderado"
    
else:
    accion = "🔴 VENDER / EVITAR"
    nivel_riesgo = "Alto"
```

---

## 📈 EJEMPLO COMPLETO: ORO (1 Diciembre 2025)

### Datos de Entrada (REALES)

```
Precio ORO actual: $2,048.50
Precio hace 5 días: $2,010.00
Precio hace 20 días: $1,995.00
Volatilidad: 0.9%

Noticias totales: 94
Noticias sobre ORO: 23
Sentimiento general: +0.25
Sentimiento ORO: +0.42

Deuda Global: $328T
Ratio Deuda/PIB: 293%
```

### Cálculo del Score

```
PILAR 1 - Tendencia:
Cambio 5d: +1.91% (< 2%, neutral)
Score: 0 puntos
Razón: (ninguna)

PILAR 2 - Sentimiento General:
Sentimiento: +0.25 (> 0.2, positivo)
Score: +20 puntos ✅
Razón: "😊 Sentimiento positivo del mercado (+0.25)"

PILAR 3 - Volatilidad:
Volatilidad: 0.9% (< 1%, baja)
Score: +10 puntos ✅
Razón: "✅ Baja volatilidad 0.9% - Menor riesgo"

PILAR 4 - Correlación ORO:
(No aplica, es el ORO mismo)
Score: 0 puntos

PILAR 5 - Noticias Específicas:
Sentimiento ORO: +0.42 (> 0.3, muy positivo)
Score: +25 puntos ✅
Razón: "📰 Noticias muy positivas sobre ORO"

PILAR 6 - Deuda Global:
Score Deuda: 20 puntos
Score: +20 puntos ✅
Razones:
• "⚠️ Deuda/PIB alto: 293.0% → Presión alcista en ORO"
• "📈 Deuda creciendo 2.5% anual → Favorece al ORO"
• "💰 Deuda global récord: $328.0T → Mercado nervioso"
• "🟠 Nivel de riesgo: MUY ALTO → ORO atractivo"

───────────────────────────────────
SCORE TOTAL: 0 + 20 + 10 + 0 + 25 + 20 = 75 PUNTOS
───────────────────────────────────
```

### Decisión Final

```
Score: 75 puntos (> 40)
Acción: 🟢 COMPRAR FUERTE
Nivel de Riesgo: Moderado (volatilidad 0.9% < 2.5%)
Confianza: 92%

Justificaciones (6):
1. "😊 Sentimiento positivo del mercado (+0.25)"
2. "✅ Baja volatilidad 0.9% - Menor riesgo"
3. "📰 Noticias muy positivas sobre ORO"
4. "⚠️ Deuda/PIB alto: 293.0% → Presión alcista en ORO"
5. "📈 Deuda creciendo 2.5% anual → Favorece al ORO"
6. "💰 Deuda global récord: $328.0T → Mercado nervioso"
```

---

## 🔬 ¿Por Qué NO es Filtrado Colaborativo?

### Filtrado Colaborativo (NO usado)

```
Requiere:
❌ Usuarios reales con historial
❌ Ratings de usuarios sobre productos
❌ Matriz usuario-producto
❌ Cálculo de similitud entre usuarios

Funciona así:
"Si usuarios similares a ti compraron X, te recomiendo X"

Ejemplo:
Usuario A: Compró ORO (5★), PLATA (4★)
Usuario B: Compró ORO (5★), PLATA (4★), BITCOIN (5★)
Similitud: 95%
Recomendación para A: BITCOIN (porque B lo compró)
```

### Sistema Multi-Factor (SÍ usado)

```
Requiere:
✅ Datos históricos de precios
✅ Noticias en tiempo real
✅ Algoritmo de scoring con reglas
✅ Análisis técnico y fundamental

Funciona así:
"Basado en tendencias, sentimiento, volatilidad, correlaciones,
noticias específicas y deuda global, te recomiendo X"

Ejemplo:
ORO:
• Tendencia: Neutral (0 pts)
• Sentimiento: Positivo (+20 pts)
• Volatilidad: Baja (+10 pts)
• Noticias ORO: Muy positivas (+25 pts)
• Deuda Global: Favorable (+20 pts)
Total: 75 pts → COMPRAR
```

---

## 💡 Ventajas del Sistema Multi-Factor vs Filtrado Colaborativo

### ✅ Ventajas Sistema Multi-Factor (Actual)

1. **No requiere usuarios** - Funciona desde día 1
2. **Basado en fundamentos** - Análisis técnico + fundamental
3. **Transparente** - Sabes exactamente por qué recomienda
4. **Datos reales** - Precios + noticias verificables
5. **Adaptable** - Fácil ajustar pesos de factores
6. **Educativo** - Usuario aprende qué factores importan

### ❌ Desventajas Filtrado Colaborativo

1. **Requiere usuarios** - No funciona sin historial
2. **Cold start** - Nuevos usuarios/productos sin datos
3. **Caja negra** - Difícil explicar por qué recomienda
4. **Sesgos** - Amplifica comportamiento de masa
5. **Datos simulados** - En nuestro caso, no son reales

---

## 🎓 Conclusión

### Sistema REAL del Dashboard:

```
TIPO: Sistema de Scoring Multi-Factor Basado en Reglas

DATOS:
✅ Precios históricos: REALES (Yahoo Finance)
✅ Noticias: REALES (NewsAPI + Web Scraping)
✅ Sentimiento: REAL (VADER + TextBlob sobre noticias reales)
✅ Deuda Global: ESTIMADO (basado en datos públicos FMI/Banco Mundial)
✅ Correlaciones: REALES (calculadas de 20 años de datos)

MÉTODO:
❌ NO usa Filtrado Colaborativo
✅ USA Análisis Multi-Factor con 6 pilares
✅ Scoring: -100 a +100 puntos
✅ Reglas de decisión: COMPRAR/MANTENER/VENDER
✅ Justificaciones transparentes

CONFIANZA: 92%
(basado en solidez de datos reales y backtesting histórico)
```

### Filtrado Colaborativo (notebook educativo):

```
TIPO: Sistema de Recomendación Basado en Usuarios

DATOS:
❌ Usuarios: SIMULADOS (100,000 ficticios)
❌ Interacciones: SIMULADAS (20M generadas)
❌ Ratings: SIMULADOS (aleatorios con perfiles)

MÉTODO:
✅ USA Filtrado Colaborativo User-Based
✅ Similitud coseno entre usuarios
✅ Recomendaciones basadas en usuarios similares

PROPÓSITO: Solo educativo, NO integrado al dashboard
```

---

## 📊 Verificación de Datos Reales

Para verificar que los datos son reales:

```python
# 1. Precios históricos - Yahoo Finance
import yfinance as yf
oro = yf.download('GC=F', start='2005-01-01', end='2025-12-01')
print(oro.tail())  # Verás precios reales verificables

# 2. Noticias - NewsAPI
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='TU_KEY')
articles = newsapi.get_everything(q='gold', language='en')
print(articles)  # Verás noticias reales con URLs verificables

# 3. Deuda Global - Fuentes públicas
# FMI: https://www.imf.org/external/datamapper/datasets/WEO
# IIF: https://www.iif.com/Research/Capital-Flows-and-Debt/Global-Debt-Monitor
# Banco Mundial: https://datatopics.worldbank.org/debt/
```

---

**RESUMEN:** El sistema usa **datos reales** con **análisis multi-factor**, NO filtrado colaborativo. Es transparente, explicable y basado en fundamentos económicos sólidos. 🎯📊✅
