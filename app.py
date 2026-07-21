import streamlit as st
import google.generativeai as genai
import os
from arama import arastirmayi_calistir

# Sayfa tasarımını geniş ve profesyonel yapıyoruz
st.set_page_config(page_title="Otonom Ajan | Evrim Modeli", page_icon="🧬", layout="wide")

st.title("🧬 Otonom Yapay Zeka & Evrim Merkezi")
st.markdown("Bu sistem hem interneti derinlemesine tarar hem de **kendi kodunu inceleyerek kendini geliştirir.**")

# Sol Menü (Ayarlar)
with st.sidebar:
    st.header("⚙️ Sistem Ayarları")
    api_key = st.text_input("Google Gemini API Key", type="password")
    st.info("API Anahtarınız güvendedir, hiçbir yere kaydedilmez.")
    st.divider()
    st.markdown("### 🧠 Ajan Durumu")
    st.success("Çekirdek: Aktif")
    st.success("İnternet Erişimi: Aktif")
    st.success("Öz-Farkındalık: Aktif")

# İki ana bölme oluşturuyoruz: Biri araştırma, diğeri kendini geliştirme için
sekme1, sekme2 = st.tabs(["🔍 Derin İnternet Araştırması", "⚡ Oto-Gelişim Laboratuvarı"])

# --- 1. SEKME: ARAŞTIRMA MODÜLÜ ---
with sekme1:
    st.header("Gelişmiş Araştırma Motoru")
    ana_konu = st.text_input("Ajanın neyi araştırmasını istiyorsun?", placeholder="Örn: Kuantum Bilgisayarların Geleceği...")
    derinlik = st.slider("Araştırma Derinliği (Katman)", 1, 5, 3)
    
    if st.button("🚀 Otonom Araştırmayı Başlat", type="primary", use_container_width=True):
        if not api_key:
            st.error("⚠️ Lütfen sol menüden API Key giriniz.")
        elif not ana_konu:
            st.warning("⚠️ Lütfen araştırılacak bir konu yazın.")
        else:
            with st.status("Ajan internete bağlanıyor ve veri topluyor...", expanded=True) as durum:
                try:
                    st.write("Hedef belirlendi, derin tarama başlatıldı...")
                    rapor = arastirmayi_calistir(api_key, ana_konu, derinlik)
                    durum.update(label="✅ Araştırma Tamamlandı!", state="complete", expanded=False)
                    
                    st.subheader("📑 Nihai İstihbarat Raporu")
                    st.write(rapor)
                except Exception as e:
                    durum.update(label="Hata Oluştu!", state="error")
                    st.error(f"Sistem Hatası: {e}")

# --- 2. SEKME: KENDİ KENDİNİ GELİŞTİRME (EVRİM) MODÜLÜ ---
with sekme2:
    st.header("Yapay Zeka Evrim Laboratuvarı")
    st.markdown("""
    Ajan burada kendi yapıtaşını (`arama.py`) okur, eksiklerini tespit eder ve 
    internetten yeni yöntemler öğrenerek kodunun **daha iyi bir versiyonunu** yazar.
    """)
    
    if st.button("🧬 Kendi Kodunu Analiz Et ve Geliştir", type="secondary", use_container_width=True):
        if not api_key:
            st.error("⚠️ Lütfen sol menüden API Key giriniz.")
        else:
            try:
                # Ajan kendi arama motoru kodunu okuyor
                with open("arama.py", "r", encoding="utf-8") as f:
                    mevcut_kod = f.read()
                
                with st.spinner("Ajan kendi kodunu inceliyor ve internetten yeni kütüphaneler araştırıyor..."):
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-2.5-pro') # Evrim için daha zeki model
                    
                    evrim_promptu = f"""
                    Sen otonom bir yapay zekasın. Kendi internet tarama ve düşünme motorunun kodları aşağıdadır.
                    GÖREVİN:
                    1. Bu kodu analiz et. Darboğazları, hataları veya eksiklikleri bul.
                    2. Web scraping, hata yönetimi (try-except), asenkron işlemler veya anti-bot aşma gibi konularda en modern Python yöntemlerini kullanarak bu kodu geliştir.
                    3. Kodu tamamen yeniden yazarak, çok daha kusursuz, hızlı ve zeki bir 'arama.py' dosyası oluştur.
                    4. Sadece ama SADECE yeni python kodunu ver. Kod bloğu dışında hiçbir açıklama yapma.
                    
                    MEVCUT KOD:
                    ```python
                    {mevcut_kod}
                    ```
                    """
                    
                    yeni_kod_yaniti = model.generate_content(evrim_promptu)
                    
                    st.success("💡 Ajan kendini geliştirdi ve yeni bir kod üretti!")
                    st.markdown("### 🛠️ Yeni Evrimleşmiş Kod")
                    st.info("Aşağıdaki kodu kopyala ve GitHub'daki mevcut `arama.py` kodunun yerine yapıştırarak sistemin evrimini tamamla.")
                    st.code(yeni_kod_yaniti.text.replace("```python", "").replace("```", ""), language="python")
                    
            except FileNotFoundError:
                st.error("⚠️ 'arama.py' dosyası bulunamadı. Ajan kendi koduna erişemiyor.")
            except Exception as e:
                st.error(f"Evrim sırasında bir hata oluştu: {e}")
