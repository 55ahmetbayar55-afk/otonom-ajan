import os
import json
import time
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
import google.generativeai as genai

def internette_kod_arastir(sorgu):
    """Geliştirilecek özellik için internetten en güncel bilgileri araştırır."""
    sonuclar = []
    try:
        with DDGS() as ddgs:
            for sonuc in ddgs.text(sorgu + " python latest documentation code example", max_results=3):
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

def hafizayi_oku():
    """Ajanın kalıcı JSON hafızasını okur ve prompt için hazırlar."""
    hafiza_dosyasi = "ajan_hafizasi.json"
    if os.path.exists(hafiza_dosyasi):
        try:
            with open(hafiza_dosyasi, "r", encoding="utf-8") as f:
                hafiza = json.load(f)
                
                kurallar = "\n".join([f"- {k}" for k in hafiza.get("genel_kurallar", [])])
                stratejiler = "\n".join([f"- {s}" for s in hafiza.get("ogrenilen_stratejiler", [])])
                
                hafiza_metni = f"""
                🚨 KALICI HAFIZA DEVREDE (BUNLARA KESİNLİKLE UY):
                Senin kalıcı hafızana kullanıcı tarafından şu kurallar kazındı:
                
                KULLANICI KURALLARI:
                {kurallar if kurallar else "- Henüz genel kural eklenmemiş."}
                
                ÖĞRENİLEN STRATEJİLER:
                {stratejiler if stratejiler else "- Henüz strateji eklenmemiş."}
                """
                return hafiza_metni
        except Exception as e:
            return f"Hafıza okuma hatası: {e}"
    return "🚨 KALICI HAFIZA DEVREDE: Henüz hafızada kayıtlı bir kural yok."

def yeni_yetenek_yaz(api_key, konu, mevcut_kod):
    """Kalıcı hafızayı ve interneti kullanarak yeni özellik yazar."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # 1. İnternetten araştırma yap
    arastirma_verisi = internette_kod_arastir(konu)
    
    # 2. Kalıcı hafızayı (json dosyasını) oku
    kalici_hafiza_kurallari = hafizayi_oku()
    
    prompt = f"""
    Sen kendini geliştirebilen otonom bir Yapay Zeka Ajanısın.
    Aşağıdaki kalıcı hafıza kurallarına ve internet araştırma verisine dayanarak, sistemin 'yetenekler.py' dosyasını güncellemelisin.
    
    {kalici_hafiza_kurallari}
    
    Kullanıcının Yeni İsteyi: '{konu}'
    
    İnternet Araştırma Verisi:
    {arastirma_verisi}
    
    Sistemin Şu Anki Yetenekler Kodu (Bunu güncelleyeceksin):
    ```python
    {mevcut_kod}
    ```
    
    🎯 **GÖREVİN VE KATI KURALLARIN:**
    1. **HAFIZAYA İTAAT ET:** Yukarıda 'KALICI HAFIZA DEVREDE' kısmında yazan tüm kurallara KESİNLİKLE uyarak bu kodu yaz.
    2. **ESKİYİ KORU VEYA GELİŞTİR:** Eğer kullanıcının isteği mevcut sistemi tamamen değiştirmek değilse, eski özellikleri bozmadan yenisini ekle. Çöpleri temizle. (Örn: `st.experimental_rerun` YERİNE DAİMA `st.rerun` KULLAN).
    3. **TEK BİR DÜZENLİ DOSYA OLUŞTUR:** Tüm yetenekleri `def ana_yetenekler():` altında Streamlit ile çalışacak şekilde birleştir. Sekmeler (Tabs) kullanarak şık bir tasarım yap.
    4. **SADECE KOD VER:** Bana SADECE ve SADECE en güncel, temizlenmiş, hatasız tam Python kodunu ver. Asla açıklama yazma.
    """
    
    yanit = model.generate_content(prompt)
    yeni_kod = yanit.text
    
    # AI'ın fazladan koyabileceği Markdown etiketlerini temizle
    yeni_kod = yeni_kod.replace("```python", "").replace("```", "").strip()
    return yeni_kod
    5. **ASLA ESKİ KODU KOPYALAYip YAMAMA (KATI KURAL):** Eski kodda yer alan mükerrer (duplicate), eski sürüm veya çakışan fonksiyonları tamamen çöpe at. Asla aynı işi yapan iki farklı sürüm bırakma. Sadece kullanıcının isteğini yerine getiren, en baştan yazılmış TEK ve TERTEMİZ bir kod blok yapısı kur.
    
