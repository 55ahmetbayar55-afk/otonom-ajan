import time
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
import google.generativeai as genai

def internette_kod_arastir(sorgu):
    """Geliştirilecek özellik için internetten en güncel Python yöntemlerini araştırır."""
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

def yeni_yetenek_yaz(api_key, konu, mevcut_kod):
    """Eski çöpleri siler, güncel kütüphaneleri kullanır ve koda yeni özelliği entegre eder."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    arastirma_verisi = internette_kod_arastir(konu)
    
    prompt = f"""
    Sen kıdemli bir Python Kod Mimarı ve Otomatik Temizlik (Refactor) Uzmanısın.
    
    Kullanıcının Yeni İsteyi: '{konu}'
    
    İnternet Araştırma Verisi:
    {arastirma_verisi}
    
    Sistemin Şu Anki Yetenekler Kodu:
    ```python
    {mevcut_kod}
    ```
    
    🎯 **GÖREVİN VE KATI KURALLARIN:**
    1. **ESKİ SİSTEMLERİ TEMİZLE:** Mevcut koddaki artık kullanılmayan, çöpe dönmüş, hatalı veya güncelliğini yitirmiş (Örn: `st.experimental_rerun` yerine `st.rerun` kullan) ESKİ FONKSİYONLARI VE KODLARI SİL VEYA GÜNCELLE.
    2. **ÇAKIŞMALARI ENGELLE:** Yeni ekleyeceğin özellik eski kodla çakışıyorsa, eski olanı kaldırıp yenisini baskın kıl.
    3. **TEK BİR DÜZENLİ DOSYA OLUŞTUR:** Tüm yetenekleri derli toplu, `def ana_yetenekler():` altında Streamlit ile çalışacak şekilde birleştir.
    4. **SADECE KOD VER:** Bana SADECE ve SADECE en güncel, temizlenmiş, hatasız tam Python kodunu ver. Asla açıklama yazma.
    """
    
    yanit = model.generate_content(prompt)
    yeni_kod = yanit.text
    
    # Markdown temizliği
    yeni_kod = yeni_kod.replace("```python", "").replace("```", "").strip()
    return yeni_kod
