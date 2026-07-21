import time
import logging
import re
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
import google.generativeai as genai

# Loglama sistemini yapılandırarak işlemlerin takibini kolaylaştıralım
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def metni_temizle(ham_metin):
    """
    Web sitelerinden çekilen ham HTML metinlerindeki gereksiz boşlukları,
    fazla satırları ve web çöpü karakterleri temizler.
    """
    if not ham_metin:
        return ""
    # Fazla boşlukları ve yeni satır karakterlerini tek boşluğa indirge
    temizlenmis = re.sub(r'\s+', ' ', ham_metin)
    return temizlenmis.strip()

def internette_ara(sorgu, maksimum_ sonuc=3):
    """
    DuckDuckGo arama motorunu kullanarak internet üzerinde güvenli ve 
    api anahtarı gerektirmeyen bir arama gerçekleştirir.
    """
    logging.info(f"'{sorgu}' için internet araması başlatılıyor...")
    bulunan_sonuclar = []
    
    try:
        with DDGS() as ddgs:
            # Belirtilen maksimum sonuç sayısı kadar arama yap
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
        logging.info(f"Toplam {len(bulunan_sonuclar)} adet arama sonucu başarıyla bulundu.")
    except Exception as hata:
        logging.error(f"İnternet araması sırasında bir hata oluştu: {hata}")
        
    return bulunan_sonuclar

def sayfa_icerigi_oku(url, zaman_asimi=5):
    """
    Verilen URL adresine bir tarayıcı gibi (User-Agent ile) bağlanır,
    sayfanın HTML içeriğini çeker ve sadece anlamlı metinleri (<p> etiketleri) ayıklar.
    """
    logging.info(f"Sayfa içeriği okunuyor: {url}")
    try:
        # Engellenmemek için gerçek bir tarayıcı kimliği (User-Agent) taklit ediyoruz
        basliklar = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        yanit = requests.get(url, headers=basliklar, timeout=zaman_asimi)
        
        if yanit.status_code == 200:
            soup = BeautifulSoup(yanit.text, 'html.parser')
            
            # Sayfadaki gereksiz script, stil, reklam ve gezinti menülerini kaldır
            for element in soup(["script", "style", "nav", "footer", "header", "aside"]):
                element.decompose()
                
            # Sadece paragraf etiketlerini (<p>) çekerek ana makale metnini alıyoruz
            paragraflar = soup.find_all('p')
            birlesmis_metin = " ".join([p.get_text() for p in paragraflar])
            
            # Metni temizle ve çok uznsa ilk 2500 karakteri sınırla (token tasarrufu için)
            temiz_metin = metni_temizle(birlesmis_metin)
            return temiz_metin[:2500]
        else:
            logging.warning(f"Sayfaya ulaşılamadı. HTTP Durum Kodu: {yanit.status_code}")
            return ""
    except requests.exceptions.Timeout:
        logging.warning(f"Zaman aşımı! Sayfa çok geç yanıt verdi: {url}")
        return ""
    except Exception as hata:
        logging.error(f"Sayfa okunurken beklenmeyen hata ({url}): {hata}")
        return ""

