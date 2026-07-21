import time
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
import google.generativeai as genai
import re

def internette_kod_arastir(sorgu):
    """Geliştirilecek özellik için internetten Python kütüphaneleri ve yöntemleri araştırır."""
    sonuclar = []
    try:
        with DDGS() as ddgs:
            for sonuc in ddgs.text(sorgu + " python example code", max_results=3):
                url = sonuc.get('href', '')
                if url:
                    try:
                        headers = {'User-Agent': 'Mozilla/5.0'}
                        yanit = requests.get(url, headers=headers, timeout=5)
                        if yanit.status_code == 200:
                            soup = BeautifulSoup(yanit.text, 'html.parser')
                            metin = " ".join([p.get_text() for p in soup.find_all(['p', 'pre', 'code'])])
                            sonuclar.append(metin[:1500])
                    except:
                        pass
    except:
        pass
    return "\n".join(sonuclar)

def yeni_yetenek_yaz(api_key, konu, mevcut_kod):
    """İnternetten öğrendikleriyle kendi koduna yeni bir fonksiyon ekler."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    arastirma_verisi = internette_kod_arastir(konu)
    
    prompt = f"""
    Sen otonom kendini kodlayan bir yapay zekasın. 
    Kullanıcı senden şu yeni yeteneği eklemeni istedi: '{konu}'
    
    İnternetten yaptığın araştırma verisi:
    {arastirma_verisi}
    
    Mevcut Yetenekler Dosyasının Kodu:
    ```python
    {mevcut_kod}
    ```
    
    GÖREVİN: 
    Mevcut koda, kullanıcının istediği bu yeni özelliği/fonksiyonu entegre et. 
    Streamlit (st) ile ekranda gösterilecek şekilde bir arayüz fonksiyonu yaz.
    Bana SADECE ve SADECE güncellenmiş tam Python kodunu ver. Asla açıklama yapma.
    """
    
    yanit = model.generate_content(prompt)
    yeni_kod = yanit.text
    
    # Fazlalık markdown işaretlerini temizle
    yeni_kod = yeni_kod.replace("```python", "").replace("```", "").strip()
    return yeni_kod
