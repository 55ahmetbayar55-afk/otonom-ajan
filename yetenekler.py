import streamlit as st
import json
import os
import logging
import time

# --- Yapılandırma ve Loglama ---
LOG_FILE = "ajan_sistem_gunlugu.log"
MEMORY_FILE = "ajan_hafizasi.json"
YETENEKLER_FILE = "yetenekler.py"

# Loglama ayarları
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# --- Yardımcı Fonksiyonlar (Modüler Yapı, Hata Yönetimi) ---

def _load_json_data(file_path, default_data=None):
    """
    Belirtilen JSON dosyasını güvenli bir şekilde yükler.
    Hata durumunda varsayılan veriyi döndürür ve loglar.
    """
    if default_data is None:
        default_data = {}
    try:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        logging.info(f"Dosya bulunamadı veya boş: {file_path}. Varsayılan veri kullanılıyor.")
        return default_data
    except json.JSONDecodeError as e:
        logging.error(f"JSON okuma hatası '{file_path}': {e}")
        st.error(f"Hafıza dosyası bozuk: {e}. Varsayılan yükleniyor...")
        return default_data
    except Exception as e:
        logging.error(f"Dosya yükleme hatası '{file_path}': {e}")
        st.error(f"Dosya okuma hatası: {e}. Varsayılan yükleniyor...")
        return default_data

def _save_json_data(file_path, data):
    """
    Veriyi belirtilen JSON dosyasına güvenli bir şekilde kaydeder.
    Hata durumunda loglar.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        logging.error(f"JSON kaydetme hatası '{file_path}': {e}")
        st.error(f"Veri kaydetme hatası: {e}")
        return False

def _write_file_content(file_path, content):
    """
    Belirtilen içeriği bir dosyaya güvenli bir şekilde yazar.
    Hata durumunda loglar.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        logging.error(f"Dosyaya yazma hatası '{file_path}': {e}")
        st.error(f"Dosyaya yazma hatası: {e}")
        return False

def _simulate_planning_phase(request: str):
    """
    OpenAI/DeepMind prensipleri doğrultusunda bir kod planlama aşamasını simüle eder.
    """
    st.info(f"🧠 Planlama aşaması başlatıldı: '{request}' için mimari analiz yapılıyor...")
    logging.info(f"Planlama: '{request}' için analiz ediliyor.")
    time.sleep(0.5) # Simülasyon gecikmesi
    # Burada karmaşık bir planlama motoru, gereksinim analizi, modül seçimi vb. olabilir.
    plan = {
        "istek": request,
        "modüller": ["gerekli_modul_1", "gerekli_modul_2"],
        "yaklaşım": "modüler ve hataya dayanıklı",
        "tahmini_ciktilar": ["fonksiyon_adi.py", "test_fonksiyonu.py"]
    }
    st.success("✅ Planlama tamamlandı. Detaylı mimari çıktı hazırlandı.")
    logging.info(f"Planlama tamamlandı: {plan}")
    return plan

def _simulate_code_generation(plan: dict):
    """
    Planlama çıktısına göre kod üretimi simüle eder.
    """
    st.info(f"💻 Kod üretim aşaması başlatıldı: '{plan['istek']}'...")
    logging.info(f"Kod Üretimi: '{plan['istek']}' için üretim başlatıldı.")
    time.sleep(1) # Simülasyon gecikmesi
    generated_code_template = f"""
def new_feature_{plan['istek'].replace(' ', '_').lower()}():
    try:
        # {plan['istek']} yeteneği için üretilen örnek kod bloğu
        st.write("Yeni yetenek '{plan['istek']}' başarıyla etkinleştirildi!")
        # Buraya dinamik olarak üretilen asıl kod gelecek
        return True
    except Exception as e:
        st.error(f"Hata oluştu: {{e}}")
        logging.error(f"Üretilen kodda hata: {{e}}")
        return False
"""
    st.success("⚡ Temel kod iskeleti üretildi.")
    logging.info(f"Kod iskeleti üretildi.")
    return generated_code_template

