"""
Script para probar las APIs reales
Ejecutar: python test_apis.py
"""
import sys
import os

print("="*60)
print("PRUEBA DE APIs REALES - Sistema de Predicción del Oro")
print("="*60)

# 1. Verificar configuración
print("\n[1/4] Verificando configuración...")
try:
    from config import verificar_apis, API_KEYS
    apis_disponibles = verificar_apis()
    
    for api, estado in apis_disponibles.items():
        simbolo = "✅" if estado else "❌"
        print(f"  {simbolo} {api}: {'Configurada' if estado else 'No configurada'}")
    
    total_activas = sum(apis_disponibles.values())
    print(f"\n  Total APIs activas: {total_activas}/4")
    
except Exception as e:
    print(f"  ❌ Error: {e}")
    print("\n  SOLUCIÓN: Verifica que el archivo .env existe y tiene las claves correctas")
    sys.exit(1)

# 2. Probar NewsAPI
print("\n[2/4] Probando NewsAPI...")
if apis_disponibles['NewsAPI']:
    try:
        from apis.news_api import obtener_noticias_oro
        
        df_news = obtener_noticias_oro(dias=3, idioma='en')
        
        if not df_news.empty:
            print(f"  ✅ {len(df_news)} noticias obtenidas")
            print("\n  Últimas 3 noticias:")
            for idx, row in df_news.head(3).iterrows():
                print(f"    - [{row['fuente']}] {row['titulo'][:60]}...")
        else:
            print("  ⚠️ No se encontraron noticias (puede ser límite de API)")
    except Exception as e:
        print(f"  ❌ Error: {e}")
else:
    print("  ⏭️ Saltando (API no configurada)")

# 3. Probar Alpha Vantage
print("\n[3/4] Probando Alpha Vantage...")
if apis_disponibles['AlphaVantage']:
    try:
        from apis.alpha_vantage import obtener_sentimiento_noticias
        
        df_alpha = obtener_sentimiento_noticias('GOLD', limite=10)
        
        if not df_alpha.empty:
            print(f"  ✅ {len(df_alpha)} noticias con sentimiento obtenidas")
            sentimiento_prom = df_alpha['sentimiento'].mean()
            print(f"  📊 Sentimiento promedio: {sentimiento_prom:.3f}")
            print(f"  📈 Positivos: {(df_alpha['sentimiento_label'] == 'Bullish').sum()}")
            print(f"  📉 Negativos: {(df_alpha['sentimiento_label'] == 'Bearish').sum()}")
        else:
            print("  ⚠️ No se obtuvieron datos (puede ser límite de API)")
    except Exception as e:
        print(f"  ❌ Error: {e}")
else:
    print("  ⏭️ Saltando (API no configurada)")

# 4. Probar Analizador de Sentimiento
print("\n[4/4] Probando Analizador de Sentimiento...")
try:
    from apis.sentiment_analyzer import AnalizadorSentimiento
    
    analizador = AnalizadorSentimiento()
    
    # Textos de prueba
    textos_prueba = [
        "Gold prices soar to new record highs!",
        "Gold market crashes dramatically today",
        "Gold remains stable with minimal movement"
    ]
    
    print("  Analizando 3 textos de ejemplo...")
    for texto in textos_prueba:
        resultado = analizador.analizar_texto(texto)
        print(f"    {resultado['sentimiento_label']:8} ({resultado['sentimiento']:+.3f}): {texto[:40]}...")
    
    print("  ✅ Analizador funcionando correctamente")
    
except Exception as e:
    print(f"  ❌ Error: {e}")

# Resumen final
print("\n" + "="*60)
print("RESUMEN")
print("="*60)

if total_activas >= 2:
    print("✅ Sistema listo para funcionar con datos reales!")
    print("\nPróximos pasos:")
    print("  1. Instalar dependencias: pip install -r requirements_real.txt")
    print("  2. Ejecutar dashboard: streamlit run dashboard_oro.py")
    print("  3. El sistema usará datos REALES de las APIs configuradas")
else:
    print("⚠️ Necesitas al menos 2 APIs configuradas para funcionar")
    print("\nConfigura las APIs faltantes en el archivo .env")

print("="*60)
