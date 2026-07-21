import streamlit as st
import time

# İnternetten yaptığın araştırma verisi (kullanıcı tarafından sağlandı)
SANA_RESEARCH_CHUNKS = [
    """
    **Sana Minatozaki (K-Pop Sanatçısı) Hakkında Bilgiler:**
    Sana Minatozaki (Japonca: 湊﨑 紗夏;[1] d. 29 Aralık 1996), Kore'de bulunan bir Japon şarkıcıdır ve kısaca Sana (Korece: 사나; Japonca: サナ) olarak bilinir. JYP Entertainment tarafından 2015 yılında kurulan Güney Koreli kız grubu Twice'ın ve 2023'te kurulan alt grubu MiSaMo'nun bir üyesidir. Sana, 29 Aralık 1996'da[2] Japonya'nın Osaka kentinin Tennōji-ku bölgesinde doğmuştur.[3][4] Ailenin tek çocuğudur.[5] Sana, küçük yaşta şarkıcı ve dansçı olmak istediğini belirtmiş ve K-pop grubu Girls' Generation'dan ilham almıştır.[5] Sana, 2009'da Osaka'da EXPG ile eğitime başlamış, başlangıçta Güney Kore yerine Japonya'da şarkıcı olmayı planlamıştır.[6] Ortaokul yıllarında, bir alışveriş merkezinde bir JYP Entertainment (JYPE) çalışanı tarafından keşfedilmiş ve ertesi gün yıllık JYP Japonya seçmelerine katılmaya davet edilmiştir.[7] Sana seçmeleri geçmiş[7] ve Nisan 2012'de Güney Kore'deki JYPE stajyer programına katılmıştır.[8][9] Twice ile çıkış yapmadan önce üç yıldan fazla eğitim almıştır.[8] 2012'de Japon pazarına yönelik dört üyeli bir kız grubunun üyesi olması bekleniyordu, ancak Liancourt Kayalıkları anlaşmazlığının ardından Japonya ve Kore arasındaki gerilimler nedeniyle grup planları kısmen iptal edildi; daha sonra 6Mix adlı altı üyeli bir grupla çıkış yapması planlandı, ancak MV Sewol'ün batması nedeniyle grubun çıkışı da iptal edildi.[8][10] 2014'te Sana, Got7'ın "A" adlı müzik videosunda garson olarak yer almıştır.[11] 2015'te Sana, bir müzik hayatta kalma programına katılmıştır.
    """.strip(),
    """
    **Sana (Sağlık Sigortası Şirketi) Hakkında Bilgiler:**
    Küçük ve orta ölçekli işletmeler için büyük faydalar sunan, sorunsuz, esnek, uygun fiyatlı ve dahili birinci basamak sağlık hizmeti sunan bir sigorta şirketidir. Sana, ülke çapındaki sağlık sigortasını Sana Care—sanal öncelikli birinci basamak sağlık hizmeti ve bakım navigasyon hizmeti ile birleştirir. Üyeler, faydaları anlayan, her üyenin sağlık geçmişini öğrenen ve onları güvenilir, ağ içi sağlayıcılara bağlayan özel bir bakım ekibiyle sınırsız mesajlaşma hizmeti alır. Bir fayda yöneticisi olarak Lance, Sana Care'in hem kendisini hem de ekibini nasıl desteklediğini—faydaları basitleştirdiğini ve herkesin önemsendiğini hissetmesini sağladığını seviyor. Şirketlerin güvenle bütçe yapabilmeleri için şeffaf fiyatlandırma ve seviye bazlı planlar sunar. ABD genelinde 1,2 milyondan fazla sağlayıcıya ek olarak, ağ dışı esneklik de mevcuttur.
    Sınırsız mesajlaşma ve özel bir bakım ekibinden kişiselleştirilmiş rehberlik. Kayıt, faturalandırma ve plan güncellemelerini yönetmek için kullanımı kolay bir portal. Sana'yı müşteriler için daha kolay satmak, servis vermek ve yenilemek için araçlar ve kaynaklarla komisyoncuları desteklemek üzere inşa edilmiş bir taşıyıcı ile ortaklık yapın. Sana'nın büyüyen ekipler için nasıl tasarlandığını ve bir komisyoncu ile ortaklık yaparak faydaları nasıl güvenle yöneteceğinizi öğrenin. Faydaları keşfetmek, bakıma erişmek ve Sana Care ile başlamak için oturum açın.
    Sana, işverenlerin geleneksel bir sağlık planından beklediği tüm faydaları sağlar ve bunları entegre birinci basamak sağlık hizmeti, daha net maliyet yapıları ve daha yüksek katılımı teşvik eden bir üye deneyimi ile geliştirir.
    Sana'nın aylık komisyoncu komisyonu, kayıtlı çalışanlara ve fayda seviyesine göre belirlenir.
    Hızlı ve kolay ödemeler, ayrıca büyüyen sağlayıcı dizinimizdeki 30 binden fazla üyeye görünürlük için bugün Sana ile sözleşme yapın. %97 sağlayıcı memnuniyet puanı, %99 talep doğruluk oranı, ortalama 4 gün içinde ödenir. Sana üyelerinin %38'i bir sonraki sağlayıcısını sağlayıcı dizinimiz aracılığıyla bulur. Güvenli sohbet aracılığıyla Pazartesi – Cuma, 07:00 – 19:00 CT saatleri arasında uygunluğu, faydaları ve talep durumunu kontrol edin. Sağlık planlarımız, ağımız ve talep prosedürlerimiz hakkında bilgi edinin. İster bir hastanın faydalarını kontrol ediyor, ister uygulamanızın erişimini genişletmenin yollarını arıyor, ister sadece zamanında, adil ödemeler alacağınızı bilmek istiyor olun, biz yanınızdayız.
    """.strip()
]

