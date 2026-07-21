import time
import logging
import re
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
import google.generativeai as genai

logging.basicConfig(level=logging.INFO)

def metni_temizle(ham_metin):
    if not ham_metin:
        return ""
    temizlenmis = re.sub(r'\s+', ' ', ham_metin)
    return temizlenmis.strip()

def internette_ara(sorgu, maksimum_sonuc=3):
    bulunan_sonuclar = []
    try:
        with DDGS() as ddgs:
            for sonuc in ddgs.text(sorgu, max_results=maksimum_sonuc):
                baslik = sonuc.get('title', 'Başlık Yok')
                url = sonuc.get('href', '')
                ozet = sonuc.get('body', '')
                if url:
                    bulunan_sonuclar.append({
                        'title': baslik,
                        'href': url,
                        'body': ozet
                    })
    except Exception as e:
        logging.error(f"Arama hatası: {e}")
    return bulunan_sonuclar

def sayfa_icerigi_oku(url, zaman_asimi=5):
    try:
        basliklar = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        yanit = requests.get(url, headers=basliklar, timeout=zaman_asimi)
        if yanit.status_code == 200:
            soup = BeautifulSoup(yanit.text, 'html.parser')
            for element in soup(["script", "style", "nav", "footer", "header", "aside"]):
                element.decompose()
            paragraflar = soup.find_all('p')
            birlesmis_metin = " ".join([p.get_text() for p in paragraflar])
            temiz_metin = metni_temizle(birlesmis_metin)
            return temiz_metin[:2500]
        return ""
    except Exception:
        return ""

def arastirmayi_calistir(api_key, ana_konu, derinlik_seviyesi=3):
    if not api_key:
        raise ValueError("Google Gemini API anahtarı girilmedi!")
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    toplanan_hafiza = []
    mevcut_sorgu = ana_konu
    islenen_urller = set()
    
    for seviye in range(1, derinlik_seviyesi + 1):
        arama_sonuclari = internette_ara(mevcut_sorgu, maksimum_sonuc=3)
        okunan_metinler_bu_tur = []
        
        for sonuc in arama_sonuclari:
            url = sonuc.get('href')
            if url and url not in islenen_urller:
                islenen_urller.add(url)
                icerik = sayfa_icerigi_oku(url)
                if icerik:
                    okunan_metinler_bu_tur.append(icerik)
        
        if not okunan_metinler_bu_tur:
            continue
            
        tur_verisi = " ".join(okunan_metinler_bu_tur)
        toplanan_hafiza.append(f"[Derinlik Seviyesi {seviye} Verileri]: {tur_verisi[:1500]}")
        
        if seviye < derinlik_seviyesi:
            yonlendirici_prompt = (
                f"Ana Konu: '{ana_konu}'\n"
                f"Şu anki turda elde edilen metin:\n{tur_verisi[:1000]}\n\n"
                f"GÖREV: Bu metne dayanarak konunun daha derinlerine inmek için "
                f"en kritik 1 adet arama kelime öbeği üret. Sadece arama terimini yaz."
            )
            try:
                yanit_model = model.generate_content(yonlendirici_prompt)
                yeni_terim = yanit_model.text.strip()
                mevcut_sorgu = f"{ana_konu} {yeni_terim}"
            except Exception:
                pass
                
        time.sleep(1)

    if not toplanan_hafiza:
        return "Üzgünüm, internet taraması sonucunda bu konuyla ilgili yeterli veri toplanamadı."

    nihai_sentez_prompt = (
        f"Aşağıda internetten otonom taranarak toplanmış veriler yer almaktadır:\n\n"
        f"{str(toplanan_hafiza)}\n\n"
        f"GÖREV: '{ana_konu}' hakkında detaylı, profesyonel ve kapsamlı bir araştırma raporu yaz."
    )
    
    nihai_rapor = model.generate_content(nihai_sentez_prompt)
    return nihai_rapor.text
