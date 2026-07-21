import streamlit as st
import traceback
import hashlib
import re

class AgentCodeArchitect:
    """
    Otonom ajan için OpenAI, Google DeepMind ve Microsoft AI prensipleri
    doğrultusunda kod üretim altyapısını yöneten ana mimari sınıfı.
    
    Bu sınıf, aşağıdaki endüstriyel standartları uygular:
    1. Üretilen her kod parçası katı bir hata yönetiminden (try-except blokları) geçer.
    2. Kod yazılmadan önce mantıksal bir 'planlama aşaması' simüle edilir.
    3. Kod kalitesi ve temizliği için gereksiz eski bloklar otomatik olarak temizlenir.
    """
    def __init__(self):
        st.subheader("🤖 Otonom Kod Mimarı Aktif")
        self.code_history = [] # Üretilen kod parçacıklarını kaydetmek için

    def _simulate_planning_phase(self, user_request: str) -> dict:
        """
        1. Planlama Aşaması: Kullanıcı isteğini analiz eder, problemi ayrıştırır
        ve kod üretimi için mantıksal bir plan oluşturur.
        Google DeepMind'ın zor problemlerin çözümüne odaklanan modüler yapılarını
        taklit eder. Bu aşama, karmaşık görevleri alt parçalara ayırır.
        """
        st.info(f"🧠 PLANLAMA AŞAMASI: '{user_request}' isteği için detaylı plan oluşturuluyor...")
        try:
            # Gerçek bir senaryoda, bu aşamada LLM veya gelişmiş bir NLP modeli
            # kullanıcının isteğini anlayıp, alt görevlere böler, gereksinimleri çıkarır
            # ve bir eylem planı oluşturur.
            plan = {
                "istek": user_request,
                "adım_1_analiz": "Kullanıcı isteği temel bileşenlerine ayrıştırılıyor ve ana hedefler belirleniyor.",
                "adım_2_modül_tasarımı": "Gerekli kod modülleri, fonksiyonlar ve sınıflar tasarlanıyor; bağımlılıklar öngörülüyor.",
                "adım_3_algoritma_seçimi": "Problem çözümü için en uygun algoritmalar, veri yapıları ve yaklaşımlar listeleniyor.",
                "adım_4_hata_öngörüsü": "Olası çalışma zamanı hataları, güvenlik açıkları ve performans darboğazları tahmin ediliyor; bunlara karşı koruma mekanizmaları planlanıyor.",
                "beklenen_çıktı_tipi": "Python fonksiyonu veya sınıfı içeren çalışabilir kod",
                "detay": f"Bu plan, '{user_request}' için sağlam, verimli ve hatasız bir kod yapısı oluşturmayı hedefler."
            }
            st.success("✅ Planlama tamamlandı.")
            return plan
        except Exception as e:
            st.error(f"❌ Planlama aşamasında beklenmeyen bir hata oluştu: {e}")
            st.code(traceback.format_exc())
            raise # Hatayı yukarı fırlat, süreci durdur

    def _simulate_code_generation(self, plan: dict) -> str:
        """
        2. Kod Üretimi Aşaması: Oluşturulan plana göre Python kodu üretir.
        OpenAI'ın iteratif ürün geliştirme prensiplerini yansıtır.
        Üretilen her kod parçası katı bir hata yönetimi (try-except blokları) içermelidir.
        """
        st.info(f"💻 KOD ÜRETİM AŞAMASI: Plan doğrultusunda kod üretimi başlatılıyor...")
        try:
            # Gerçek bir senaryoda, burada OpenAI API'si veya benzeri bir LLM çağrılır
            # ve planı baz alarak kod çıktısı alınır.
            # Simülasyon için, planı yansıtan, benzersiz adlandırılmış ve `try-except` içeren
            # örnek bir kod bloğu oluşturuyoruz.

            # Fonksiyon adını kullanıcı isteğinden türetme ve benzersiz hale getirme
            base_function_name = re.sub(r'[^a-zA-Z0-9_]', '', plan["istek"].lower().replace(" ", "_"))
            hash_suffix = hashlib.sha256(plan["istek"].encode()).hexdigest()[:8]
            unique_function_name = f"yetkinlik_{base_function_name}_{hash_suffix}"

            generated_code = f"""
import streamlit as st # Streamlit bileşenlerinin kullanımına izin verilir

def {unique_function_name}(*args, **kwargs):
    \"\"\"
    Bu fonksiyon, '{plan["istek"]}' isteği doğrultusunda otonom ajan tarafından üretilmiştir.
    Plan detayları: {plan.get('detay', 'Belirtilmemiş.')}
    \"\"\"
    st.info(f"'{unique_function_name}' yeteneği çalıştırılıyor...")
    try:
        # Gerçek kod mantığı buraya gelir.
        # Örneğin, argümanları işleyebilir veya belirli bir görevi yerine getirebilir.
        st.write(f"Argümanlar: {{args}}, Anahtar Kelime Argümanlar: {{kwargs}}")
        
        # Olası bir çıktı veya işlem simülasyonu
        if "hata_oluştur" in str(kwargs.values()).lower() or "hata_oluştur" in str(args).lower():
            raise ValueError("Simüle edilmiş özel bir hata durumu algılandı!")
        
        result_message = f"'{plan['istek']}' isteği başarıyla işlendi."
        st.success(f"✅ İşlem tamamlandı: {{result_message}}")
        return result_message
    except Exception as e:
        # Katı hata yönetimi: Her üretilen kod bloğu bu şekilde hata yakalamalıdır.
        st.error(f"❌ '{unique_function_name}' çalışırken bir hata oluştu: {{type(e).__name__}} - {{e}}")
        st.code(traceback.format_exc()) # Detaylı hata izi
        return f"HATA: İşlem tamamlanamadı. Detay: {{e}}"
"""
            st.success("✅ Kod üretimi tamamlandı.")
            return generated_code
        except Exception as e:
            st.error(f"❌ Kod üretimi aşamasında beklenmeyen bir hata oluştu: {e}")
            st.code(traceback.format_exc())
            raise # Hatayı yukarı fırlat

    def _simulate_code_quality_and_cleanup(self, generated_code: str) -> str:
        """
        3. Kod Kalitesi ve Temizliği (Refactoring) Aşaması: Üretilen kodu
        Microsoft AI'ın kurumsal ölçeklenebilirlik ilkelerine uygun olarak
        inceler, gereksiz eski blokları otomatik olarak temizler ve genel kod kalitesini artırır.
        """
        st.info("🧹 KOD KALİTESİ VE TEMİZLİK AŞAMASI: Üretilen kod inceleniyor ve refactor ediliyor...")
        try:
            # Gerçek bir senaryoda, bu aşamada statik kod analiz araçları (pylint, flake8),
            # otomatik formatlayıcılar (black, isort) veya hatta başka bir LLM
            # kodu kurumsal standartlara göre optimize eder, güvenlik açıklarını kontrol eder,
            # gereksiz kodları (eski yorumlar, kullanılmayan değişkenler) temizler.
            # Şu an için simülasyon olarak kodun başına bir açıklama ekliyoruz
            # ve belirli eski kalıpları güncelliyoruz.

            cleaned_code = "# Bu kod, kurumsal standartlara uygunluk ve temizlik kontrollerinden geçmiştir.\n" \
                           "# Gereksiz eski bloklar otomatik olarak temizlenmiştir.\n" \
                           + generated_code

            # Örnek bir otomatik temizlik/güncelleme: st.experimental_rerun -> st.rerun
            if "st.experimental_rerun" in cleaned_code:
                st.warning("Tespit edildi: Eski 'st.experimental_rerun' kullanımı 'st.rerun' olarak güncelleniyor.")
                cleaned_code = cleaned_code.replace("st.experimental_rerun", "st.rerun")
            
            # Eski veya gereksiz yorum satırlarını temizleme (basit bir örnek)
            # Bu, daha gelişmiş bir regex veya AST tabanlı analiz gerektirir.
            cleaned_code = re.sub(r'#+\s*Eski bloklar temizlendi\s*#+', '', cleaned_code)

            st.success("✅ Kod kalitesi ve temizlik aşaması tamamlandı.")
            return cleaned_code
        except Exception as e:
            st.error(f"❌ Kod temizliği ve refactor aşamasında beklenmeyen bir hata oluştu: {e}")
            st.code(traceback.format_exc())
            raise # Hatayı yukarı fırlat

    def generate_and_refine_code(self, user_request: str) -> str:
        """
        Tüm kod üretim ve rafine etme sürecini orkestre eden ana fonksiyondur.
        Her adımı `try-except` blokları ile sarmalar ve sürecin bütünlüğünü sağlar.
        """
        try:
            st.write("---")
            st.subheader(f"🔄 '{user_request}' isteği için yeni yetenek geliştirme süreci başladı...")

            # Adım 1: Planlama Aşaması
            plan = self._simulate_planning_phase(user_request)

            # Adım 2: Kod Üretimi Aşaması
            generated_code = self._simulate_code_generation(plan)

            # Adım 3: Kod Kalitesi ve Temizliği (Refactoring) Aşaması
            final_code = self._simulate_code_quality_and_cleanup(generated_code)

            self.code_history.append({"request": user_request, "code": final_code})
            st.success(f"🎉 '{user_request}' için yetenek başarıyla üretildi ve rafine edildi!")
            return final_code
        except Exception as e:
            st.error(f"🚨 GENEL SÜREÇ HATASI: Kod üretim ve rafine etme sürecinde beklenmeyen bir sorun oluştu: {e}")
            st.code(traceback.format_exc())
            return f"# Hata oluştu: {e}\n# Detay: {traceback.format_exc()}\ndef hata_olustu_fonksiyonu(): pass"

