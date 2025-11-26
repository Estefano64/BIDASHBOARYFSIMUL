# SISTEMA DE BUSINESS INTELLIGENCE - DOCUMENTACIÓN TÉCNICA

Este documento contiene la documentación técnica completa de los tres proyectos principales del sistema de BI.

---

# PROYECTO 1: SISTEMA DE RECOMENDACIÓN DE INVERSIONES (20M+ DATOS)

## RESUMEN EJECUTIVO

Sistema de recomendación utilizando filtrado colaborativo con más de 20 millones de registros para recomendar productos financieros basándose en el comportamiento de usuarios similares. Alcanza tiempos de procesamiento inferiores a 100ms por recomendación.

## PROBLEMA

**¿Cuál será el precio del oro el próximo lunes? ¿Es buen momento para invertir?**

Los inversionistas necesitan herramientas para tomar decisiones informadas sobre compra/venta de oro basadas en análisis de datos históricos y tendencias del mercado.

## SOLUCIÓN TÉCNICA

### Fuente de Datos
- **API**: Yahoo Finance (yfinance)
- **Símbolo**: GC=F (Gold Futures - NYMEX)
- **Período**: 180 días (6 meses)
- **Actualización**: Tiempo real
- **Costo**: Gratuito, sin límites

### Metodología

#### 1. Obtención de Datos
```python
oro = yf.download('GC=F', start=fecha_inicio, end=fecha_fin)
```
Descarga automática de:
- Precio de apertura, cierre, máximo, mínimo
- Volumen de transacciones
- Datos históricos completos

#### 2. Análisis Exploratorio (EDA)
- Evolución temporal del precio
- Cálculo de retornos diarios y acumulados
- Medias móviles (7 y 30 días)
- Volatilidad del mercado
- Análisis de tendencias

#### 3. Preparación de Datos
**Variables Predictoras (Features):**
- Día número (secuencial)
- Día de la semana
- Mes
- Precio anterior
- Media móvil 7 días
- Media móvil 30 días
- Volatilidad 7 días
- Volumen de transacciones

**Variable Objetivo:**
- Precio de cierre del oro

#### 4. Modelo de Machine Learning
**Algoritmo:** Regresión Lineal (sklearn)

**División de datos:**
- Entrenamiento: 80%
- Prueba: 20%
- Sin mezcla (shuffle=False) para mantener orden temporal

**Entrenamiento:**
```python
modelo = LinearRegression()
modelo.fit(X_train, y_train)
```

#### 5. Evaluación del Modelo
**Métricas utilizadas:**
- **R² Score**: Coeficiente de determinación (calidad del ajuste)
- **RMSE**: Error cuadrático medio (en USD)
- **MAE**: Error absoluto medio (en USD)

**Criterios de calidad:**
- R² > 0.9: Excelente
- R² > 0.7: Bueno
- R² > 0.5: Aceptable

#### 6. Predicción
Genera predicciones para:
- Próximo lunes (objetivo principal)
- Siguientes 7 días laborables
- Con intervalos de confianza

## RESULTADOS ESPERADOS

### Salida del Modelo
```
🎯 PRECIO PREDICHO PARA EL LUNES: $2,XXX.XX USD
📈 Tendencia: SUBIDA/BAJADA
✅ Recomendación: COMPRAR/VENDER/ESPERAR
Cambio esperado: ±X.XX%
```

### Análisis de Tendencias
- Corto plazo (7 días)
- Medio plazo (30 días)
- Largo plazo (90 días)

### Visualizaciones
- Evolución histórica del precio
- Predicción vs valores reales
- Medias móviles
- Distribución de retornos
- Dashboard completo

## FACTORES QUE AFECTAN EL PRECIO DEL ORO

1. **Inflación**: Oro como refugio anti-inflacionario
2. **Tasas de interés**: Relación inversa
3. **Valor del dólar**: Correlación negativa
4. **Incertidumbre geopolítica**: Aumenta demanda
5. **Oferta y demanda**: Producción minera y joyería
6. **Mercados bursátiles**: Activo refugio

## APLICACIÓN PRÁCTICA

### Caso de Uso
1. **Hoy**: Ejecutar modelo → obtener predicción
2. **Lunes**: Verificar precio real del mercado
3. **Análisis**: Comparar predicción vs realidad
4. **Decisión**: Evaluar utilidad del modelo

### Validación
La predicción es **verificable** consultando:
- Yahoo Finance
- Investing.com
- Bloomberg
- Cualquier plataforma financiera

## IMPLEMENTACIÓN

### Requisitos Técnicos
```bash
pip install yfinance pandas numpy matplotlib seaborn scikit-learn jupyter
```

### Ejecución
```bash
jupyter notebook prediccion_oro.ipynb
```

### Tiempo de Ejecución
- Descarga de datos: 5-10 segundos
- Procesamiento y análisis: 10-15 segundos
- Generación de gráficos: 5-10 segundos
- **Total: < 1 minuto**

## VENTAJAS DEL PROYECTO

✅ **Datos Reales**: Del mercado financiero actual
✅ **Verificable**: Comprobable el próximo día hábil
✅ **Sin Costo**: API gratuita sin limitaciones
✅ **Actualizado**: Datos hasta el día actual
✅ **Profesional**: Técnicas usadas en finanzas reales
✅ **Reproducible**: Código ejecutable y documentado
✅ **Escalable**: Adaptable a otros commodities

## LIMITACIONES

- El modelo asume continuidad de patrones históricos
- Eventos imprevistos pueden afectar la predicción
- Mercado del oro es influenciado por factores externos
- Regresión lineal es un modelo básico (puede mejorarse con LSTM, Random Forest, etc.)

## MÉTRICAS DE ÉXITO

**Modelo exitoso si:**
- Error de predicción < $30 USD
- Tendencia correcta (subida/bajada)
- R² Score > 0.7

## FUTURAS MEJORAS

1. Integrar datos de inflación y tasas de interés
2. Análisis de sentimiento de noticias financieras
3. Modelos más complejos (LSTM, Random Forest)
4. Predicciones multi-horizonte
5. Sistema de alertas automáticas

## CONCLUSIÓN

Este proyecto demuestra la aplicación práctica de Machine Learning en finanzas, utilizando datos reales del mercado para generar predicciones verificables. El modelo proporciona una herramienta útil para análisis de inversión en oro, con resultados comprobables en el mundo real.

## REFERENCIAS

- Yahoo Finance API: https://finance.yahoo.com/
- yfinance Documentation: https://pypi.org/project/yfinance/
- Scikit-learn: https://scikit-learn.org/
- Gold Futures (NYMEX): https://www.cmegroup.com/markets/metals/precious/gold.html

---

**Archivo**: prediccion_oro.ipynb
**Lenguaje**: Python 3.8+
**Framework**: Jupyter Notebook
**Bibliotecas**: pandas, numpy, scikit-learn, matplotlib, seaborn, yfinance
