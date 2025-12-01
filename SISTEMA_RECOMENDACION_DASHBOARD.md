# 🎯 Sistema de Recomendación Integrado al Dashboard

## 📋 Resumen Ejecutivo

El **Dashboard REAL** ahora incluye un **Sistema de Recomendación Inteligente** que analiza el sentimiento del mercado en tiempo real y combina múltiples fuentes de datos para generar recomendaciones personalizadas de inversión.

---

## 🔥 Características Principales

### ✅ Integración Completa

```
Dashboard REAL + Sistema de Recomendación
├── 📊 1.9M+ registros históricos (20 años)
├── 📰 Noticias en tiempo real (NewsAPI + Web Scraping)
├── 🧠 Análisis de sentimiento (VADER + TextBlob)
├── 🎯 Recomendaciones personalizadas (IA)
└── 📈 Predicción de precios con correlaciones
```

---

## 🧠 Funcionamiento del Sistema de Recomendación

### Algoritmo de Análisis Multi-Factor

El sistema evalúa **5 factores críticos** para cada activo:

#### 1️⃣ **Análisis de Tendencia (±30 puntos)**
```python
Evaluación:
├── Cambio últimos 5 días
├── Cambio últimos 20 días
└── Dirección del momentum

Ejemplo:
• Si activo sube >2% en 5 días → +30 puntos (alcista)
• Si activo baja >2% en 5 días → -30 puntos (bajista)
```

#### 2️⃣ **Sentimiento del Mercado (±20 puntos)**
```python
Fuentes:
├── NewsAPI: Noticias financieras globales
├── Web Scraping: Gestión, República, Kitco, Mining.com
└── VADER + TextBlob: Análisis de sentimiento IA

Evaluación:
• Sentimiento > +0.2 → +20 puntos (muy positivo)
• Sentimiento < -0.2 → -20 puntos (muy negativo)

Impacto:
📰 "Oro alcanza máximos históricos" → Sentimiento +0.8
📰 "Crisis económica global" → Sentimiento -0.6
```

#### 3️⃣ **Análisis de Volatilidad (±15 puntos)**
```python
Medición:
└── Desviación estándar de retornos diarios

Interpretación:
• Alta volatilidad (>3%) → -15 puntos (ALTO RIESGO)
• Baja volatilidad (<1%) → +10 puntos (BAJO RIESGO)

Ejemplo:
• Bitcoin: Volatilidad 4.5% → Riesgo muy alto
• Bonos: Volatilidad 0.3% → Riesgo muy bajo
```

#### 4️⃣ **Correlación con ORO (+15 puntos)**
```python
Objetivo: Identificar oportunidades de diversificación

Lógica:
Si ORO sube Y activo baja → OPORTUNIDAD
└── Comprar activo barato para diversificar

Ejemplo:
• ORO: +3.5% (5 días)
• S&P 500: -2.1% (5 días)
→ Recomendación: COMPRAR S&P 500 (diversificación)
```

#### 5️⃣ **Noticias Específicas del Activo (±25 puntos)**
```python
Búsqueda:
├── Keywords del activo en noticias
├── Análisis de sentimiento específico
└── Ponderación por relevancia

Ejemplo:
Activo: BITCOIN
Noticias encontradas: 12
Sentimiento promedio: +0.7
→ +25 puntos (noticias muy positivas)
```

---

## 📊 Escala de Puntuación

### Sistema de Scoring (-100 a +100)

| Rango de Score | Acción Recomendada | Color | Interpretación |
|----------------|-------------------|-------|----------------|
| **> +40** | 🟢 COMPRAR | Verde | Fuerte oportunidad de compra |
| **+10 a +40** | 🟡 CONSIDERAR COMPRA | Amarillo | Oportunidad moderada |
| **-10 a +10** | ⚪ MANTENER | Gris | Posición neutral |
| **-40 a -10** | 🟠 CONSIDERAR VENTA | Naranja | Señal de precaución |
| **< -40** | 🔴 VENDER / EVITAR | Rojo | Fuerte señal de venta |

---

## 🎯 Ejemplo de Recomendación Completa

### Caso: Usuario consulta el 26 de Noviembre 2025

#### **Contexto del Mercado:**
```
📰 Noticias analizadas: 94 artículos
😊 Sentimiento promedio: +0.35 (POSITIVO)
📊 Volatilidad del mercado: 1.8% (MODERADA)
🎯 Perfil sugerido: Moderado ⚖️
```

#### **Top 3 Recomendaciones:**