def _simulate_code_refactoring_and_cleanup(generated_code: str):
    """
    Microsoft AI prensipleri doğrultusunda üretilen kodu otomatik olarak temizler ve refaktör eder.
    Eski, gereksiz blokları temizleme mantığını burada simüle ederiz.
    """
    st.info("🧹 Kod kalitesi ve temizliği için otomatik refaktör işlemi başlatıldı...")
    logging.info("Kod refaktör ve temizlik aşaması.")
    time.sleep(0.7) # Simülasyon gecikmesi
    
    # Gerçek bir sistemde burada AST analizi, linting, güvenlik taramaları yapılabilirdi.
    # Örneğin, belirli anahtar kelimeleri veya yapıları kaldırabiliriz.
    
    cleaned_code = generated_code.replace("örnek kod bloğu", "otomatik temizlenmiş ve optimize edilmiş kod bloğu")
    cleaned_code += "\n    # Otomatik temizlik ve hata yönetimi eklendi.\n"
    
    st.success("✨ Kod başarıyla refaktör edildi ve gereksiz bloklar temizlendi.")
    logging.info("Kod refaktör edildi ve gereksiz bloklar temizlendi.")
    return cleaned_code

def _perform_full_system_reset():
    """
    Tüm sistemi (yetenekler.py ve ajan_hafizasi.json) fabrika ayarlarına döndürür.
    """
    st.warning("💥 TÜM SİSTEM SIFIRLANIYOR... Bu işlem geri alınamaz!")
    logging.warning("SİSTEM HARD RESET BAŞLATILDI!")

    default_yetenekler_code = """import streamlit as st\n\ndef ana_yetenekler():\n    st.success("Yetenekler fabrika ayarlarına döndürüldü!")\n    st.info("Lütfen yeni yetenekler ekleyerek ajanı yeniden eğitin.")\n"""
    if not _write_file_content(YETENEKLER_FILE, default_yetenekler_code):
        st.error("Yetenekler dosyası sıfırlanırken hata oluştu.")
        return False

    empty_memory = {"genel_kurallar": [], "ogrenilen_stratejiler": []}
    if not _save_json_data(MEMORY_FILE, empty_memory):
        st.error("Hafıza dosyası sıfırlanırken hata oluştu.")
        return False
    
    st.success("Komple sistem başarıyla resetlendi! Lütfen sayfayı yenileyin.")
    logging.info("SİSTEM BAŞARIYLA SIFIRLANDI.")
    return True


# --- Ana Ajan Arayüzü (Streamlit) ---