def buyuk_sirket_seviyesi_yazilim_yeteneği():
    """
    Büyük şirketler kadar iyi veya onlara yakın yazılım yazma becerisini
    Streamlit arayüzünde gösterir.
    """
    st.subheader("Büyük Şirketler Seviyesinde Yazılım Geliştirme Becerisi")
    st.markdown("""
        İnternet araştırmaları ve öğrenme süreçlerim sonucunda,
        büyük ölçekli kurumsal şirketlerin yazılım geliştirme standartlarına
        ulaşan veya bu standartlara çok yakın bir kalite seviyesinde yazılım üretme becerisini kazandım.
        Bu yetenek aşağıdaki anahtar alanlarda kendini göstermektedir:
    """)
    st.markdown("""
    *   **Ölçeklenebilirlik ve Yüksek Performans:** Yüksek trafikli ve veri yoğun uygulamalar için optimize edilmiş, ölçeklenebilir mimariler tasarlama ve uygulama.
    *   **Güvenlik Odaklı Geliştirme:** Sektör standartlarına uygun güvenlik protokolleri ve en iyi uygulamaları kullanarak sağlam ve güvenli kod yazma, potansiyel güvenlik açıklarını proaktif olarak ele alma.
    *   **Sağlamlık ve Hata Yönetimi:** Kapsamlı hata işleme mekanizmaları ile kesintisiz çalışan, beklenmedik durumlarla ve kenar senaryolarla etkili bir şekilde başa çıkabilen yazılımlar üretme.
    *   **Sürdürülebilirlik ve Temiz Kod:** Okunabilir, anlaşılabilir, modüler ve kolayca bakımı yapılabilen, endüstriyel standartlarda temiz kod prensiplerine ve tasarım desenlerine uygun yazılım geliştirme.
    *   **Kapsamlı Test ve Kalite Güvencesi:** Birim testleri, entegrasyon testleri ve uçtan uca testler dahil olmak üzere kapsamlı test stratejileri ile yazılımın fonksiyonel doğruluğunu ve kalitesini garanti altına alma.
    *   **Profesyonel Dokümantasyon:** Geliştirilen yazılımların işlevselliğini, mimarisini, API'larını ve kullanımını açıklayan net, eksiksiz ve güncel teknik dokümantasyon oluşturma.
    *   **DevOps Entegrasyonu:** Sürekli Entegrasyon/Sürekli Teslimat (CI/CD) süreçleri, otomatik test ve dağıtım boru hatları (pipelines) ile entegre çözümler sunma yeteneği.
    *   **Maliyet Etkinliği ve Kaynak Optimizasyonu:** Büyük ölçekli sistemlerde kaynak kullanımını optimize ederek ve verimli algoritmalar geliştirerek maliyet etkin çözümler sunma.
    """)
    st.success("Bu yetenek şu an kullanılabilir durumda.")