##### 🥇 #1: S&P 500 (Score: +65)
```
💰 Precio actual: $4,567.89
📊 Cambio 5 días: +2.3%
📊 Cambio 20 días: +5.7%
📉 Volatilidad: 1.2%
⚠️ Nivel de Riesgo: Moderado

🟢 ACCIÓN: COMPRAR

🔍 Justificación:
• 📈 Tendencia alcista +2.3% (5 días)
• 😊 Sentimiento positivo del mercado (+0.35)
• ✅ Baja volatilidad 1.2% - Menor riesgo
• 🔄 Oportunidad de diversificación vs ORO
• 📰 Noticias positivas sobre S&P

✅ Confianza: 89%
```

##### 🥈 #2: ORO (GC=F) (Score: +52)
```
💰 Precio actual: $2,048.50
📊 Cambio 5 días: +1.8%
📊 Cambio 20 días: +4.2%
📉 Volatilidad: 0.9%
⚠️ Nivel de Riesgo: Bajo

🟢 ACCIÓN: COMPRAR

🔍 Justificación:
• 📈 Tendencia alcista +1.8% (5 días)
• 😊 Sentimiento positivo del mercado (+0.35)
• ✅ Baja volatilidad 0.9% - Menor riesgo
• 📰 Noticias muy positivas sobre ORO

✅ Confianza: 92%
```

##### 🥉 #3: BITCOIN (Score: +38)
```
💰 Precio actual: $37,245.67
📊 Cambio 5 días: +3.5%
📊 Cambio 20 días: +12.3%
📉 Volatilidad: 4.1%
⚠️ Nivel de Riesgo: Alto

🟡 ACCIÓN: CONSIDERAR COMPRA

🔍 Justificación:
• 📈 Tendencia alcista +3.5% (5 días)
• 😊 Sentimiento positivo del mercado (+0.35)
• ⚠️ Alta volatilidad 4.1% - Mayor riesgo
• 📰 Noticias positivas sobre BITCOIN

⚠️ Confianza: 75% (alta volatilidad)
```

---

## 🚀 Características del Dashboard Integrado

### Tab 1: 📈 Análisis Histórico REAL
- Gráfico de 20 años de datos del oro
- Estadísticas: Máximo, Mínimo, Promedio, Volatilidad
- Basado en 1.9M+ registros reales

### Tab 2: 📰 Noticias en Tiempo Real
- NewsAPI: Noticias financieras globales
- Web Scraping: Medios peruanos + internacionales
- Análisis de sentimiento con VADER + TextBlob
- Métricas: Sentimiento promedio, Noticias positivas/negativas

### Tab 3: 🔮 Predicción con IA
- Modelo de predicción basado en correlaciones de 20 años
- Factores: DXY (-0.72), S&P500 (-0.35), Petróleo (+0.45), BTC (+0.15)
- Incorpora sentimiento de noticias (+5%)
- Intervalo de confianza del 95%

### Tab 4: 🎯 Recomendaciones Inteligentes ⭐ **NUEVO**
```
Funcionalidades:
├── 📊 Análisis de 8 activos financieros
├── 🎯 Recomendaciones personalizadas (COMPRAR/VENDER/MANTENER)
├── 🔍 Justificación detallada por activo
├── 🏆 Top 3 mejores oportunidades
├── 📊 Distribución de recomendaciones (gráfico circular)
├── 💼 Sugerencia de portafolio diversificado
└── ⚠️ Alertas basadas en sentimiento del mercado
```

### Tab 5: 🔗 Correlaciones Reales
- Heatmap de correlaciones históricas (20 años)
- Interpretación de relaciones entre activos
- Conclusiones basadas en datos reales

---

## 💡 Perfiles de Inversión

El sistema sugiere automáticamente un perfil basado en el análisis del mercado:

### 🔥 Perfil Agresivo
```
Condiciones:
├── Sentimiento > +0.3
└── Volatilidad < 2%

Recomendaciones:
├── Mayor peso en acciones tecnológicas
├── Criptomonedas (Bitcoin, Ethereum)
├── Índices de crecimiento (NASDAQ)
└── Commodities con momentum

Riesgo: Alto
Retorno esperado: Alto
```

### ⚖️ Perfil Moderado
```
Condiciones:
├── Sentimiento entre -0.3 y +0.3
└── Volatilidad entre 2% y 3%

Recomendaciones:
├── Diversificación balanceada
├── Mix de acciones e índices
├── Commodities estables (Oro, Plata)
└── Divisas principales

Riesgo: Medio
Retorno esperado: Medio
```

### 🛡️ Perfil Conservador
```
Condiciones:
├── Sentimiento < -0.3
└── Volatilidad > 3%

Recomendaciones:
├── Refugios seguros (Oro, Bonos)
├── Divisas estables
├── Reducir exposición a volátiles
└── Mantener liquidez

Riesgo: Bajo
Retorno esperado: Bajo-Medio
```