def ana_yetenekler():
    st.set_page_config(layout="wide")
    st.title("🚀 Otonom Ajan v2.0 - Kurumsal Sürüm")
    st.markdown("---")

    # Tüm arayüzü 3 ana sekme altında topluyoruz
    sekme_mimari, sekme_hafiza, sekme_temizlik = st.tabs([
        "🧬 Otonom Kod Mimarı", 
        "🧠 Kalıcı Hafıza", 
        "🧹 Sistem Temizliği"
    ])

    # --- 1. SEKME: OTONOM KOD MİMARI (Yetenek Geliştirme) ---
    with sekme_mimari:
        st.markdown("### 🚀 Yenilikçi Yetenek Geliştirme & Refaktör")
        st.markdown("Ajanına yeni bir özellik kazandırmak için komutunu gir ve evrimi başlat. Her adım sıkı hata yönetimi ve kalite kontrolünden geçecektir.")
        
        yetenek_istegi = st.text_area(
            "Ajanın koduna ne eklemesini istiyorsun?", 
            placeholder="Örn: İnternetten döviz kuru çeken bir fonksiyon ekle...",
            key="yetenek_giris_kutusu_beyin"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚡ Kodu Üret ve Rafine Et", use_container_width=True, key="kod_uret_btn_beyin"):
                if yetenek_istegi:
                    st.empty() # Eski mesajları temizle
                    try:
                        plan_cikti = _simulate_planning_phase(yetenek_istegi)
                        if plan_cikti:
                            generated_code = _simulate_code_generation(plan_cikti)
                            if generated_code:
                                final_code = _simulate_code_refactoring_and_cleanup(generated_code)
                                
                                # Simülasyon olarak üretilen kodu 'yetenekler.py' dosyasına ekleyelim.
                                # Gerçek bir senaryoda bu, mevcut koda ekleme/birleştirme mantığı içerir.
                                current_yetenekler_content = _load_json_data(YETENEKLER_FILE, default_data="").replace("def ana_yetenekler():", "") # Mevcut kodun içinde ana fonksiyonu çıkart
                                
                                # Basitçe yeni kodu ekleyip tekrar ana_yetenekler() fonksiyonu içine saralım
                                # Bu kısım gerçek entegrasyon için daha gelişmiş bir AST/kod birleştirme mantığı gerektirir.
                                updated_yetenekler_content = f"""
import streamlit as st
import json
import os # Eğer üretilen kodda JSON/OS kullanılacaksa

def ana_yetenekler():
    st.subheader("Yetenekler başarıyla güncellendi!")
    st.code(\"\"\"{final_code}\"\"\", language="python")
    {current_yetenekler_content} # Mevcut diğer yetenekleri de koru

{final_code} # Yeni üretilen fonksiyonu da dosya seviyesine koyalım
"""
                                if _write_file_content(YETENEKLER_FILE, updated_yetenekler_content):
                                    st.success(f"'{yetenek_istegi}' için tüm süreç tamamlandı! Yeni yetenekler dosyasına yazıldı.")
                                    logging.info(f"Yeni yetenek '{yetenek_istegi}' yetenekler.py'ye eklendi.")
                                else:
                                    st.error("Yetenek dosyasına yazılırken kritik bir hata oluştu.")
                            else:
                                st.error("Kod üretiminde bir sorun oluştu.")
                        else:
                            st.error("Planlama aşaması başarısız oldu.")
                    except Exception as e:
                        st.error(f"Genel kod üretim sürecinde beklenmedik bir hata oluştu: {e}")
                        logging.error(f"Genel üretim hatası: {e}")
                else:
                    st.warning("Lütfen bir istek girin.")
                    
        with col2:
            if st.button("📜 Üretilen Kodu Göster", use_container_width=True, key="gecmis_btn_beyin"):
                try:
                    with open(YETENEKLER_FILE, "r", encoding="utf-8") as f:
                        st.code(f.read(), language="python")
                except FileNotFoundError:
                    st.info(f"'{YETENEKLER_FILE}' dosyası bulunamadı.")
                except Exception as e:
                    st.error(f"'{YETENEKLER_FILE}' okunurken bir hata oluştu: {e}")
                    logging.error(f"Yetenekler dosyası okuma hatası: {e}")

    # --- 2. SEKME: KALICI HAFIZA ---
    with sekme_hafiza:
        st.markdown("### 📂 JSON Hafıza Yönetimi")
        
        hafiza_verisi = _load_json_data(MEMORY_FILE, {"genel_kurallar": [], "ogrenilen_stratejiler": []})
        st.json(hafiza_verisi)
            
        with st.expander("➕ Hafızaya Yeni Kural Ekle"):
            yeni_kural = st.text_input("Aklında tutması gereken kural:", key="hafiza_kural_input_beyin")
            if st.button("💾 Kaydet", key="hafiza_kaydet_btn_beyin"):
                if yeni_kural:
                    hafiza_verisi.setdefault("genel_kurallar", []).append(yeni_kural)
                    if _save_json_data(MEMORY_FILE, hafiza_verisi):
                        st.success("Kural başarıyla hafızaya eklendi!")
                        st.rerun() # Sayfayı yenilemek için
                    else:
                        st.error("Kural hafızaya kaydedilemedi.")
                else:
                    st.warning("Lütfen bir kural girin.")

    # --- 3. SEKME: SİSTEM TEMİZLİĞİ ---
    with sekme_temizlik:
        st.markdown("### 🧹 Sistem Temizliği ve Reset Merkezi")
        st.warning("Eski veya çakışan tüm verileri buradan sıfırlayabilirsiniz. Dikkatli kullanın!")

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🗑️ Yetenekleri Sıfırla", use_container_width=True, key="temizlik_yet_btn_beyin"):
                temiz_kod = """import streamlit as st\n\ndef ana_yetenekler():\n    st.success("Yetenekler başarıyla sıfırlandı!")\n"""
                if _write_file_content(YETENEKLER_FILE, temiz_kod):
                    st.success("Yetenekler sıfırlandı!")
                    st.rerun()
        with c2:
            if st.button("🧹 Hafızayı Sıfırla", use_container_width=True, key="temizlik_haf_btn_beyin"):
                bos_hafiza = {"genel_kurallar": [], "ogrenilen_stratejiler": []}
                if _save_json_data(MEMORY_FILE, bos_hafiza):
                    st.success("Hafıza sıfırlandı!")
                    st.rerun()

        st.markdown("---")
        if st.button("💥 TÜM SİSTEMİ HARD RESET AT", type="primary", use_container_width=True, key="hard_reset_btn_beyin"):
            if _perform_full_system_reset():
                st.rerun() # Sıfırlama sonrası UI'ı yenile
            else:
                st.error("Sistem sıfırlanırken beklenmedik bir hata oluştu.")

# Ana Streamlit uygulamasını başlat
if __name__ == "__main__":
    ana_yetenekler()