"""
Módulo para análisis de sentimiento real usando VADER y TextBlob
"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import pandas as pd
import numpy as np

class AnalizadorSentimiento:
    """Analiza sentimiento de textos usando VADER y TextBlob"""
    
    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()
    
    def analizar_texto(self, texto):
        """
        Analizar sentimiento de un texto individual
        
        Returns:
            dict con scores de sentimiento
        """
        if not texto or pd.isna(texto) or len(str(texto).strip()) < 3:
            return {
                'sentimiento': 0.0,
                'vader_compound': 0.0,
                'vader_pos': 0.0,
                'vader_neg': 0.0,
                'vader_neu': 1.0,
                'textblob_polarity': 0.0,
                'textblob_subjectivity': 0.0,
                'sentimiento_label': 'Neutral'
            }
        
        texto_str = str(texto)
        
        # VADER (mejor para redes sociales, maneja emojis y slang)
        vader_scores = self.vader.polarity_scores(texto_str)
        
        # TextBlob (mejor para noticias formales)
        try:
            blob = TextBlob(texto_str)
            textblob_polarity = blob.sentiment.polarity
            textblob_subjectivity = blob.sentiment.subjectivity
        except:
            textblob_polarity = 0.0
            textblob_subjectivity = 0.0
        
        # Combinar ambos métodos (promedio ponderado)
        # VADER compound va de -1 a 1
        # TextBlob polarity va de -1 a 1
        sentimiento_final = (vader_scores['compound'] * 0.6 + textblob_polarity * 0.4)
        
        # Clasificar
        if sentimiento_final >= 0.05:
            label = 'Positivo'
        elif sentimiento_final <= -0.05:
            label = 'Negativo'
        else:
            label = 'Neutral'
        
        return {
            'sentimiento': float(sentimiento_final),
            'vader_compound': float(vader_scores['compound']),
            'vader_pos': float(vader_scores['pos']),
            'vader_neg': float(vader_scores['neg']),
            'vader_neu': float(vader_scores['neu']),
            'textblob_polarity': float(textblob_polarity),
            'textblob_subjectivity': float(textblob_subjectivity),
            'sentimiento_label': label
        }
    
    def analizar_dataframe(self, df, columna_texto='texto'):
        """
        Analizar sentimiento de todo un DataFrame
        
        Args:
            df: DataFrame con textos
            columna_texto: Nombre de la columna con el texto
        
        Returns:
            DataFrame original con columnas de sentimiento agregadas
        """
        if df.empty or columna_texto not in df.columns:
            return df
        
        print(f"Analizando sentimiento de {len(df)} textos...")
        
        resultados = []
        for idx, texto in enumerate(df[columna_texto]):
            resultado = self.analizar_texto(texto)
            resultados.append(resultado)
            
            # Mostrar progreso cada 10 textos
            if (idx + 1) % 10 == 0:
                print(f"  Progreso: {idx + 1}/{len(df)}")
        
        # Convertir a DataFrame y combinar
        df_sentiment = pd.DataFrame(resultados)
        df_resultado = pd.concat([df.reset_index(drop=True), df_sentiment], axis=1)
        
        print(f"✅ Análisis completado")
        print(f"  Positivos: {(df_resultado['sentimiento_label'] == 'Positivo').sum()}")
        print(f"  Negativos: {(df_resultado['sentimiento_label'] == 'Negativo').sum()}")
        print(f"  Neutrales: {(df_resultado['sentimiento_label'] == 'Neutral').sum()}")
        print(f"  Sentimiento promedio: {df_resultado['sentimiento'].mean():.3f}")
        
        return df_resultado
    
    def obtener_estadisticas(self, df):
        """Obtener estadísticas de sentimiento de un DataFrame"""
        if 'sentimiento' not in df.columns:
            return {}
        
        stats = {
            'sentimiento_promedio': float(df['sentimiento'].mean()),
            'sentimiento_mediana': float(df['sentimiento'].median()),
            'sentimiento_std': float(df['sentimiento'].std()),
            'total_positivos': int((df['sentimiento_label'] == 'Positivo').sum()),
            'total_negativos': int((df['sentimiento_label'] == 'Negativo').sum()),
            'total_neutrales': int((df['sentimiento_label'] == 'Neutral').sum()),
            'porcentaje_positivos': float((df['sentimiento_label'] == 'Positivo').sum() / len(df) * 100),
            'porcentaje_negativos': float((df['sentimiento_label'] == 'Negativo').sum() / len(df) * 100),
            'sentimiento_max': float(df['sentimiento'].max()),
            'sentimiento_min': float(df['sentimiento'].min())
        }
        
        return stats

if __name__ == '__main__':
    # Prueba
    print("Probando Analizador de Sentimiento...\n")
    
    analizador = AnalizadorSentimiento()
    
    # Textos de prueba
    textos = [
        "Gold prices surge to record highs! Great news for investors!",
        "Gold market crashes, investors lose millions in worst day ever",
        "Gold prices remain stable today with minimal changes",
        "🚀📈 GOLD TO THE MOON! Best investment ever! 💰💎",
        "Terrible losses in gold market 😢 Very bad news"
    ]
    
    print("Análisis individual de textos:\n")
    for texto in textos:
        resultado = analizador.analizar_texto(texto)
        print(f"Texto: {texto[:50]}...")
        print(f"  Sentimiento: {resultado['sentimiento']:.3f} ({resultado['sentimiento_label']})")
        print(f"  VADER: {resultado['vader_compound']:.3f} | TextBlob: {resultado['textblob_polarity']:.3f}\n")
    
    # Prueba con DataFrame
    print("\nPrueba con DataFrame:")
    df_test = pd.DataFrame({'texto': textos})
    df_resultado = analizador.analizar_dataframe(df_test)
    print("\nResultados:")
    print(df_resultado[['texto', 'sentimiento', 'sentimiento_label']])