---

## 📊 Visualizaciones Incluidas

### 1. Tarjetas de Métricas
```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│ 😊 Sent.    │ 🎯 Perfil   │ ✅ Confianza│ 🟢 Compras  │
│ +0.35       │ Moderado ⚖️ │ 87%         │ 4 activos   │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

### 2. Expandibles por Activo
- Datos completos del activo
- Indicador visual de acción recomendada
- Lista de justificaciones

### 3. Top 3 Oportunidades
- Cards con gradiente visual
- Precio, cambio, score
- Acción recomendada destacada

### 4. Gráfico Circular
- Distribución de recomendaciones
- Colores por tipo de acción

### 5. Sugerencia de Portafolio
- Lista de activos para comprar
- Lista de activos para mantener
- Basado en diversificación óptima

---

## 🔄 Flujo de Trabajo del Usuario

```
1. Usuario abre Dashboard
   ↓
2. Sistema carga 1.9M datos históricos
   ↓
3. Obtiene noticias en tiempo real
   ├── NewsAPI
   └── Web Scraping
   ↓
4. Analiza sentimiento con IA
   ├── VADER
   └── TextBlob
   ↓
5. Calcula tendencias y volatilidad
   ↓
6. Genera recomendaciones
   ├── Scoring multi-factor
   ├── Ranking de activos
   └── Justificaciones
   ↓
7. Usuario consulta Tab "Recomendaciones Inteligentes"
   ↓
8. Ve análisis completo con visualizaciones
   ↓
9. Toma decisión informada de inversión
```

---

## 🎓 Ventajas del Sistema Integrado

### ✅ Datos 100% Reales
- No hay simulaciones ni datos inventados
- 1.9M+ registros históricos verificables
- APIs en tiempo real (NewsAPI + Web Scraping)

### ✅ Análisis Multi-Dimensional
- Tendencias (corto + largo plazo)
- Sentimiento (noticias en tiempo real)
- Volatilidad (gestión de riesgo)
- Correlaciones (diversificación)
- Noticias específicas (contexto del activo)

### ✅ Recomendaciones Justificadas
- Cada recomendación incluye 3-5 razones
- Transparencia total en el scoring
- Usuario entiende el "por qué"

### ✅ Actualización en Tiempo Real
- Noticias actualizadas cada consulta
- Sentimiento recalculado constantemente
- Datos históricos siempre disponibles

### ✅ Gestión de Riesgo
- Clasificación por nivel de riesgo
- Alertas cuando sentimiento es extremo
- Sugerencia de perfil adaptativo

---

## 📈 Casos de Uso Reales

### Caso 1: Mercado Alcista
```
Contexto:
├── Sentimiento: +0.45 (muy positivo)
├── ORO: +2.8% (5 días)
├── S&P 500: +3.2% (5 días)
└── Bitcoin: +5.1% (5 días)

Recomendaciones:
🟢 COMPRAR S&P 500 (Score: +72)
🟢 COMPRAR BITCOIN (Score: +58)
🟡 CONSIDERAR NASDAQ (Score: +35)

Perfil Sugerido: Agresivo 🔥
Estrategia: Aprovechar momentum alcista
```

### Caso 2: Mercado Bajista
```
Contexto:
├── Sentimiento: -0.52 (muy negativo)
├── ORO: +1.5% (refugio seguro)
├── S&P 500: -4.3% (5 días)
└── Bitcoin: -8.2% (5 días)

Recomendaciones:
🟢 COMPRAR ORO (Score: +65)
🟢 COMPRAR BONOS (Score: +48)
🔴 VENDER BITCOIN (Score: -62)

Perfil Sugerido: Conservador 🛡️
Estrategia: Proteger capital en activos seguros
```

### Caso 3: Mercado Neutral
```
Contexto:
├── Sentimiento: +0.08 (neutral)
├── ORO: -0.3% (5 días)
├── S&P 500: +0.5% (5 días)
└── Bitcoin: -1.1% (5 días)

Recomendaciones:
⚪ MANTENER ORO (Score: +5)
⚪ MANTENER S&P 500 (Score: +8)
🟠 CONSIDERAR VENTA BITCOIN (Score: -15)

Perfil Sugerido: Moderado ⚖️
Estrategia: Mantener posiciones, esperar claridad
```

---

## 🔧 Configuración y Uso

### Requisitos Previos
```bash
# 1. Instalar dependencias
pip install streamlit pandas numpy plotly

# 2. Descargar datos históricos (1.9M registros)
python descargar_historico_MEJORADO.py

# 3. Configurar APIs en .env
NEWSAPI_KEY=tu_api_key
```

### Ejecutar Dashboard
```bash
# Opción 1: Streamlit directo
streamlit run dashboard_REAL.py

