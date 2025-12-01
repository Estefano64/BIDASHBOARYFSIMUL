"""
🚀 SCRIPT PARA LLEGAR A 20 MILLONES DE DATOS
==============================================

Este script descarga datos históricos masivos de múltiples fuentes
para alcanzar el objetivo de 20M+ registros.

TIEMPO ESTIMADO: 2-4 horas
ESPACIO EN DISCO: ~5 GB
COSTO: $0 (100% GRATIS)

Ejecutar: python descargar_historico_masivo.py
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

# Crear carpeta para datos
DATA_DIR = Path("data_historico")
DATA_DIR.mkdir(exist_ok=True)

print("="*60)
print("🚀 DESCARGA MASIVA DE DATOS HISTÓRICOS")
print("="*60)
print(f"📁 Guardando en: {DATA_DIR.absolute()}\n")

# ============================================
# 1. METALES PRECIOSOS (Principal)
# ============================================

print("\n" + "="*60)
print("💰 PASO 1: METALES PRECIOSOS")
print("="*60)

metales = {
    'GC=F': 'Oro',
    'SI=F': 'Plata',
    'PL=F': 'Platino',
    'PA=F': 'Paladio',
    'HG=F': 'Cobre'
}

total_registros = 0

for ticker, nombre in metales.items():
    print(f"\n📊 Descargando {nombre} ({ticker})...")
    
    try:
        # Descargar 10 años de datos por hora (máximo detalle disponible)
        # 10 años × 365 días × 24 horas = ~87,600 registros por metal
        df = yf.download(
            ticker,
            period="10y",
            interval="1h",  # Cada hora
            progress=False
        )
        
        if not df.empty:
            # Aplanar MultiIndex si existe
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            
            filename = DATA_DIR / f"{ticker.replace('=', '_')}_10años_1h.parquet"
            df.to_parquet(filename)
            
            registros = len(df)
            total_registros += registros
            print(f"  ✅ {nombre}: {registros:,} registros guardados")
            print(f"  📁 {filename}")
        
        time.sleep(1)  # Pausa para no saturar la API
        
    except Exception as e:
        print(f"  ❌ Error con {nombre}: {str(e)}")

print(f"\n💰 Subtotal Metales: {total_registros:,} registros")

# ============================================
# 2. ÍNDICES BURSÁTILES
# ============================================

print("\n" + "="*60)
print("📈 PASO 2: ÍNDICES BURSÁTILES")
print("="*60)

indices = {
    '^GSPC': 'S&P 500',
    '^DJI': 'Dow Jones',
    '^IXIC': 'NASDAQ',
    '^RUT': 'Russell 2000',
    '^FTSE': 'FTSE 100',
    '^N225': 'Nikkei 225',
    '^HSI': 'Hang Seng',
    '^GDAXI': 'DAX',
    '^FCHI': 'CAC 40',
    '^IBEX': 'IBEX 35'
}

subtotal_indices = 0

for ticker, nombre in indices.items():
    print(f"\n📊 Descargando {nombre} ({ticker})...")
    
    try:
        df = yf.download(
            ticker,
            period="10y",
            interval="1h",
            progress=False
        )
        
        if not df.empty:
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            
            filename = DATA_DIR / f"{ticker.replace('^', 'IDX_')}_10años_1h.parquet"
            df.to_parquet(filename)
            
            registros = len(df)
            subtotal_indices += registros
            total_registros += registros
            print(f"  ✅ {nombre}: {registros:,} registros")
        
        time.sleep(1)
        
    except Exception as e:
        print(f"  ❌ Error con {nombre}: {str(e)}")

print(f"\n📈 Subtotal Índices: {subtotal_indices:,} registros")

# ============================================
# 3. DIVISAS (FOREX)
# ============================================

print("\n" + "="*60)
print("💱 PASO 3: DIVISAS (FOREX)")
print("="*60)

divisas = {
    'DX-Y.NYB': 'Índice Dólar (DXY)',
    'EURUSD=X': 'EUR/USD',
    'GBPUSD=X': 'GBP/USD',
    'JPYUSD=X': 'JPY/USD',
    'AUDUSD=X': 'AUD/USD',
    'NZDUSD=X': 'NZD/USD',
    'CADUSD=X': 'CAD/USD',
    'CHFUSD=X': 'CHF/USD'
}

subtotal_divisas = 0

for ticker, nombre in divisas.items():
    print(f"\n📊 Descargando {nombre} ({ticker})...")
    
    try:
        df = yf.download(
            ticker,
            period="10y",
            interval="1h",
            progress=False
        )
        
        if not df.empty:
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            
            filename = DATA_DIR / f"{ticker.replace('=', '_').replace('-', '_')}_10años_1h.parquet"
            df.to_parquet(filename)
            
            registros = len(df)
            subtotal_divisas += registros
            total_registros += registros
            print(f"  ✅ {nombre}: {registros:,} registros")
        
        time.sleep(1)
        
    except Exception as e:
        print(f"  ❌ Error con {nombre}: {str(e)}")

print(f"\n💱 Subtotal Divisas: {subtotal_divisas:,} registros")

# ============================================
# 4. CRIPTOMONEDAS
# ============================================

print("\n" + "="*60)
print("₿ PASO 4: CRIPTOMONEDAS")
print("="*60)

criptos = {
    'BTC-USD': 'Bitcoin',
    'ETH-USD': 'Ethereum',
    'BNB-USD': 'Binance Coin',
    'XRP-USD': 'Ripple',
    'ADA-USD': 'Cardano',
    'SOL-USD': 'Solana',
    'DOGE-USD': 'Dogecoin',
    'DOT-USD': 'Polkadot',
    'MATIC-USD': 'Polygon',
    'LTC-USD': 'Litecoin'
}

subtotal_criptos = 0

for ticker, nombre in criptos.items():
    print(f"\n📊 Descargando {nombre} ({ticker})...")
    
    try:
        # Cripto tiene datos 24/7, más registros
        df = yf.download(
            ticker,
            period="5y",  # 5 años (muchas cripto no tienen más)
            interval="1h",
            progress=False
        )
        
        if not df.empty:
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            
            filename = DATA_DIR / f"{ticker.replace('-', '_')}_5años_1h.parquet"
            df.to_parquet(filename)
            
            registros = len(df)
            subtotal_criptos += registros
            total_registros += registros
            print(f"  ✅ {nombre}: {registros:,} registros")
        
        time.sleep(1)
        
    except Exception as e:
        print(f"  ❌ Error con {nombre}: {str(e)}")

print(f"\n₿ Subtotal Criptomonedas: {subtotal_criptos:,} registros")

# ============================================
# 5. ENERGÍA Y COMMODITIES
# ============================================

print("\n" + "="*60)
print("⚡ PASO 5: ENERGÍA Y COMMODITIES")
print("="*60)

energia = {
    'CL=F': 'Petróleo WTI',
    'BZ=F': 'Petróleo Brent',
    'NG=F': 'Gas Natural',
    'ZC=F': 'Maíz',
    'ZS=F': 'Soja',
    'ZW=F': 'Trigo',
    'KC=F': 'Café',
    'SB=F': 'Azúcar',
    'CT=F': 'Algodón',
    'CC=F': 'Cacao'
}

subtotal_energia = 0

for ticker, nombre in energia.items():
    print(f"\n📊 Descargando {nombre} ({ticker})...")
    
    try:
        df = yf.download(
            ticker,
            period="10y",
            interval="1h",
            progress=False
        )
        
        if not df.empty:
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            
            filename = DATA_DIR / f"{ticker.replace('=', '_')}_10años_1h.parquet"
            df.to_parquet(filename)
            
            registros = len(df)
            subtotal_energia += registros
            total_registros += registros
            print(f"  ✅ {nombre}: {registros:,} registros")
        
        time.sleep(1)
        
    except Exception as e:
        print(f"  ❌ Error con {nombre}: {str(e)}")

print(f"\n⚡ Subtotal Energía: {subtotal_energia:,} registros")

# ============================================
# 6. ETFs IMPORTANTES
# ============================================

print("\n" + "="*60)
print("📦 PASO 6: ETFs (Exchange Traded Funds)")
print("="*60)

etfs = {
    'GLD': 'SPDR Gold Shares',
    'SLV': 'iShares Silver Trust',
    'USO': 'Oil ETF',
    'UNG': 'Gas ETF',
    'SPY': 'S&P 500 ETF',
    'QQQ': 'NASDAQ ETF',
    'DIA': 'Dow Jones ETF',
    'IWM': 'Russell 2000 ETF',
    'TLT': 'Treasury Bond ETF',
    'VXX': 'Volatility ETF'
}

subtotal_etfs = 0

for ticker, nombre in etfs.items():
    print(f"\n📊 Descargando {nombre} ({ticker})...")
    
    try:
        df = yf.download(
            ticker,
            period="10y",
            interval="1h",
            progress=False
        )
        
        if not df.empty:
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            
            filename = DATA_DIR / f"{ticker}_10años_1h.parquet"
            df.to_parquet(filename)
            
            registros = len(df)
            subtotal_etfs += registros
            total_registros += registros
            print(f"  ✅ {nombre}: {registros:,} registros")
        
        time.sleep(1)
        
    except Exception as e:
        print(f"  ❌ Error con {nombre}: {str(e)}")

print(f"\n📦 Subtotal ETFs: {subtotal_etfs:,} registros")

# ============================================
# RESUMEN FINAL
# ============================================

print("\n" + "="*60)
print("🎉 DESCARGA COMPLETADA")
print("="*60)

print(f"\n📊 DESGLOSE POR CATEGORÍA:")
print(f"  💰 Metales Preciosos:    {total_registros - subtotal_indices - subtotal_divisas - subtotal_criptos - subtotal_energia - subtotal_etfs:>12,} registros")
print(f"  📈 Índices Bursátiles:   {subtotal_indices:>12,} registros")
print(f"  💱 Divisas (Forex):      {subtotal_divisas:>12,} registros")
print(f"  ₿  Criptomonedas:        {subtotal_criptos:>12,} registros")
print(f"  ⚡ Energía/Commodities:  {subtotal_energia:>12,} registros")
print(f"  📦 ETFs:                 {subtotal_etfs:>12,} registros")
print(f"  " + "-"*40)
print(f"  🎯 TOTAL:                {total_registros:>12,} registros")

# Calcular espacio en disco
archivos = list(DATA_DIR.glob("*.parquet"))
tamano_total = sum(f.stat().st_size for f in archivos) / (1024**3)  # GB

print(f"\n💾 ESPACIO EN DISCO:")
print(f"  📁 Archivos creados: {len(archivos)}")
print(f"  💿 Tamaño total: {tamano_total:.2f} GB")
print(f"  📂 Ubicación: {DATA_DIR.absolute()}")

# Estimación para llegar a 20M
print(f"\n🎯 PROGRESO HACIA 20 MILLONES:")
progreso = (total_registros / 20_000_000) * 100
print(f"  Actual: {total_registros:,} registros ({progreso:.1f}%)")
print(f"  Meta:   20,000,000 registros")
print(f"  Faltan: {20_000_000 - total_registros:,} registros")

if total_registros >= 1_000_000:
    print(f"\n  ✅ ¡HAS SUPERADO 1 MILLÓN DE REGISTROS!")
if total_registros >= 5_000_000:
    print(f"  ✅ ¡HAS SUPERADO 5 MILLONES DE REGISTROS!")
if total_registros >= 10_000_000:
    print(f"  ✅ ¡HAS SUPERADO 10 MILLONES DE REGISTROS!")
if total_registros >= 20_000_000:
    print(f"  🎉 ¡FELICIDADES! ¡HAS ALCANZADO 20 MILLONES!")

print("\n📝 PRÓXIMOS PASOS:")
print("  1. Ejecutar: python cargar_datos_dashboard.py")
print("  2. Los datos se cargarán automáticamente en el dashboard")
print("  3. Ver análisis en: http://localhost:8503")

print("\n" + "="*60)
print("✅ PROCESO COMPLETADO EXITOSAMENTE")
print("="*60)
