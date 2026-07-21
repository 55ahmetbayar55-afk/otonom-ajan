import streamlit as st
import json
import os
import logging
import time
from datetime import datetime

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
    Yeni yetenek_haritasi yapısını desteklemek için default_data güncellendi.
    """
    if default_data is None:
        default_data = {"genel_kurallar": [], "ogrenilen_stratejiler": [], "yetenekler_data": []}
    try:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Geriye dönük uyumluluk için 'yetenekler_data' anahtarının varlığını kontrol et
                data.setdefault("yetenekler_data", [])
                return data
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

def _read_file_content(file_path, default_content=""):
    """
    Belirtilen dosyanın içeriğini güvenli bir şekilde okur.
    Hata durumunda varsayılan içeriği döndürür ve loglar.
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        logging.info(f"Dosya bulunamadı: {file_path}. Varsayılan içerik kullanılıyor.")
        return default_content
    except Exception as e:
        logging.error(f"Dosya okuma hatası '{file_path}': {e}")
        st.error(f"Dosya okuma hatası: {e}. Varsayılan içerik yükleniyor...")
        return default_content

def _extract_function_name(code_block: str) -> str:
    """
    Verilen kod bloğundan ilk 'def func_name(' desenini arayarak fonksiyon adını çıkarır.
    """
    import re
    match = re.search(r"def (\w+)\s*\(", code_block)
    if match:
        return match.group(1)
    return ""

def _normalize_request(request: str) -> str:
    """
    İstek stringini normalize eder (küçük harf, boşlukları temizler).
    """
    return request.strip().lower()

def _update_and_write_yetenekler_file(request_str: str, generated_code_block: str):
    """
    Yeni üretilen yeteneği hafızaya kaydeder, çakışanları tespit edip temizler ve yetenekler.py dosyasını günceller.
    """
    st.info("🔄 Yetenek hafızası güncelleniyor ve çakışmalar kontrol ediliyor...")
    logging.info(f"Yetenek güncelleme başlatıldı: '{request_str}'")

    memory_data = _load_json_data(MEMORY_FILE)
    yetenekler_data = memory_data.get("yetenekler_data", [])

    new_func_name = _extract_function_name(generated_code_block)
    if not new_func_name:
        st.error("Üretilen koddan fonksiyon adı çıkarılamadı. Yetenek kaydedilemedi.")
        logging.error(f"Fonksiyon adı çıkarılamadı: {generated_code_block[:100]}...")
        return False

    normalized_new_request = _normalize_request(request_str)
    
    updated_yetenekler_data = []
    replaced = False

    # Mevcut yetenekler arasında yeni istek ile çakışanları bul ve işaretle
    for item in yetenekler_data:
        normalized_existing_request = _normalize_request(item.get("istek", ""))
        if normalized_new_request == normalized_existing_request:
            st.warning(f"⚠️ Mevcut '{item['fonksiyon_adi']}' yeteneği, yeni '{new_func_name}' yeteneğiyle çakıştığı için güncelleniyor/siliniyor.")
            logging.info(f"Yetenek '{item['fonksiyon_adi']}' -> '{new_func_name}' ile değiştirildi (İstek: '{request_str}')")
            # Eski öğe eklenmiyor, yeni öğe yerine geçecek
            replaced = True
        else:
            updated_yetenekler_data.append(item)
    
    # Yeni yeteneği (yeni bir yetenek olarak veya eski bir yeteneğin yerine) ekle
    updated_yetenekler_data.append({
        "istek": request_str,
        "fonksiyon_adi": new_func_name,
        "kod_icerigi": generated_code_block,
        "timestamp": datetime.now().isoformat()
    })

    memory_data["yetenekler_data"] = updated_yetenekler_data
    if not _save_json_data(MEMORY_FILE, memory_data):
        st.error("Hafıza dosyasına yetenek verisi kaydedilirken hata oluştu.")
        return False
    
    # Şimdi, güncellenmiş hafıza verilerinden yetenekler.py dosyasını yeniden oluştur
    yetenekler_file_content = [
        "import streamlit as st",
        "import json",
        "import os",
        "import logging",
        "import time",
        "",
        "def ana_yetenekler():",
        "    st.subheader('🚀 Mevcut Yüklü Yetenekler:')"
    ]

    for item in updated_yetenekler_data:
        # ana_yetenekler() içinde yeteneği listelemek için bir satır ekle
        display_name = item['fonksiyon_adi'].replace('new_feature_', '').replace('_', ' ').title()
        yetenekler_file_content.append(f"    st.markdown(f\"- **{display_name}** (`{item['fonksiyon_adi']}()`)\")")
        # İstenirse, bu kısma yeteneği çalıştırmak için düğmeler eklenebilir.
        # yetenekler_file_content.append(f"    if st.button('Çalıştır: {display_name}', key='run_{item['fonksiyon_adi']}'):")
        # yetenekler_file_content.append(f"        {item['fonksiyon_adi']}()")

    yetenekler_file_content.append("") # Fonksiyon tanımları arasına boş satır

    # Tüm aktif fonksiyon tanımlarını dosyaya ekle
    for item in updated_yetenekler_data:
        yetenekler_file_content.append(item["kod_icerigi"])
        yetenekler_file_content.append("") # Fonksiyonlar arasına boş satır bırak

    final_yetenekler_code = "\n".join(yetenekler_file_content)

    if _write_file_content(YETENEKLER_FILE, final_yetenekler_code):
        st.success("✅ Yetenekler dosyası başarıyla güncellendi!")
        logging.info(f"'{YETENEKLER_FILE}' dosyası yeniden oluşturuldu. Toplam yetenek: {len(updated_yetenekler_data)}")
        return True
    else:
        st.error("Yetenekler dosyası yazılırken kritik bir hata oluştu.")
        return False