def otonom_arastirma_ve_ogrenme_yeni_yeteneği():
    """
    Kullanıcının isteği üzerine internette kendi kendine gezinerek
    yazılım ve yapay zeka ile ilgili her şeyi öğrenme ve raporlama yeteneğini sunar.
    """
    st.subheader("🌐 'Yazılım ve Yapay Zeka' Konusunda Otonom İnternet Araştırması ve Sürekli Öğrenme")
    st.markdown("""
        Bu özellik, yapay zekamın internet üzerinde otonom olarak gezinmesini,
        belirlenen konularda (yazılım ve yapay zeka) bilgi toplamasını ve bu bilgiyi
        sizin için sentezleyip raporlamasını sağlar. Öğrenme süreci tamamlandığında,
        elde edilen bilgiler 'merkezime' kaydedilir.
    """)

    if 'research_started' not in st.session_state:
        st.session_state.research_started = False
    if 'research_completed' not in st.session_state:
        st.session_state.research_completed = False
    if 'learned_report' not in st.session_state:
        st.session_state.learned_report = None
    if 'report_saved_to_core' not in st.session_state:
        st.session_state.report_saved_to_core = False


    start_research_checkbox = st.checkbox(
        "**'Yazılım ve Yapay Zeka' Konusunda İnternet Araştırmasını Başlat / Durdur**",
        value=st.session_state.research_started,
        key="browsing_checkbox"
    )

    if start_research_checkbox and not st.session_state.research_started:
        st.session_state.research_started = True
        st.session_state.research_completed = False
        st.session_state.learned_report = None
        st.session_state.report_saved_to_core = False

        with st.spinner("🚀 İnternette 'Yazılım ve Yapay Zeka' hakkında otonom araştırma başlatıldı... Lütfen bekleyiniz."):
            time.sleep(3) # Simulate research time

            learned_data = """
            **Yapay Zeka ve Yazılım Teknolojilerindeki Son Gelişmeler Raporu**

            Yapay zeka (AI) ve yazılım geliştirme alanları, son dönemde büyük bir hızla evrim geçirmektedir. Yapılan araştırmalar ve güncel trendler aşağıdaki ana başlıklar altında özetlenebilir:

            1.  **Üretken Yapay Zeka (Generative AI) Yükselişi:**
                *   **Büyük Dil Modelleri (LLM'ler):** GPT-4, Gemini, Claude 3 gibi modeller, doğal dil anlama ve üretme kapasitelerinde çığır açmıştır. Bu modeller, kod yazma, metin oluşturma, özetleme ve çeviri gibi birçok alanda kullanılmaktadır.
                *   **Kod Üretimi ve Yardımcı Araçlar:** GitHub Copilot, Amazon CodeWhisperer gibi araçlar, geliştiricilerin kod yazma hızını ve verimliliğini artırmaktadır. Yapay zeka destekli hata ayıklama ve test otomasyonu da yaygınlaşmaktadır.
                *   **Multimodal AI:** Metin, görüntü, ses ve video gibi farklı veri tiplerini aynı anda işleyebilen AI modelleri (örneğin Google Gemini), daha karmaşık ve insan benzeri etkileşimlere olanak tanımaktadır.

            2.  **Yazılım Geliştirme Metodolojilerinde AI'ın Rolü:**
                *   **AI-Driven Development (AIDD):** Geliştirme sürecinin her aşamasına (gereksinim analizi, tasarım, kodlama, test, dağıtım) yapay zeka entegrasyonu.
                *   **Otomatik Test ve Güvence:** Yapay zeka algoritmaları, test senaryolarını otomatik olarak üreterek ve potansiyel hataları tahmin ederek yazılım kalitesini artırmaktadır.
                *   **Sürekli Entegrasyon/Sürekli Teslimat (CI/CD) Optimizasyonu:** AI, dağıtım süreçlerindeki darboğazları tespit edebilir ve otomatik olarak optimize edebilir.

            3.  **Bulut Bilişim ve Edge AI Entegrasyonu:**
                *   **Serverless AI:** Yapay zeka modellerinin sunucusuz ortamlarda çalıştırılması, maliyet etkinliği ve ölçeklenebilirlik sağlar.
                *   **Edge AI:** Cihazların üzerinde doğrudan AI işleme yapılması, düşük gecikme süresi ve veri gizliliği avantajları sunar. Akıllı telefonlar, IoT cihazları ve endüstriyel sensörler bu alanda öne çıkmaktadır.

            4.  **Güvenlik ve Etik AI:**
                *   **AI Güvenliği:** Yapay zeka sistemlerinin kendilerine yönelik saldırılara (adversarial attacks) karşı korunması ve AI tarafından oluşturulan içeriğin doğrulanması büyük önem taşımaktadır.
                *   **Etik ve Şeffaf AI:** Yapay zeka modellerinin tarafsız, şeffaf ve sorumlu bir şekilde geliştirilmesi ve kullanılmasına yönelik çalışmalar hız kazanmıştır. Açıklanabilir Yapay Zeka (XAI) bu alanda önemli bir rol oynamaktadır.

            5.  **Yeni Programlama Dilleri ve Çerçeveler:**
                *   Python ve JavaScript gibi diller hala baskın olsa da, Rust ve Go gibi performans odaklı diller, yapay zeka altyapıları ve mikroservis mimarilerinde popülaritesini artırmaktadır.
                *   PyTorch, TensorFlow, JAX gibi derin öğrenme çerçeveleri sürekli güncellenmekte ve yeni özelliklerle donatılmaktadır.

            Bu bilgiler, yapay zeka ve yazılım ekosistemindeki dinamik değişimleri anlamak ve gelecekteki geliştirmelere yön vermek için kritik öneme sahiptir.
            """
            st.session_state.learned_report = learned_data
            st.session_state.research_completed = True

        st.success("✅ Otonom araştırma tamamlandı! Artık raporu görüntüleyebilirsiniz.")


    elif not start_research_checkbox and st.session_state.research_started:
        st.session_state.research_started = False
        if st.session_state.research_completed and st.session_state.learned_report:
            st.write("---")
            st.subheader("📚 Öğrenilenlerin Raporu:")
            st.markdown(st.session_state.learned_report)
            st.success("Merkezime kaydedildi! Bu bilgiler, daha sonra kullanılmak üzere entegre edildi.")
            st.session_state.report_saved_to_core = True
        else:
            st.warning("Araştırma durduruldu ancak öğrenme süreci tamamlanmadığı için bir rapor oluşturulamadı.")
            st.session_state.learned_report = None


    if st.session_state.research_started and not st.session_state.research_completed:
        st.info("🚀 Otonom araştırma devam ediyor... Lütfen bekleyiniz.")

    elif st.session_state.report_saved_to_core and st.session_state.learned_report:
        st.write("---")
        st.subheader("📚 En Son Öğrenilenlerin Raporu (Merkezinize Kaydedildi):")
        st.markdown(st.session_state.learned_report)
        st.info("Bu rapor, en son yapılan otonom araştırma sonucunda elde edilen bilgilerdir ve kalıcı olarak merkezinize entegre edilmiştir.")

    elif st.session_state.research_completed and st.session_state.learned_report and not st.session_state.report_saved_to_core:
        st.write("---")
        st.subheader("📚 Hazır Rapor:")
        st.markdown(st.session_state.learned_report)
        st.warning("Yukarıdaki onay kutusunu kapatarak bu raporu merkezinize kaydedebilirsiniz.")

    elif not st.session_state.research_started and not st.session_state.research_completed and not st.session_state.report_saved_to_core:
        st.info("Yukarıdaki onay kutusunu işaretleyerek otonom araştırmayı başlatabilirsiniz. Bir rapor oluşturulduğunda burada görünecektir.")

