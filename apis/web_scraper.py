"""
Módulo de Web Scraping para noticias económicas de Perú y el mundo
Sitios objetivo: La Gestión, La República, El Comercio, Kitco, Mining.com
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import warnings
warnings.filterwarnings('ignore')

class WebScraperNoticias:
    """Scraper de noticias sobre oro y economía"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.timeout = 10
    
    def scrape_gestion(self, max_noticias=20):
        """
        Scrapear noticias de La Gestión (Perú)
        URL: https://gestion.pe/noticias/oro/
        """
        noticias = []
        
        try:
            print("  📰 Scrapeando La Gestión...")
            
            # URLs de búsqueda
            urls = [
                'https://gestion.pe/noticias/oro/',
                'https://gestion.pe/noticias/precio-oro/',
                'https://gestion.pe/economia/'
            ]
            
            for url in urls[:1]:  # Por ahora solo 1 URL para no saturar
                try:
                    response = requests.get(url, headers=self.headers, timeout=self.timeout)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Buscar artículos (la estructura puede cambiar)
                    articulos = soup.find_all('div', class_='story-item', limit=max_noticias)
                    
                    if not articulos:
                        # Intentar otra estructura común
                        articulos = soup.find_all('article', limit=max_noticias)
                    
                    for articulo in articulos[:max_noticias]:
                        try:
                            # Extraer título
                            titulo_elem = articulo.find('h2') or articulo.find('h3') or articulo.find('a')
                            titulo = titulo_elem.get_text(strip=True) if titulo_elem else 'Sin título'
                            
                            # Extraer enlace
                            link_elem = articulo.find('a', href=True)
                            link = link_elem['href'] if link_elem else ''
                            if link and not link.startswith('http'):
                                link = f"https://gestion.pe{link}"
                            
                            # Extraer descripción
                            desc_elem = articulo.find('p')
                            descripcion = desc_elem.get_text(strip=True) if desc_elem else ''
                            
                            if titulo and len(titulo) > 10:
                                noticias.append({
                                    'fecha': datetime.now(),
                                    'titulo': titulo,
                                    'descripcion': descripcion,
                                    'texto': f"{titulo} {descripcion}",
                                    'fuente': 'La Gestión (Web Scraping)',
                                    'url': link,
                                    'pais': 'Perú'
                                })
                        except Exception as e:
                            continue
                    
                    time.sleep(1)  # Respetar el servidor
                    
                except Exception as e:
                    print(f"    ⚠️ Error en {url}: {str(e)[:50]}")
                    continue
            
            print(f"    ✅ {len(noticias)} noticias de La Gestión")
            
        except Exception as e:
            print(f"    ❌ Error general en La Gestión: {str(e)}")
        
        return noticias
    
    def scrape_larepublica(self, max_noticias=20):
        """
        Scrapear noticias de La República (Perú)
        URL: https://larepublica.pe/economia/
        """
        noticias = []
        
        try:
            print("  📰 Scrapeando La República...")
            
            urls = [
                'https://larepublica.pe/economia/',
                'https://larepublica.pe/tag/oro/'
            ]
            
            for url in urls[:1]:
                try:
                    response = requests.get(url, headers=self.headers, timeout=self.timeout)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Buscar artículos
                    articulos = soup.find_all('article', limit=max_noticias)
                    
                    if not articulos:
                        articulos = soup.find_all('div', class_='news-item', limit=max_noticias)
                    
                    for articulo in articulos[:max_noticias]:
                        try:
                            titulo_elem = articulo.find('h2') or articulo.find('h3') or articulo.find('a')
                            titulo = titulo_elem.get_text(strip=True) if titulo_elem else ''
                            
                            link_elem = articulo.find('a', href=True)
                            link = link_elem['href'] if link_elem else ''
                            if link and not link.startswith('http'):
                                link = f"https://larepublica.pe{link}"
                            
                            desc_elem = articulo.find('p')
                            descripcion = desc_elem.get_text(strip=True) if desc_elem else ''
                            
                            if titulo and len(titulo) > 10:
                                noticias.append({
                                    'fecha': datetime.now(),
                                    'titulo': titulo,
                                    'descripcion': descripcion,
                                    'texto': f"{titulo} {descripcion}",
                                    'fuente': 'La República (Web Scraping)',
                                    'url': link,
                                    'pais': 'Perú'
                                })
                        except:
                            continue
                    
                    time.sleep(1)
                    
                except Exception as e:
                    print(f"    ⚠️ Error en {url}: {str(e)[:50]}")
                    continue
            
            print(f"    ✅ {len(noticias)} noticias de La República")
            
        except Exception as e:
            print(f"    ❌ Error general en La República: {str(e)}")
        
        return noticias
    
    def scrape_elcomercio(self, max_noticias=20):
        """
        Scrapear noticias de El Comercio (Perú)
        URL: https://elcomercio.pe/economia/
        """
        noticias = []
        
        try:
            print("  📰 Scrapeando El Comercio...")
            
            url = 'https://elcomercio.pe/economia/'
            
            try:
                response = requests.get(url, headers=self.headers, timeout=self.timeout)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                articulos = soup.find_all('article', limit=max_noticias)
                
                for articulo in articulos[:max_noticias]:
                    try:
                        titulo_elem = articulo.find('h2') or articulo.find('h3') or articulo.find('a')
                        titulo = titulo_elem.get_text(strip=True) if titulo_elem else ''
                        
                        link_elem = articulo.find('a', href=True)
                        link = link_elem['href'] if link_elem else ''
                        if link and not link.startswith('http'):
                            link = f"https://elcomercio.pe{link}"
                        
                        if titulo and len(titulo) > 10:
                            noticias.append({
                                'fecha': datetime.now(),
                                'titulo': titulo,
                                'descripcion': '',
                                'texto': titulo,
                                'fuente': 'El Comercio (Web Scraping)',
                                'url': link,
                                'pais': 'Perú'
                            })
                    except:
                        continue
                
                time.sleep(1)
                
            except Exception as e:
                print(f"    ⚠️ Error: {str(e)[:50]}")
            
            print(f"    ✅ {len(noticias)} noticias de El Comercio")
            
        except Exception as e:
            print(f"    ❌ Error general en El Comercio: {str(e)}")
        
        return noticias
    
    def scrape_kitco(self, max_noticias=15):
        """
        Scrapear Kitco.com - Líder mundial en noticias de oro
        URL: https://www.kitco.com/news/gold.html
        """
        noticias = []
        
        try:
            print("  📰 Scrapeando Kitco (Gold News)...")
            
            url = 'https://www.kitco.com/news/gold.html'
            
            try:
                response = requests.get(url, headers=self.headers, timeout=self.timeout)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Kitco tiene una estructura específica
                articulos = soup.find_all('div', class_='article', limit=max_noticias)
                
                if not articulos:
                    articulos = soup.find_all('article', limit=max_noticias)
                
                for articulo in articulos[:max_noticias]:
                    try:
                        titulo_elem = articulo.find('h3') or articulo.find('h2') or articulo.find('a')
                        titulo = titulo_elem.get_text(strip=True) if titulo_elem else ''
                        
                        link_elem = articulo.find('a', href=True)
                        link = link_elem['href'] if link_elem else ''
                        if link and not link.startswith('http'):
                            link = f"https://www.kitco.com{link}"
                        
                        desc_elem = articulo.find('p')
                        descripcion = desc_elem.get_text(strip=True) if desc_elem else ''
                        
                        if titulo and len(titulo) > 10:
                            noticias.append({
                                'fecha': datetime.now(),
                                'titulo': titulo,
                                'descripcion': descripcion,
                                'texto': f"{titulo} {descripcion}",
                                'fuente': 'Kitco (Web Scraping)',
                                'url': link,
                                'pais': 'Internacional'
                            })
                    except:
                        continue
                
                time.sleep(1)
                
            except Exception as e:
                print(f"    ⚠️ Error: {str(e)[:50]}")
            
            print(f"    ✅ {len(noticias)} noticias de Kitco")
            
        except Exception as e:
            print(f"    ❌ Error general en Kitco: {str(e)}")
        
        return noticias
    
    def scrape_mining(self, max_noticias=15):
        """
        Scrapear Mining.com - Noticias de minería y oro
        URL: https://www.mining.com/category/gold/
        """
        noticias = []
        
        try:
            print("  📰 Scrapeando Mining.com...")
            
            url = 'https://www.mining.com/tag/gold/'
            
            try:
                response = requests.get(url, headers=self.headers, timeout=self.timeout)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                articulos = soup.find_all('article', limit=max_noticias)
                
                for articulo in articulos[:max_noticias]:
                    try:
                        titulo_elem = articulo.find('h3') or articulo.find('h2')
                        titulo = titulo_elem.get_text(strip=True) if titulo_elem else ''
                        
                        link_elem = articulo.find('a', href=True)
                        link = link_elem['href'] if link_elem else ''
                        
                        if titulo and len(titulo) > 10:
                            noticias.append({
                                'fecha': datetime.now(),
                                'titulo': titulo,
                                'descripcion': '',
                                'texto': titulo,
                                'fuente': 'Mining.com (Web Scraping)',
                                'url': link,
                                'pais': 'Internacional'
                            })
                    except:
                        continue
                
                time.sleep(1)
                
            except Exception as e:
                print(f"    ⚠️ Error: {str(e)[:50]}")
            
            print(f"    ✅ {len(noticias)} noticias de Mining.com")
            
        except Exception as e:
            print(f"    ❌ Error general en Mining.com: {str(e)}")
        
        return noticias
    
    def scrape_todas_las_fuentes(self, max_por_fuente=15):
        """
        Scrapear todas las fuentes disponibles
        
        Returns:
            DataFrame con todas las noticias scrapeadas
        """
        print("\n🌐 Iniciando Web Scraping de múltiples fuentes...\n")
        
        todas_noticias = []
        
        # Scrapear cada fuente
        todas_noticias.extend(self.scrape_gestion(max_por_fuente))
        todas_noticias.extend(self.scrape_larepublica(max_por_fuente))
        todas_noticias.extend(self.scrape_elcomercio(max_por_fuente))
        todas_noticias.extend(self.scrape_kitco(max_por_fuente))
        todas_noticias.extend(self.scrape_mining(max_por_fuente))
        
        df = pd.DataFrame(todas_noticias)
        
        if not df.empty:
            # Eliminar duplicados por título
            df = df.drop_duplicates(subset=['titulo'], keep='first')
            print(f"\n✅ Total: {len(df)} noticias únicas scrapeadas")
            print(f"\nDistribución por fuente:")
            print(df['fuente'].value_counts())
        else:
            print("\n⚠️ No se obtuvieron noticias del web scraping")
        
        return df

def obtener_noticias_scraping(max_por_fuente=15):
    """
    Función simple para obtener noticias via web scraping
    Compatible con la estructura del dashboard
    """
    scraper = WebScraperNoticias()
    return scraper.scrape_todas_las_fuentes(max_por_fuente)

if __name__ == '__main__':
    print("="*60)
    print("PRUEBA DE WEB SCRAPING - Noticias de Oro y Economía")
    print("="*60)
    
    scraper = WebScraperNoticias()
    df_noticias = scraper.scrape_todas_las_fuentes(max_por_fuente=10)
    
    if not df_noticias.empty:
        print("\n" + "="*60)
        print("MUESTRA DE NOTICIAS SCRAPEADAS")
        print("="*60)
        print("\nPrimeras 5 noticias:")
        for idx, row in df_noticias.head(5).iterrows():
            print(f"\n{idx+1}. [{row['fuente']}]")
            print(f"   {row['titulo'][:80]}...")
            if row['url']:
                print(f"   URL: {row['url'][:60]}...")
        
        print(f"\n{'='*60}")
        print(f"✅ Web scraping completado: {len(df_noticias)} noticias")
        print(f"{'='*60}")
    else:
        print("\n❌ No se obtuvieron noticias")
