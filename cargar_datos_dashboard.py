"""
📊 CARGADOR DE DATOS HISTÓRICOS MASIVOS PARA DASHBOARD
========================================================

Este script carga los datos descargados y los integra con el dashboard.

Ejecutar DESPUÉS de: python descargar_historico_masivo.py
"""

import pandas as pd
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

DATA_DIR = Path("data_historico")

print("="*60)
print("📊 CARGANDO DATOS HISTÓRICOS MASIVOS")
print("="*60)

# Buscar todos los archivos parquet
archivos = list(DATA_DIR.glob("*.parquet"))

if not archivos:
    print("❌ No se encontraron archivos. Ejecuta primero:")
    print("   python descargar_historico_masivo.py")
    exit(1)

print(f"\n📁 Encontrados {len(archivos)} archivos\n")

# Cargar y combinar datos
datos_combinados = {}
total_registros = 0

for archivo in archivos:
    nombre = archivo.stem
    print(f"📂 Cargando {nombre}...")
    
    try:
        df = pd.read_parquet(archivo)
        datos_combinados[nombre] = df
        registros = len(df)
        total_registros += registros
        print(f"   ✅ {registros:,} registros cargados")
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")

print(f"\n🎯 TOTAL: {total_registros:,} registros en memoria")

# Crear resumen estadístico
print("\n" + "="*60)
print("📈 RESUMEN ESTADÍSTICO")
print("="*60)

# Top 5 activos con más datos
top_5 = sorted(
    [(k, len(v)) for k, v in datos_combinados.items()],
    key=lambda x: x[1],
    reverse=True
)[:5]

print("\n🏆 Top 5 activos con más datos:")
for i, (nombre, cantidad) in enumerate(top_5, 1):
    print(f"  {i}. {nombre}: {cantidad:,} registros")

# Rango de fechas
print("\n📅 Rango de fechas:")
fechas_min = []
fechas_max = []

for nombre, df in datos_combinados.items():
    if not df.empty and hasattr(df.index, 'min'):
        fechas_min.append(df.index.min())
        fechas_max.append(df.index.max())

if fechas_min and fechas_max:
    print(f"  Desde: {min(fechas_min)}")
    print(f"  Hasta: {max(fechas_max)}")
    diferencia = max(fechas_max) - min(fechas_min)
    print(f"  Período: {diferencia.days} días ({diferencia.days/365:.1f} años)")

# Guardar resumen
resumen = {
    'total_archivos': len(archivos),
    'total_registros': total_registros,
    'activos': list(datos_combinados.keys()),
    'top_5': dict(top_5)
}

import json
with open('resumen_datos_historicos.json', 'w', encoding='utf-8') as f:
    json.dump(resumen, f, indent=2, default=str)

print("\n✅ Resumen guardado en: resumen_datos_historicos.json")

# Instrucciones para usar en dashboard
print("\n" + "="*60)
print("🚀 CÓMO USAR ESTOS DATOS EN EL DASHBOARD")
print("="*60)

print("""
1. Los datos están en: data_historico/*.parquet

2. Para cargar en tu dashboard, agrega esto al inicio de dashboard_oro.py:

   from pathlib import Path
   
   def cargar_datos_masivos():
       DATA_DIR = Path("data_historico")
       datos = {}
       for archivo in DATA_DIR.glob("*.parquet"):
           datos[archivo.stem] = pd.read_parquet(archivo)
       return datos
   
   # Usar así:
   datos_masivos = cargar_datos_masivos()

3. Mostrar en el dashboard:
   
   st.sidebar.metric("Total de Datos", f"{len(datos_masivos):,} activos")
   st.sidebar.metric("Registros Totales", f"{total_registros:,}")

4. Para análisis específico:
   
   df_oro = datos_masivos['GC_F_10años_1h']
   df_bitcoin = datos_masivos['BTC_USD_5años_1h']
   etc.
""")

print("="*60)
print("✅ DATOS LISTOS PARA USAR")
print("="*60)