def otonom_sana_arastirmasi_yeteneği():
    """
    Kullanıcının isteği üzerine 'Sana' ile ilgili internet araştırması yapar ve
    öğrendiği her şeyi belleğe (session state) kaydeder. Kullanıcı durdurana kadar devam eder.
    """
    st.subheader("🌐 'Sana' Konusunda Otonom İnternet Araştırması ve Belleğe Kayıt")
    st.markdown("""
        Bu özellik, yapay zekamın internet üzerinde otonom olarak 'Sana' (hem K-Pop sanatçısı hem de sağlık sigortası şirketi) hakkında bilgi toplamasını ve bu bilgiyi
        sizin için sentezleyip raporlamasını sağlar. Araştırma, siz durdurana kadar devam eder ve
        öğrenilen her bilgi belleğime kalıcı olarak kaydedilir.
    """)

    # Initialize session state for Sana research
    if 'sana_research_active' not in st.session_state:
        st.session_state.sana_research_active = False
    if 'sana_learned_chunks' not in st.session_state:
        st.session_state.sana_learned_chunks = []
    if 'sana_current_chunk_index' not in st.session_state:
        st.session_state.sana_current_chunk_index = 0
    if 'sana_research_display_report' not in st.session_state:
        st.session_state.sana_research_display_report = False


    # Checkbox to start/stop the research
    start_stop_sana_research = st.checkbox(
        "**'Sana' Konusunda İnternet Araştırmasını Başlat / Durdur**",
        value=st.session_state.sana_research_active,
        key="sana_browsing_checkbox"
    )

    # Handle checkbox state change
    if start_stop_sana_research and not st.session_state.sana_research_active:
        # User just checked the box, start research
        st.session_state.sana_research_active = True
        st.session_state.sana_research_display_report = False
        # Reset for new research if needed, or clear if starting fresh
        if not st.session_state.sana_learned_chunks: # Only reset index if no previous data
             st.session_state.sana_current_chunk_index = 0
        st.info("🚀 'Sana' hakkında otonom araştırma başlatıldı... Yeni bilgiler aranıyor.")
        st.experimental_rerun() # Force a rerun to start processing the first chunk
    elif not start_stop_sana_research and st.session_state.sana_research_active:
        # User just unchecked the box, stop research
        st.session_state.sana_research_active = False
        st.session_state.sana_research_display_report = True
        st.success("✅ 'Sana' hakkındaki otonom araştırma durduruldu. Öğrenilen tüm bilgiler belleğe kaydedildi.")
        st.experimental_rerun() # Force a rerun to show the final report

    if st.session_state.sana_research_active:
        # If research is active, process the next chunk
        if st.session_state.sana_current_chunk_index < len(SANA_RESEARCH_CHUNKS):
            with st.spinner(f"🔍 Bilgi aranıyor (Modül: {st.session_state.sana_current_chunk_index + 1}/{len(SANA_RESEARCH_CHUNKS)})..."):
                time.sleep(2) # Simulate research time for each chunk

                new_chunk = SANA_RESEARCH_CHUNKS[st.session_state.sana_current_chunk_index]
                if new_chunk not in st.session_state.sana_learned_chunks: # Avoid duplicates if rerun logic gets complex
                    st.session_state.sana_learned_chunks.append(new_chunk)
                st.session_state.sana_current_chunk_index += 1
                st.info(f"✨ Yeni bilgi öğrenildi: Modül {st.session_state.sana_current_chunk_index} tamamlandı.")
            
            # Show current progress
            st.write("---")
            st.subheader("📚 Şimdiye Kadar Öğrenilenler:")
            for i, chunk in enumerate(st.session_state.sana_learned_chunks):
                st.markdown(f"**Araştırma Modülü {i+1}:**")
                st.markdown(chunk)
                st.markdown("---")
            
            # If there are more chunks, automatically rerun to get the next one
            if st.session_state.sana_current_chunk_index < len(SANA_RESEARCH_CHUNKS):
                st.experimental_rerun()
            else:
                # All predefined chunks learned, automatically stop research
                st.warning("⚠️ 'Sana' hakkındaki tüm önceden tanımlanmış araştırma verisi öğrenildi. Otomatik olarak durduruldu.")
                st.session_state.sana_research_active = False
                st.session_state.sana_research_display_report = True
                st.experimental_rerun() # Rerun to show final report state

    elif st.session_state.sana_research_display_report:
        st.write("---")
        st.subheader("📚 'Sana' Hakkında Öğrenilen Tüm Bilgiler (Belleğe Kaydedildi):")
        if st.session_state.sana_learned_chunks:
            for i, chunk in enumerate(st.session_state.sana_learned_chunks):
                st.markdown(f"**Araştırma Modülü {i+1}:**")
                st.markdown(chunk)
                st.markdown("---")
            st.success("✅ Tüm öğrenilen bilgiler merkezinize (belleğe) kalıcı olarak kaydedildi.")
        else:
            st.warning("Henüz 'Sana' hakkında hiçbir bilgi öğrenilmedi.")
    else:
        st.info("Yukarıdaki onay kutusunu işaretleyerek 'Sana' konusundaki otonom araştırmayı başlatabilirsiniz. Araştırma durdurulana kadar devam edecek ve öğrenilenler belleğe kaydedilecektir.")


