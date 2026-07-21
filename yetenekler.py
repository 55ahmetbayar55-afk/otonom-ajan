import streamlit as st
import traceback
import hashlib
import re
import collections
from typing import List, Dict, Any

# Simulate external internet research data. In a real scenario, this would involve API calls to search engines.
# This dictionary holds pre-defined "search results" for various queries, simulating multiple sources
# with varying degrees of accuracy/completeness.
_SIMULATED_RESEARCH_DB = {
    "Python Async/Await": [
        {"source": "Wikipedia", "content": "Async/await in Python allows writing concurrent code that looks like sequential code. `async` defines a coroutine, `await` pauses execution until another coroutine completes. Introduced in Python 3.5. Uses `asyncio` library. Primarily for I/O-bound tasks."},
        {"source": "StackOverflow", "content": "Python's async/await is for I/O bound operations. `async def` marks a function as a coroutine. `await` can only be used inside `async` functions to wait for futures or other coroutines. Avoid for CPU-bound tasks, use `multiprocessing` instead. It does not replace threads for CPU-bound tasks."},
        {"source": "RealPython Blog", "content": "Async/await facilitates non-blocking operations. The event loop schedules coroutines. Key concepts: coroutines, event loop, futures, tasks. Example: `async def main(): await asyncio.sleep(1); print('Hello')`. Important for web servers, database access, networking."},
        {"source": "Medium Article (less reliable)", "content": "Async/await is a way to make Python faster. Just use `async` everywhere and your code will be concurrent. It's a replacement for threads and works for any task type. (Contains some misleading info)"},
        {"source": "Official Python Docs", "content": "The `asyncio` module provides infrastructure for writing concurrent code using the `async`/`await` syntax. Coroutines are generalized subroutines. `await` expressions are used to suspend the execution of the current coroutine until the result of the `awaitable` is ready. Best for network clients/servers and other I/O libraries."},
    ],
    "Duck Typing Principle": [
        {"source": "Wikipedia", "content": "Duck typing is a style of dynamic typing in which an object's current set of methods and properties determines the valid semantics, rather than its inheritance from a particular class or implementation of a specific interface. If it walks like a duck and quacks like a duck, then it must be a duck."},
        {"source": "GeeksForGeeks", "content": "In Python, duck typing is a concept related to dynamic typing. It says: 'If it looks like a duck and quacks like a duck, it's a duck.' This means you don't care about the type of object, only that it has the methods you want to call. It promotes flexible code."},
        {"source": "Python Central (outdated)", "content": "Duck typing is about making sure your object is exactly a `Duck` class instance. It's a strict type checking mechanism. It's similar to static typing. (Incorrect information)"},
        {"source": "StackOverflow", "content": "Duck typing means that the type or the class of an object is less important than the methods it defines. For example, you can pass any object with a `__len__` method to `len()`, not just lists or tuples. Python embraces duck typing heavily. It's a powerful concept for polymorphism."},
    ],
    "Python Decorators": [
        {"source": "Medium Blog", "content": "Decorators are functions that take another function as an argument and extend its behavior without explicitly modifying it. They use the `@decorator_name` syntax. Useful for logging, authentication, rate limiting, and caching. Often return a wrapper function."},
        {"source": "RealPython", "content": "A Python decorator is a function that takes a function as its argument and returns another function. Decorators allow you to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it. Syntactic sugar is `@`. They are higher-order functions."},
        {"source": "Wikipedia", "content": "Decorators in Python are a form of syntactic sugar for higher-order functions. They allow programmers to modify or extend a function or class definition. The concept is similar to annotations in Java or attributes in C#. They enable aspects of aspect-oriented programming."},
        {"source": "Random Forum Post", "content": "Decorators just make your code look fancy. They don't actually do much. You can achieve the same with simple function calls, it's mostly for style. (Understates their utility)"}
    ]
}

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
        if 'code_history' not in st.session_state:
            st.session_state.code_history = []

    def _simulate_planning_phase(self, user_request: str) -> dict:
        """
        1. Planlama Aşaması: Kullanıcı isteğini analiz eder, problemi ayrıştırır
        ve kod üretimi için mantıksal bir plan oluşturur.
        Google DeepMind'ın zor problemlerin çözümüne odaklanan modüler yapılarını
        taklit eder. Bu aşama, karmaşık görevleri alt parçalara ayırır.
        """
        st.info(f"🧠 PLANLAMA AŞAMASI: '{user_request}' isteği için detaylı plan oluşturuluyor...")
        try:
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
            raise

    def _simulate_code_generation(self, plan: dict) -> str:
        """
        2. Kod Üretimi Aşaması: Oluşturulan plana göre Python kodu üretir.
        OpenAI'ın iteratif ürün geliştirme prensiplerini yansıtır.
        Üretilen her kod parçası katı bir hata yönetimi (try-except blokları) içermelidir.
        """
        st.info(f"💻 KOD ÜRETİM AŞAMASI: Plan doğrultusunda kod üretimi başlatılıyor...")
        try:
            base_function_name = re.sub(r'[^a-zA-Z0-9_]', '', plan["istek"].lower().replace(" ", "_"))
            hash_suffix = hashlib.sha256(plan["istek"].encode()).hexdigest()[:8]
            unique_function_name = f"yetkinlik_{base_function_name}_{hash_suffix}"

            generated_code = f"""
import streamlit as st

def {unique_function_name}(*args, **kwargs):
    \"\"\"
    Bu fonksiyon, '{plan["istek"]}' isteği doğrultusunda otonom ajan tarafından üretilmiştir.
    Plan detayları: {plan.get('detay', 'Belirtilmemiş.')}
    \"\"\"
    st.info(f"'{unique_function_name}' yeteneği çalıştırılıyor...")
    try:
        st.write(f"Argümanlar: {{args}}, Anahtar Kelime Argümanlar: {{kwargs}}")
        
        if "hata_olustur" in str(kwargs.values()).lower() or "hata_olustur" in str(args).lower():
            raise ValueError("Simüle edilmiş özel bir hata durumu algılandı!")
        
        result_message = f"'{plan['istek']}' isteği başarıyla işlendi."
        st.success(f"✅ İşlem tamamlandı: {{result_message}}")
        return result_message
    except Exception as e:
        st.error(f"❌ '{unique_function_name}' çalışırken bir hata oluştu: {{type(e).__name__}} - {{e}}")
        st.code(traceback.format_exc())
        return f"HATA: İşlem tamamlanamadı. Detay: {{e}}"
"""
            st.success("✅ Kod üretimi tamamlandı.")
            return generated_code
        except Exception as e:
            st.error(f"❌ Kod üretimi aşamasında beklenmeyen bir hata oluştu: {e}")
            st.code(traceback.format_exc())
            raise

    def _simulate_code_quality_and_cleanup(self, generated_code: str) -> str:
        """
        3. Kod Kalitesi ve Temizliği (Refactoring) Aşaması: Üretilen kodu
        Microsoft AI'ın kurumsal ölçeklenebilirlik ilkelerine uygun olarak
        inceler, gereksiz eski blokları otomatik olarak temizler ve genel kod kalitesini artırır.
        """
        st.info("🧹 KOD KALİTESİ VE TEMİZLİK AŞAMASI: Üretilen kod inceleniyor ve refactor ediliyor...")
        try:
            cleaned_code = "# Bu kod, kurumsal standartlara uygunluk ve temizlik kontrollerinden geçmiştir.\n" \
                           "# Gereksiz eski bloklar otomatik olarak temizlenmiştir.\n" \
                           + generated_code

            # Örnek bir otomatik temizlik/güncelleme simülasyonu:
            # st.experimental_rerun kullanımdan kalkmıştır, yerine st.rerun kullanılmalıdır.
            # Üretilen kod doğrudan bu ifadeyi içermese de, olası eski kalıpların temizliğini simüle ederiz.
            if "st.experimental_rerun" in cleaned_code:
                st.warning("Tespit edildi: Eski 'st.experimental_rerun' kullanımı 'st.rerun' olarak güncelleniyor.")
                cleaned_code = cleaned_code.replace("st.experimental_rerun", "st.rerun")
            
            cleaned_code = re.sub(r'#+\s*Eski bloklar temizlendi\s*#+', '', cleaned_code)

            st.success("✅ Kod kalitesi ve temizlik aşaması tamamlandı.")
            return cleaned_code
        except Exception as e:
            st.error(f"❌ Kod temizliği ve refactor aşamasında beklenmeyen bir hata oluştu: {e}")
            st.code(traceback.format_exc())
            raise

    def generate_and_refine_code(self, user_request: str) -> str:
        """
        Tüm kod üretim ve rafine etme sürecini orkestre eden ana fonksiyondur.
        Her adımı `try-except` blokları ile sarmalar ve sürecin bütünlüğünü sağlar.
        """
        try:
            st.write("---")
            st.subheader(f"🔄 '{user_request}' isteği için yeni yetenek geliştirme süreci başladı...")

            plan = self._simulate_planning_phase(user_request)
            generated_code = self._simulate_code_generation(plan)
            final_code = self._simulate_code_quality_and_cleanup(generated_code)

            st.session_state.code_history.append({"request": user_request, "code": final_code})
            st.success(f"🎉 '{user_request}' için yetenek başarıyla üretildi ve rafine edildi!")
            return final_code
        except Exception as e:
            st.error(f"🚨 GENEL SÜREÇ HATASI: Kod üretim ve rafine etme sürecinde beklenmeyen bir sorun oluştu: {e}")
            st.code(traceback.format_exc())
            return f"# Hata oluştu: {e}\n# Detay: {traceback.format_exc()}\ndef hata_olustu_fonksiyonu(): pass"

    def _normalize_text(self, text: str) -> str:
        """Metni küçük harfe dönüştürür ve noktalama işaretlerini kaldırır."""
        return re.sub(r'[^\w\s]', '', text).lower()

    def _extract_key_phrases(self, text: str, n_gram_range=(1, 3)) -> List[str]:
        """Metinden anahtar kelime ve kelime öbeklerini çıkarır."""
        words = [word for word in self._normalize_text(text).split() if len(word) > 2]
        phrases = []
        for n in range(n_gram_range[0], n_gram_range[1] + 1):
            phrases.extend([" ".join(words[i:i+n]) for i in range(len(words) - n + 1)])
        return phrases

    def guvenli_arastirma_ve_dogrulama(self, query: str) -> Dict[str, Any]:
        """
        İnternetten çok kaynaklı veri toplayıp doğrulayan ve sentezleyen modül.
        En az 3 farklı kaynaktaki bilgiyi karşılaştırarak ortak noktaları alır,
        çelişkili veya uydurma bilgileri eler ve en yüksek güvenilirlik skoruna sahip bilgileri sentezler.
        """
        st.subheader(f"🌐 GÜVENLİ ARAŞTIRMA VE DOĞRULAMA: '{query}' için bilgi doğrulama başlatılıyor...")
        try:
            # 1. Kaynaklardan veri toplama simülasyonu
            raw_findings = _SIMULATED_RESEARCH_DB.get(query, [])
            
            if not raw_findings:
                st.warning(f"⚠️ '{query}' için simüle edilmiş araştırma verisi bulunamadı. Genel bir yanıt dönülüyor.")
                return {
                    "query": query,
                    "status": "No specific data found",
                    "reliable_summary": f"'{query}' konusunda yeterli bilgi bulunamadı. Lütfen daha spesifik bir sorgu deneyin veya genel bilgiye başvurun.",
                    "raw_findings": [],
                    "common_points": [],
                    "conflicting_points": []
                }
            
            st.info(f"Toplanan {len(raw_findings)} kaynak verisi:")
            for i, f in enumerate(raw_findings):
                st.markdown(f"- **Kaynak {i+1} ({f['source']}):** `{f['content'][:100]}...`")

            # En az 3 kaynak kontrolü
            if len(raw_findings) < 3:
                st.warning(f"⚠️ Yeterli kaynak ({len(raw_findings)}) bulunamadı. Güvenilirlik analizi kısıtlı olacaktır.")
            
            # 2. Bilgileri karşılaştırma ve güvenilirlik puanlama
            all_phrases = collections.defaultdict(int) # phrase -> count of sources
            source_phrases = [] # List of phrases (as sets) for each source
            
            for finding in raw_findings:
                phrases = self._extract_key_phrases(finding["content"])
                source_phrases.append(set(phrases))
                for phrase in set(phrases):
                    all_phrases[phrase] += 1
            
            # 3. Ortak noktaları ve çelişkili bilgileri belirleme
            total_sources = len(raw_findings)
            common_points = []
            conflicting_points = []
            
            # A threshold for "common": appears in at least 3 sources OR majority if total sources > 3
            common_threshold = max(3, total_sources // 2 + 1)
            
            reliable_info_phrases = set()
            
            for phrase, count in all_phrases.items():
                if count >= common_threshold:
                    common_points.append({"phrase": phrase, "reliability_score": count, "sources": [f['source'] for f, sp in zip(raw_findings, source_phrases) if phrase in sp]})
                    reliable_info_phrases.add(phrase)
                elif count <= total_sources // 3 and count > 0: # Appears in few sources, potentially conflicting
                    conflicting_points.append({"phrase": phrase, "reliability_score": count, "sources": [f['source'] for f, sp in zip(raw_findings, source_phrases) if phrase in sp]})

            # 4. En yüksek güvenilirlik skoruna sahip bilgileri sentezleme
            reliable_summary_parts = []
            
            if reliable_info_phrases:
                st.success("✅ Yüksek güvenilirlikli ortak noktalar belirlendi.")
                
                phrases_to_summarize = sorted(list(reliable_info_phrases), key=len, reverse=True)
                
                final_phrases_for_summary = []
                for p1 in phrases_to_summarize:
                    is_redundant = False
                    for p2 in final_phrases_for_summary:
                        if p1 in p2:
                            is_redundant = True
                            break
                    if not is_redundant:
                        final_phrases_for_summary.append(p1)

                reliable_summary = ". ".join([p.capitalize() for p in final_phrases_for_summary if all_phrases[p] >= common_threshold]) + "."
                if not reliable_summary.strip():
                    reliable_summary = ". ".join([p.capitalize() for p in phrases_to_summarize[:min(5, len(phrases_to_summarize))]]) + "."

                st.info("🎯 Güvenilir sentezlenmiş bilgi oluşturuldu.")
            else:
                reliable_summary = f"'{query}' hakkında yeterince ortak ve güvenilir bilgi bulunamadı. Çelişkili bilgiler olabilir."
                st.warning("⚠️ Yeterli ortak bilgi bulunamadı. Doğrulama zorluğu var.")

            st.success("✅ Çok kaynaklı doğrulama ve sentezleme tamamlandı.")

            return {
                "query": query,
                "status": "Success",
                "raw_findings": raw_findings,
                "common_points": common_points,
                "conflicting_points": conflicting_points,
                "reliable_summary": reliable_summary.replace("..", ".")
            }

        except Exception as e:
            st.error(f"❌ Güvenli araştırma ve doğrulama aşamasında bir hata oluştu: {e}")
            st.code(traceback.format_exc())
            return {
                "query": query,
                "status": "Error",
                "reliable_summary": f"Araştırma sırasında hata oluştu: {e}",
                "raw_findings": [],
                "common_points": [],
                "conflicting_points": []
            }

def ana_yetenekler():
    """
    Bu fonksiyon, otonom kod mimarının Streamlit arayüzünü ve temel yeteneklerini
    tek bir düzenli çatı altında toplar. Uygulamanın ana giriş noktasıdır.
    """
    st.set_page_config(layout="wide")
    st.title("🧠 Otonom Kod Mimarı: Yenilikçi Yetenek Geliştirme")
    st.markdown("""
    Bu arayüz, `AgentCodeArchitect` sınıfının planlama, kod üretimi ve temizleme
    aşamalarını simüle ederek yeni yetenekler geliştirmesini gösterir.
    OpenAI, Google DeepMind ve Microsoft AI ilkeleriyle tasarlanmıştır.
    """)

    architect = AgentCodeArchitect()

    st.subheader("🤖 Otonom Kod Mimarı Aktif")

    # ----- Yeni İnternet Araştırma ve Doğrulama Modülü -----
    st.markdown("---")
    st.subheader("🌐 Çok Kaynaklı Güvenli Araştırma ve Doğrulama")
    research_query = st.text_input("Araştırmak istediğiniz konuyu veya kod kalıbını girin (örn: 'Python Async/Await'):", "Python Decorators")
    
    if st.button("Araştır ve Doğrula", help="Çok kaynaklı araştırma yaparak güvenilir bilgi sentezler."):
        with st.spinner(f"'{research_query}' için çok kaynaklı araştırma yapılıyor..."):
            research_results = architect.guvenli_arastirma_ve_dogrulama(research_query)
            
            st.markdown("### 🔍 Araştırma Sonuçları:")
            if research_results["status"] == "Success":
                st.success("🎉 Başarıyla Doğrulanmış Bilgi Sentezlendi!")
                st.markdown("---")
                st.subheader("✨ Sentezlenmiş Güvenilir Özet:")
                st.write(research_results["reliable_summary"])
                st.markdown("---")
                
                if research_results["common_points"]:
                    st.subheader("✅ Tespit Edilen Ortak Noktalar (Yüksek Güvenilirlik):")
                    for point in research_results["common_points"]:
                        st.markdown(f"- **`{point['phrase']}`** (Kaynak Sayısı: {point['reliability_score']}, Kaynaklar: {', '.join(point['sources'])})")
                else:
                    st.info("Ortak güvenilir nokta bulunamadı.")

                if research_results["conflicting_points"]:
                    st.subheader("⚠️ Potansiyel Çelişkili veya Düşük Güvenilirlikli Bilgiler:")
                    for point in research_results["conflicting_points"]:
                        st.markdown(f"- **`{point['phrase']}`** (Kaynak Sayısı: {point['reliability_score']}, Kaynaklar: {', '.join(point['sources'])})")
                else:
                    st.info("Çelişkili veya düşük güvenilirlikli bilgi tespit edilmedi.")

                st.markdown("---")
                st.expander("Tüm Ham Araştırma Verilerini Göster", expanded=False).json(research_results["raw_findings"])
            else:
                st.error(f"Araştırma hatası: {research_results['reliable_summary']}")

    st.markdown("---")

    # ----- Mevcut Kod Üretim Modülü -----
    user_input = st.text_area("Yeni bir yetenek isteği girin (örn: 'kullanıcıya özel bir karşılama mesajı gösteren bir fonksiyon'):",
                               "iki sayıyı toplayan bir fonksiyon oluştur", height=100)

    if st.button("Kodu Üret ve Rafine Et", help="Planlama, kod üretimi ve temizlik aşamalarını çalıştırır."):
        with st.spinner("İstek işleniyor..."):
            try:
                result_code = architect.generate_and_refine_code(user_input)
                st.subheader("Üretilen ve Rafine Edilen Kod:")
                st.code(result_code, language="python")

                st.subheader("Üretilen Kodun Çalıştırılması (Simülasyon):")
                st.info("Üretilen kodu doğrudan `beyin.py` içerisinde `exec` ile çalıştırmak güvenlik riski taşıdığından, "
                        "burada sadece bir simülasyon ve örnek çağrı gösterilmektedir. "
                        "Gerçek entegrasyon `yetenekler.py` gibi güvenli bir ortamda yapılmalıdır.")
                
                match = re.search(r"def (\w+)\(", result_code)
                if match:
                    func_name = match.group(1)
                    st.markdown(f"**Üretilen fonksiyon adı:** `{func_name}`")
                    
                    st.markdown("##### Örnek Çağrılar:")
                    st.code(f"{func_name}('test verisi', param='değer')", language="python")
                    st.code(f"{func_name}(10, 20)", language="python")
                    st.code(f"{func_name}('hata_oluştur', param='değer')", language="python")
                else:
                    st.warning("Üretilen kod içinde tanımlı bir Python fonksiyonu bulunamadı.")
            except Exception as e:
                st.error(f"🚨 Ana yetenek üretim sürecinde beklenmeyen bir hata oluştu: {e}")
                st.code(traceback.format_exc())

    if 'architect_history_display' not in st.session_state:
        st.session_state.architect_history_display = False

    if st.button("Üretilen Kod Geçmişini Göster/Gizle", key="toggle_history"):
        st.session_state.architect_history_display = not st.session_state.architect_history_display

    if st.session_state.architect_history_display:
        st.subheader("Üretilen Kod Geçmişi:")
        if st.session_state.code_history:
            for i, entry in enumerate(st.session_state.code_history):
                st.expander(f"İstek {i+1}: {entry['request']}", expanded=False).code(entry['code'], language="python")
        else:
            st.info("Henüz üretilmiş kod yok.")

if __name__ == "__main__":
    ana_yetenekler()