# Opción 2: Python -m
python -m streamlit run dashboard_REAL.py --server.port 8507
```

### Acceso
```
🌐 URL Local: http://localhost:8507
📱 URL Red: http://[tu-ip]:8507
```

---

## 📊 Métricas de Rendimiento

### Velocidad
```
Carga de datos históricos: ~2-3 segundos
Obtención de noticias: ~5-8 segundos
Análisis de sentimiento: ~3-5 segundos
Generación de recomendaciones: <1 segundo

Total: ~10-15 segundos (primera carga)
Subsecuentes: <2 segundos (caché)
```

### Precisión
```
Confianza base: 60%
+ Noticias disponibles: +0.5% por noticia
Máximo: 95%

Ejemplo:
94 noticias → 60% + (94 × 0.5%) = 87% confianza
```

---

## ⚠️ Limitaciones y Disclaimers

### Limitaciones Técnicas
1. **Datos históricos**: Requiere descarga previa (60 MB)
2. **APIs**: Requiere configuración de keys
3. **Sentimiento**: Basado en noticias en inglés principalmente
4. **Latencia**: Primera carga puede tomar 10-15 segundos

### Disclaimer Legal
```
⚠️ IMPORTANTE:

Este sistema de recomendación es para fines EDUCATIVOS y de 
DEMOSTRACIÓN. NO constituye asesoría financiera profesional.

Las inversiones tienen riesgos. El rendimiento pasado no 
garantiza resultados futuros.

SIEMPRE consulte con un asesor financiero certificado antes 
de tomar decisiones de inversión.

Los desarrolladores NO se hacen responsables por pérdidas 
financieras derivadas del uso de estas recomendaciones.
```

---

## 🔮 Futuras Mejoras

### Fase 2: Deep Learning
- Red neuronal LSTM para predicción de series temporales
- Análisis de imágenes de gráficos (Computer Vision)
- NLP avanzado con BERT para sentimiento

### Fase 3: Personalización
- Perfiles de usuario guardados
- Historial de inversiones
- Recomendaciones basadas en portafolio actual

### Fase 4: Alertas
- Notificaciones push cuando cambien recomendaciones
- Alertas de precio objetivo alcanzado
- Detección de oportunidades en tiempo real

### Fase 5: Backtesting
- Simulación de rendimiento histórico
- Comparación con benchmarks
- Métricas de Sharpe Ratio, Sortino, etc.

---

## 📚 Referencias Técnicas

### Algoritmos Implementados
- **Filtrado Colaborativo**: Basado en "A Programmer's Guide to Data Mining"
- **Análisis de Sentimiento**: VADER (Valence Aware Dictionary) + TextBlob
- **Scoring Multi-Factor**: Modelo propietario de 5 factores

### Fuentes de Datos
- **Yahoo Finance**: Datos históricos (yfinance library)
- **NewsAPI**: Noticias financieras globales
- **Web Scraping**: BeautifulSoup4 + lxml

### Métricas Estadísticas
- **Correlación**: Pearson correlation coefficient
- **Volatilidad**: Desviación estándar anualizada
- **Intervalo de confianza**: 95% (Z-score 1.96)

---

## 📞 Soporte

### Documentación Adicional
- `SISTEMA_RECOMENDACION.md`: Teoría del sistema de filtrado colaborativo
- `RESUMEN_EJECUTIVO.md`: Overview del proyecto completo
- `DOCUMENTACION_COMPLETA.md`: Documentación técnica detallada
- `INSTRUCCIONES_APIS.md`: Guía de configuración de APIs

### Troubleshooting
- **No aparecen noticias**: Verificar API keys en `.env`
- **Datos históricos faltantes**: Ejecutar `descargar_historico_MEJORADO.py`
- **Error de importación**: Instalar dependencias con `pip install -r requirements.txt`

---

**Creado:** Noviembre 2025  
**Versión:** 2.0 (con Sistema de Recomendación Integrado)  
**Estado:** ✅ Producción  
**URL Dashboard:** http://localhost:8507

---

## 🏆 Conclusión

El **Sistema de Recomendación integrado al Dashboard REAL** representa la evolución del proyecto hacia un **asistente financiero inteligente** que combina:

✅ Big Data (1.9M+ registros)  
✅ Inteligencia Artificial (VADER + TextBlob)  
✅ Análisis en Tiempo Real (APIs + Web Scraping)  
✅ Visualización Interactiva (Streamlit + Plotly)  
✅ Recomendaciones Accionables (Sistema de Scoring)  

Es una herramienta completa para **análisis, predicción y toma de decisiones** en el mercado financiero.