# Eğer bu dosya doğrudan çalıştırılırsa, bir test arayüzü sağlar.
# Asıl kullanım, bu sınıfın 'yetenekler.py' gibi başka bir dosya tarafından içe aktarılmasıyladır.
if __name__ == "__main__":
    st.set_page_config(layout="wide")
    st.title("Beyin.py Otonom Kod Mimarı Test Arayüzü")
    st.markdown("""
    Bu arayüz, `AgentCodeArchitect` sınıfının planlama, kod üretimi ve temizleme
    aşamalarını simüle ederek yeni yetenekler geliştirmesini gösterir.
    """)

    architect = AgentCodeArchitect()

    user_input = st.text_area("Yeni bir yetenek isteği girin (örn: 'kullanıcıya özel bir karşılama mesajı gösteren bir fonksiyon'):",
                               "iki sayıyı toplayan bir fonksiyon oluştur", height=100)

    if st.button("Kodu Üret ve Rafine Et", help="Planlama, kod üretimi ve temizlik aşamalarını çalıştırır."):
        with st.spinner("İstek işleniyor..."):
            result_code = architect.generate_and_refine_code(user_input)
            st.subheader("Üretilen ve Rafine Edilen Kod:")
            st.code(result_code, language="python")

            st.subheader("Üretilen Kodun Çalıştırılması (Simülasyon):")
            st.info("Üretilen kodu doğrudan `beyin.py` içerisinde `exec` ile çalıştırmak güvenlik riski taşıdığından, "
                    "burada sadece bir simülasyon ve örnek çağrı gösterilmektedir. "
                    "Gerçek entegrasyon `yetenekler.py` gibi güvenli bir ortamda yapılmalıdır.")
            
            # Üretilen koddan fonksiyon adını bulma
            match = re.search(r"def (\w+)\(", result_code)
            if match:
                func_name = match.group(1)
                st.markdown(f"**Üretilen fonksiyon adı:** `{func_name}`")
                
                st.markdown("##### Örnek Çağrılar:")
                st.code(f"{func_name}('test verisi', param='değer')", language="python")
                st.code(f"{func_name}(10, 20)", language="python")
                st.code(f"{func_name}('hata_oluştur', param='değer')", language="python")

                # Eğer exec kullanılsaydı (uyarılarla birlikte):
                # local_scope = {}
                # try:
                #     exec(result_code, globals(), local_scope)
                #     generated_func = local_scope.get(func_name)
                #     if generated_func:
                #         st.write("---")
                #         st.markdown("##### Gerçek Çağrı Sonucu (Örnek):")
                #         st.write(generated_func("örnek argüman", özel_parametre="test"))
                #         st.write("---")
                #         st.markdown("##### Hata Tetikleme Çağrısı (Örnek):")
                #         st.write(generated_func("örnek argüman", hata_oluştur="evet"))
                # except Exception as e:
                #     st.error(f"Üretilen kodu çalıştırma denemesinde hata: {e}")
                #     st.code(traceback.format_exc())
            else:
                st.warning("Üretilen kod içinde tanımlı bir Python fonksiyonu bulunamadı.")

    if st.session_state.get('architect_history_display', False):
        st.subheader("Üretilen Kod Geçmişi:")
        if architect.code_history:
            for i, entry in enumerate(architect.code_history):
                st.expander(f"İstek {i+1}: {entry['request']}", expanded=False).code(entry['code'], language="python")
        else:
            st.info("Henüz üretilmiş kod yok.")