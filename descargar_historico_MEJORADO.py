"""
🚀 DESCARGA MASIVA MEJORADA - ESTRATEGIA INTELIGENTE
=====================================================

Yahoo Finance tiene límites:
- Datos de 1 minuto: Solo 7 días
- Datos de 1 hora: Solo 730 días (2 años)
- Datos diarios: Sin límite (hasta 100+ años)

ESTRATEGIA ÓPTIMA:
1. Datos diarios de 20 años (máximo histórico)
2. Datos de 1 hora de los últimos 2 años
3. Datos de 1 minuto de los últimos 7 días

RESULTADO ESPERADO: 5-10 MILLONES DE REGISTROS
TIEMPO: 30-60 minutos
PESO ESTIMADO: 2-3 GB
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time
import os
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ============================================
# CONFIGURACIÓN
# ============================================

DATA_DIR = Path("data_historico")
DATA_DIR.mkdir(exist_ok=True)

print("="*70)
print("🚀 DESCARGA MASIVA MEJORADA - ESTRATEGIA MULTI-INTERVALO")
print("="*70)
print(f"📁 Guardando en: {DATA_DIR.absolute()}\n")

# ============================================
# LISTA COMPLETA DE ACTIVOS (80 activos)
# ============================================

ACTIVOS = {
    # METALES PRECIOSOS (5)
    'metales': {
        'GC=F': 'Oro Futuro',
        'SI=F': 'Plata Futuro',
        'PL=F': 'Platino',
        'PA=F': 'Paladio',
        'HG=F': 'Cobre'
    },
    
    # ÍNDICES PRINCIPALES (15)
    'indices': {
        '^GSPC': 'S&P 500',
        '^DJI': 'Dow Jones',
        '^IXIC': 'NASDAQ',
        '^RUT': 'Russell 2000',
        '^FTSE': 'FTSE 100',
        '^N225': 'Nikkei 225',
        '^HSI': 'Hang Seng',
        '^GDAXI': 'DAX',
        '^FCHI': 'CAC 40',
        '^IBEX': 'IBEX 35',
        '^MXX': 'IPC México',
        '^BVSP': 'Bovespa Brasil',
        '^MERV': 'Merval Argentina',
        '^AXJO': 'ASX 200 Australia',
        '^KS11': 'KOSPI Korea'
    },
    
    # DIVISAS (10)
    'divisas': {
        'EURUSD=X': 'EUR/USD',
        'GBPUSD=X': 'GBP/USD',
        'JPYUSD=X': 'JPY/USD',
        'AUDUSD=X': 'AUD/USD',
        'NZDUSD=X': 'NZD/USD',
        'CADUSD=X': 'CAD/USD',
        'CHFUSD=X': 'CHF/USD',
        'MXNUSD=X': 'MXN/USD',
        'CNYUSD=X': 'CNY/USD',
        'DX-Y.NYB': 'Índice Dólar DXY'
    },
    
    # CRIPTOMONEDAS (15)
    'cripto': {
        'BTC-USD': 'Bitcoin',
        'ETH-USD': 'Ethereum',
        'BNB-USD': 'Binance Coin',
        'XRP-USD': 'Ripple',
        'ADA-USD': 'Cardano',
        'SOL-USD': 'Solana',
        'DOGE-USD': 'Dogecoin',
        'DOT-USD': 'Polkadot',
        'MATIC-USD': 'Polygon',
        'LTC-USD': 'Litecoin',
        'AVAX-USD': 'Avalanche',
        'LINK-USD': 'Chainlink',
        'UNI-USD': 'Uniswap',
        'ATOM-USD': 'Cosmos',
        'XLM-USD': 'Stellar'
    },
    
    # ENERGÍA Y COMMODITIES (15)
    'energia': {
        'CL=F': 'Petróleo WTI',
        'BZ=F': 'Petróleo Brent',
        'NG=F': 'Gas Natural',
        'ZC=F': 'Maíz',
        'ZS=F': 'Soja',
        'ZW=F': 'Trigo',
        'KC=F': 'Café',
        'SB=F': 'Azúcar',
        'CT=F': 'Algodón',
        'CC=F': 'Cacao',
        'HO=F': 'Heating Oil',
        'RB=F': 'Gasolina',
        'LE=F': 'Ganado',
        'GF=F': 'Ganado Alimentado',
        'ZL=F': 'Aceite de Soja'
    },
    
    # ETFs IMPORTANTES (20)
    'etfs': {
        'GLD': 'SPDR Gold Shares',
        'SLV': 'iShares Silver Trust',
        'USO': 'US Oil Fund',
        'UNG': 'US Natural Gas Fund',
        'SPY': 'SPDR S&P 500 ETF',
        'QQQ': 'Invesco QQQ Trust',
        'DIA': 'SPDR Dow Jones ETF',
        'IWM': 'iShares Russell 2000',
        'TLT': '20+ Year Treasury Bond',
        'AGG': 'Core US Aggregate Bond',
        'EEM': 'Emerging Markets ETF',
        'VWO': 'Vanguard Emerging Markets',
        'XLE': 'Energy Select Sector',
        'XLF': 'Financial Select Sector',
        'XLK': 'Technology Select Sector',
        'XLV': 'Health Care Select',
        'XLP': 'Consumer Staples',
        'XLI': 'Industrial Select',
        'XLU': 'Utilities Select',
        'GDX': 'Gold Miners ETF'
    }
}

# ============================================
# FUNCIÓN DE DESCARGA INTELIGENTE
# ============================================

def descargar_activo(ticker, nombre, categoria):
    """Descarga un activo con múltiples intervalos"""
    registros_total = 0
    
    print(f"\n{'='*70}")
    print(f"📊 {nombre} ({ticker})")
    print(f"{'='*70}")
    
    # ESTRATEGIA 1: Datos DIARIOS - 20 años
    print(f"  📅 Descargando datos DIARIOS (20 años)...")
    try:
        df_diario = yf.download(
            ticker,
            period="20y",
            interval="1d",
            progress=False
        )
        
        if not df_diario.empty:
            if isinstance(df_diario.columns, pd.MultiIndex):
                df_diario.columns = df_diario.columns.get_level_values(0)
            
            filename = DATA_DIR / f"{ticker.replace('=', '_').replace('^', 'IDX_').replace('-', '_')}_20y_1d.parquet"
            df_diario.to_parquet(filename)
            
            registros = len(df_diario)
            registros_total += registros
            print(f"     ✅ {registros:,} registros diarios guardados")
        else:
            print(f"     ⚠️  Sin datos diarios")
    except Exception as e:
        print(f"     ❌ Error diarios: {str(e)[:50]}")
    
    time.sleep(0.5)
    
    # ESTRATEGIA 2: Datos HORARIOS - 730 días (límite de Yahoo)
    print(f"  ⏰ Descargando datos HORARIOS (730 días)...")
    try:
        df_horario = yf.download(
            ticker,
            period="730d",
            interval="1h",
            progress=False
        )
        
        if not df_horario.empty:
            if isinstance(df_horario.columns, pd.MultiIndex):
                df_horario.columns = df_horario.columns.get_level_values(0)
            
            filename = DATA_DIR / f"{ticker.replace('=', '_').replace('^', 'IDX_').replace('-', '_')}_730d_1h.parquet"
            df_horario.to_parquet(filename)
            
            registros = len(df_horario)
            registros_total += registros
            print(f"     ✅ {registros:,} registros horarios guardados")
        else:
            print(f"     ⚠️  Sin datos horarios")
    except Exception as e:
        print(f"     ❌ Error horarios: {str(e)[:50]}")
    
    time.sleep(0.5)
    
    # ESTRATEGIA 3: Datos de 5 MINUTOS - 60 días
    print(f"  🕐 Descargando datos de 5 MINUTOS (60 días)...")
    try:
        df_5min = yf.download(
            ticker,
            period="60d",
            interval="5m",
            progress=False
        )
        
        if not df_5min.empty:
            if isinstance(df_5min.columns, pd.MultiIndex):
                df_5min.columns = df_5min.columns.get_level_values(0)
            
            filename = DATA_DIR / f"{ticker.replace('=', '_').replace('^', 'IDX_').replace('-', '_')}_60d_5m.parquet"
            df_5min.to_parquet(filename)
            
            registros = len(df_5min)
            registros_total += registros
            print(f"     ✅ {registros:,} registros de 5min guardados")
        else:
            print(f"     ⚠️  Sin datos de 5min")
    except Exception as e:
        print(f"     ❌ Error 5min: {str(e)[:50]}")
    
    time.sleep(0.5)
    
    print(f"  🎯 Subtotal {nombre}: {registros_total:,} registros")
    
    return registros_total

# ============================================
# PROCESO DE DESCARGA
# ============================================

total_general = 0
resumen_por_categoria = {}

for categoria, activos in ACTIVOS.items():
    print(f"\n\n{'#'*70}")
    print(f"{'#'*70}")
    print(f"##  {categoria.upper()}")
    print(f"{'#'*70}")
    print(f"{'#'*70}\n")
    
    subtotal_categoria = 0
    
    for ticker, nombre in activos.items():
        registros = descargar_activo(ticker, nombre, categoria)
        subtotal_categoria += registros
        total_general += registros
    
    resumen_por_categoria[categoria] = subtotal_categoria
    
    print(f"\n{'='*70}")
    print(f"✅ TOTAL {categoria.upper()}: {subtotal_categoria:,} registros")
    print(f"{'='*70}")

# ============================================
# RESUMEN FINAL
# ============================================

print(f"\n\n{'='*70}")
print(f"{'='*70}")
print(f"🎉 DESCARGA COMPLETADA")
print(f"{'='*70}")
print(f"{'='*70}\n")

print(f"📊 RESUMEN POR CATEGORÍA:\n")
for categoria, total in resumen_por_categoria.items():
    emoji = {'metales': '💰', 'indices': '📈', 'divisas': '💱', 
             'cripto': '₿', 'energia': '⚡', 'etfs': '📦'}
    print(f"  {emoji.get(categoria, '📊')} {categoria.upper():20s}: {total:>15,} registros")

print(f"\n  {'='*50}")
print(f"  🎯 TOTAL GENERAL: {total_general:>23,} registros")
print(f"  {'='*50}\n")

# Calcular espacio
archivos = list(DATA_DIR.glob("*.parquet"))
tamano_total = sum(f.stat().st_size for f in archivos) / (1024**3)

print(f"💾 ESPACIO EN DISCO:")
print(f"  📁 Archivos creados: {len(archivos)}")
print(f"  💿 Tamaño total: {tamano_total:.2f} GB")
print(f"  📂 Ubicación: {DATA_DIR.absolute()}\n")

# Progreso hacia 20M
progreso = (total_general / 20_000_000) * 100
print(f"🎯 PROGRESO HACIA 20 MILLONES:")
print(f"  Actual: {total_general:,} registros ({progreso:.1f}%)")
print(f"  Meta:   20,000,000 registros")
print(f"  Faltan: {20_000_000 - total_general:,} registros\n")

# Estimación de peso por millón
peso_por_millon = (tamano_total / total_general) * 1_000_000 if total_general > 0 else 0
peso_20m = peso_por_millon * 20

print(f"📊 ESTIMACIÓN DE PESO:")
print(f"  Peso por 1M registros: {peso_por_millon:.2f} GB")
print(f"  Peso estimado de 20M: {peso_20m:.2f} GB")
print(f"  Espacio recomendado: {peso_20m * 1.5:.2f} GB (con margen)\n")

if total_general >= 1_000_000:
    print(f"  🎉 ¡HAS SUPERADO 1 MILLÓN DE REGISTROS!")
if total_general >= 5_000_000:
    print(f"  🎉 ¡HAS SUPERADO 5 MILLONES DE REGISTROS!")
if total_general >= 10_000_000:
    print(f"  🎉 ¡HAS SUPERADO 10 MILLONES DE REGISTROS!")
if total_general >= 20_000_000:
    print(f"  🎊 ¡FELICIDADES! ¡META DE 20M ALCANZADA!")

print(f"\n📝 PRÓXIMOS PASOS:")
print(f"  1. Ejecutar: python cargar_datos_dashboard.py")
print(f"  2. Ver resumen completo de datos")
print(f"  3. Integrar con dashboard: streamlit run dashboard_oro.py\n")

print(f"{'='*70}")
print(f"✅ PROCESO COMPLETADO EXITOSAMENTE")
print(f"{'='*70}\n")

# Guardar resumen JSON
import json
resumen_json = {
    'fecha_descarga': datetime.now().isoformat(),
    'total_registros': total_general,
    'total_archivos': len(archivos),
    'tamano_gb': round(tamano_total, 2),
    'resumen_categorias': resumen_por_categoria,
    'peso_por_millon_gb': round(peso_por_millon, 2),
    'estimacion_20m_gb': round(peso_20m, 2),
    'activos_descargados': sum(len(a) for a in ACTIVOS.values())
}

with open('resumen_descarga.json', 'w', encoding='utf-8') as f:
    json.dump(resumen_json, f, indent=2, ensure_ascii=False)

print(f"📄 Resumen guardado en: resumen_descarga.json")