def arastirmayi_calistir(api_key, ana_konu, derinlik_seviyesi=3):
    """
    Kademeli (Multi-hop) Otonom Araştırma Motoru:
    1. Adım: Ana konu hakkında arama yapar ve siteleri okur.
    2. Adım: Elde edilen verilerden yapay zeka yardımıyla yeni alt anahtar kelimeler türetir.
    3. Adım: Derinlik seviyesi kadar bu döngüyü tekrarlayarak konuyu katman katman köşe bucak araştırır.
    4. Adım: Toplanan tüm devasa veriyi sentezleyerek kusursuz bir final raporu çıkarır.
    """
    if not api_key:
        raise ValueError("Google Gemini API anahtarı girilmedi!")
        
    genai.configure(api_key=api_key)
    # En güncel ve hızlı modeli kullanıyoruz
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    toplanan_hafiza = []
    mevcut_sorgu = ana_konu
    islenen_urller = set()
    
    logging.info(f"Otonom araştırma süreci başlatıldı. Konu: '{ana_konu}', Derinlik: {derinlik_seviyesi}")
    
    for seviye in range(1, derinlik_seviyesi + 1):
        logging.info(f"--- Tur {seviye} / {derinlik_seviyesi} yürütülüyor ---")
        
        # 1. İnternette arama yap
        arama_sonuclari = internette_ara(mevcut_sorgu, maksimum_sonuc=3)
        okunan_metinler_bu_tur = []
        
        for sonuc in arama_sonuclari:
            url = sonuc.get('href')
            # Aynı URL'yi tekrar okumamak için kontrol ediyoruz
            if url and url not in islenen_urller:
                islenen_urller.add(url)
                icerik = sayfa_icerigi_oku(url)
                if icerik:
                    okunan_metinler_bu_tur.append(icerik)
        
        if not okunan_metinler_bu_tur:
            logging.warning(f"Tur {seviye}'de okunabilir yeni içerik bulunamadı, bir sonraki adıma geçiliyor.")
            continue
            
        tur_verisi = " ".join(okunan_metinler_bu_tur)
        toplanan_hafiza.append(f"[Derinlik Seviyesi {seviye} Verileri]: {tur_verisi[:1500]}")
        
        # Eğer son seviyede değilsek, yapay zekaya bu metinden yola çıkarak bir sonraki tur için 
        # en akıllı alt arama terimini türettiriyoruz (Kademeli Derinleşme)
        if seviye < derinlik_seviyesi:
            yonlendirici_prompt = (
                f"Ana Konu: '{ana_konu}'\n"
                f"Şu anki turda elde edilen metin:\n{tur_verisi[:1000]}\n\n"
                f"GÖREV: Bu metne dayanarak konunun daha derinlerine inmek, "
                f"eksik kalmış teknik detayları veya alt başlıkları bulmak için "
                f"kullanılabilecek **en kritik ve spesifik 1 adet arama kelime öbeği** üret. "
                f"Asla açıklama yapma, sadece arama terimini yaz."
            )
            try:
                yanit_model = model.generate_content(yonlendirici_prompt)
                yeni_terim = yanit_model.text.strip()
                mevcut_sorgu = f"{ana_konu} {yeni_terim}"
                logging.info(f"Yeni türetilen derin arama sorgusu: '{mevcut_sorgu}'")
            except Exception as e:
                logging.error(f"Alt sorgu türetilemedi: {e}")
                
        # Sunucuları yormamak için kısa bir bekleme ekleyelim
        time.sleep(1)

    if not toplanan_hafiza:
        return "Üzgünüm, internet taraması sonucunda bu konuyla ilgili yeterli veri toplanamadı."

    # Toplanan tüm katmanlardaki verileri birleştirip nihai kapsamlı raporu yazdır
    logging.info("Tüm veriler toplandı, Gemini ile kapsamlı nihai rapor sentezleniyor...")
    
    nihai_sentez_prompt = (
        f"Aşağıda internetin farklı kaynaklarından otonom ajan tarafından taranarak toplanmış "
        f"derinlemesine araştırma verileri yer almaktadır:\n\n"
        f"{str(toplanan_hafiza)}\n\n"
        f"GÖREV: Yukarıdaki tüm ham ve dağınık verileri titizlikle analiz et. "
        f"'{ana_konu}' hakkında son derece profesyonel, akıcı, yapılandırılmış, "
        f"teknik detayları atlamayan, kapsamlı ve net bir araştırma raporu yaz."
    )
    
    nihai_rapor = model.generate_content(nihai_sentez_prompt)
    logging.info("Otonom araştırma raporu başarıyla tamamlandı.")
    
    return nihai_rapor.text