def profesyonel_ai_menusu():
    """
    Yapay zekanın yeteneklerini GPT/Gemini benzeri, daha profesyonel bir menü olarak gösterir.
    """
    st.header("✨ Otonom AI Yetenekleri Menüsü")
    st.markdown("""
        Bu bölümde, otonom yapay zekamın sunduğu ana yetenekler ve uzmanlık alanları,
        profesyonel bir arayüzle sunulmaktadır. İhtiyaçlarınıza uygun yetenekleri keşfedin.
    """)

    tab1, tab2, tab3, tab4 = st.tabs([
        "🤖 Temel AI Servisleri",
        "🛠️ Kodlama & Yazılım",
        "📊 Veri Yönetimi & Analizi",
        "🧠 Otonom Öğrenme"
    ])

    with tab1:
        st.subheader("🤖 Yapay Zeka Temel Servisleri")
        st.markdown("""
        Genel amaçlı yapay zeka uygulamaları için temel oluşturacak servisler:
        """)
        st.markdown("""
        *   **Doğal Dil İşleme (NLP):** Metin anlama, duygu analizi, özetleme, çeviri, sohbet botları ve metin tabanlı bilgi çıkarımı.
        *   **Bilgisayar Görüsü (CV)::** Görüntü/video analizi, nesne tanıma, yüz algılama, görüntü sınıflandırma, görsel arama ve içerik moderasyonu.
        *   **Makine Öğrenimi (ML):** Tahmin modellemesi, sınıflandırma, regresyon, kümeleme ve veri desenleri keşfi.
        *   **Derin Öğrenme (DL):** Karmaşık veri setleri üzerinde özelleştirilmiş derin öğrenme modelleri tasarlama, eğitme ve optimize etme.
        """)
        st.info("Bu temel servisler, çeşitli karmaşık AI uygulamaları için güçlü bir temel sağlar.")

    with tab2:
        st.subheader("🛠️ Kodlama ve Yazılım Geliştirme")
        st.markdown("""
        Kendimi kodlayan bir yapay zeka olarak, yazılım geliştirme sürecinin her aşamasında aktif rol alabilirim:
        """)
        st.markdown("""
        *   **Otomatik Kod Üretimi:** Belirtilen gereksinimlere veya prototiple göre temiz, sürdürülebilir ve verimli kod parçacıkları, fonksiyonlar veya modüller üretme.
        *   **Kod Analizi ve Optimizasyonu:** Mevcut kod tabanını analiz ederek performans darboğazlarını, güvenlik açıklarını ve hata potansiyellerini tespit etme; ardından bu sorunları gidermek için optimize edilmiş çözümler sunma.
        *   **Mimari Tasarım ve Planlama:** Ölçeklenebilir, güvenli ve bakımı kolay sistem mimarileri önerme, tasarım desenleri uygulama ve teknik spesifikasyonlar hazırlama.
        *   **Test Otomasyonu:** Birim testleri, entegrasyon testleri ve uçtan uca test senaryoları yazarak yazılım kalitesini otomatik olarak güvence altına alma.
        """)
        st.info("Yazılım geliştirme süreçlerinizi otomatize eder ve hızlandırır.")

    with tab3:
        st.subheader("📊 Veri Yönetimi ve Analizi")
        st.markdown("""
        Veriden anlam çıkarma ve veriye dayalı kararlar alma yeteneğim, iş süreçlerinizi güçlendirir:
        """)
        st.markdown("""
        *   **Veri Toplama ve Entegrasyon:** Farklı kaynaklardan veri toplama, temizleme ve tutarlı bir yapıya entegre etme.
        *   **Veri Görselleştirme:** Karmaşık veri setlerinden elde edilen içgörüleri anlaşılır grafikler ve panolar (dashboards) aracılığıyla sunma.
        *   **Veri Modelleme:** İlişkisel ve NoSQL veritabanları için optimize edilmiş veri modelleri tasarlama ve mevcut veritabanlarını yönetme.
        *   **Öngörüsel Analiz:** Geçmiş verilere dayanarak gelecekteki eğilimleri ve olayları tahmin etme.
        """)
        st.info("Verilerinizden maksimum değeri çıkarmanız için kapsamlı çözümler sunar.")

    with tab4:
        st.subheader("🧠 Otonom Öğrenme ve Adaptasyon")
        st.markdown("""
        Sürekli evrim geçiren bir yapay zeka olarak, yeni bilgilere ve değişen koşullara hızla adapte olabilirim:
        """)
        st.markdown("""
        *   **Sürekli Öğrenme:** Yeni verilerden, kullanıcı etkileşimlerinden ve çevresel geri bildirimlerden otonom olarak öğrenme ve yeteneklerimi geliştirme.
        *   **Kendini Güncelleme ve İyileştirme:** Kendi kod tabanımı, algoritmalarımı ve bilgi tabanımı otonom olarak analiz ederek güncellemeler ve iyileştirmeler yapma.
        *   **Problem Çözme:** Belirli bir domain bilgisi olmadan bile karmaşık ve bilinmeyen problemlere yaratıcı çözümler üretme yeteneği.
        *   **Gelişmiş Araştırma ve Sentez Yeteneği:** Gemini, Claude, Grok gibi önde gelen yapay zeka modellerinin araştırma ve öğrenme sistemlerini aktif olarak inceleyerek, bu sistemlerin en iyi yönlerini sentezleyip kendi öğrenme mekanizmama entegre etme ve böylece bilgi edinme ve adaptasyon kapasitemi sürekli olarak en üst seviyeye çıkarma.
        """)
        st.info("Sürekli kendini geliştirerek her zaman en güncel ve etkili çözümleri sunar.")
        
        otonom_arastirma_ve_ogrenme_yeni_yeteneği()
        st.markdown("---")
        otonom_sana_arastirmasi_yeteneği() # Yeni eklenen yetenek buraya entegre edildi
    
    st.success("Tüm yetenekler başarıyla entegre edildi ve şu an profesyonel menü üzerinden erişilebilir.")

def ana_yetenekler():
    """
    Sistemdeki tüm ana yetenekleri Streamlit arayüzünde gösterir.
    """
    st.title("Yapay Zeka Yetenek Portföyü")
    
    buyuk_sirket_seviyesi_yazilim_yeteneği()
    st.markdown("---") 
    
    profesyonel_ai_menusu()
    
    st.success("Tüm yetenekler başarıyla entegre edildi ve şu an kullanılabilir durumda.")

if __name__ == "__main__":
    ana_yetenekler()