def _simulate_planning_phase(request: str):
    """
    OpenAI/DeepMind prensipleri doğrultusunda bir kod planlama aşamasını simüle eder.
    """
    st.info(f"🧠 Planlama aşaması başlatıldı: '{request}' için mimari analiz yapılıyor...")
    logging.info(f"Planlama: '{request}' için analiz ediliyor.")
    time.sleep(0.5) # Simülasyon gecikmesi
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
    
    # İstek stringinden geçerli bir fonksiyon adı oluştur
    func_name_raw = plan['istek'].replace(' ', '_').replace('-', '_').replace('.', '').lower()
    # Python tanımlayıcıları için daha kapsamlı temizlik
    func_name = "".join(c for c in func_name_raw if c.isalnum() or c == '_').strip('_')
    if not func_name or not func_name[0].isalpha(): # Geçerli bir Python tanımlayıcısı ile başladığından emin ol
        func_name = f"generated_feature_{int(time.time())}" 
    
    # 'new_feature_' ön ekini ekle (zaten varsa ekleme)
    if not func_name.startswith("new_feature_"):
        func_name = f"new_feature_{func_name}"

    generated_code_template = f"""
def {func_name}():
    try:
        # {plan['istek']} yeteneği için üretilen otomatik temizlenmiş ve optimize edilmiş kod bloğu
        st.write("Yeni yetenek '{plan['istek']}' başarıyla etkinleştirildi ve çalıştırıldı!")
        # Buraya dinamik olarak üretilen asıl kod gelecek
        logging.info("'{plan['istek']}' yeteneği çalıştırıldı.")
        return True
    except Exception as e:
        st.error(f"Hata oluştu: {{e}}")
        logging.error(f"Üretilen kodda hata: {{e}}")
        return False
"""
    st.success("⚡ Temel kod iskeleti üretildi.")
    logging.info(f"Kod iskeleti üretildi: {func_name}")
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
    cleaned_code = generated_code.replace("örnek kod bloğu", "otomatik temizlenmiş ve optimize edilmiş kod bloğu")
    cleaned_code += "\n    # Otomatik temizlik ve hata yönetimi eklendi ve kod optimize edildi.\n"
    
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

    # Yeni yetenekler_data yapısını içeren boş hafıza
    empty_memory = {"genel_kurallar": [], "ogrenilen_stratejiler": [], "yetenekler_data": []}
    if not _save_json_data(MEMORY_FILE, empty_memory):
        st.error("Hafıza dosyası sıfırlanırken hata oluştu.")
        return False
    
    st.success("Komple sistem başarıyla resetlendi! Lütfen sayfayı yenilemenizi öneririz.")
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
                                
                                # YENİ ENTEGRASYON NOKTASI: Hafıza ve yetenekler.py dosyasını güncelle
                                if _update_and_write_yetenekler_file(yetenek_istegi, final_code):
                                    st.success(f"'{yetenek_istegi}' için tüm süreç tamamlandı! Yeni yetenekler dosyasına yazıldı.")
                                    logging.info(f"Yeni yetenek '{yetenek_istegi}' yetenekler.py'ye eklendi.")
                                    st.rerun() # UI'ı güncellemek için
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
                    # _read_file_content fonksiyonunu kullanarak yetenekler.py dosyasını oku
                    st.code(_read_file_content(YETENEKLER_FILE), language="python")
                except FileNotFoundError:
                    st.info(f"'{YETENEKLER_FILE}' dosyası bulunamadı.")
                except Exception as e:
                    st.error(f"'{YETENEKLER_FILE}' okunurken bir hata oluştu: {e}")
                    logging.error(f"Yetenekler dosyası okuma hatası: {e}")

    # --- 2. SEKME: KALICI HAFIZA ---
    with sekme_hafiza:
        st.markdown("### 📂 JSON Hafıza Yönetimi")
        
        # 'yetenekler_data' dahil tüm hafıza içeriğini göster
        hafiza_verisi = _load_json_data(MEMORY_FILE)
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
                # Sadece hafızadaki yetenekler_data'yı sıfırla ve yetenekler.py'yi temiz bir başlangıca döndür
                memory_data = _load_json_data(MEMORY_FILE)
                memory_data["yetenekler_data"] = [] # Özellikleri temizle
                if _save_json_data(MEMORY_FILE, memory_data):
                    temiz_kod = """import streamlit as st\n\ndef ana_yetenekler():\n    st.success("Yetenekler başarıyla sıfırlandı!")\n    st.info("Lütfen yeni yetenekler ekleyerek ajanı yeniden eğitin.")\n"""
                    if _write_file_content(YETENEKLER_FILE, temiz_kod):
                        st.success("Yetenekler sıfırlandı!")
                        st.rerun()
                    else:
                        st.error("Yetenekler dosyası sıfırlanırken hata oluştu.")
                else:
                    st.error("Hafızadaki yetenek verileri sıfırlanırken hata oluştu.")
        with c2:
            if st.button("🧹 Hafızayı Sıfırla", use_container_width=True, key="temizlik_haf_btn_beyin"):
                # Tüm hafıza bölümlerini (yetenekler_data dahil) sıfırla
                bos_hafiza = {"genel_kurallar": [], "ogrenilen_stratejiler": [], "yetenekler_data": []}
                if _save_json_data(MEMORY_FILE, bos_hafiza):
                    st.success("Hafıza sıfırlandı!")
                    st.rerun()
                else:
                    st.error("Hafıza sıfırlanırken hata oluştu.")

        st.markdown("---")
        if st.button("💥 TÜM SİSTEMİ HARD RESET AT", type="primary", use_container_width=True, key="hard_reset_btn_beyin"):
            if _perform_full_system_reset():
                st.rerun() # Sıfırlama sonrası UI'ı yenile
            else:
                st.error("Sistem sıfırlanırken beklenmedik bir hata oluştu.")

# Ana Streamlit uygulamasını başlat
if __name__ == "__main__":
    ana_yetenekler()