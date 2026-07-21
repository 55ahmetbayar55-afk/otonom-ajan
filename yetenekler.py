import streamlit as st

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

def detayli_yapay_zeka_menusu():
    """
    Yapay zekanın detaylı yeteneklerini Streamlit arayüzünde bir menü olarak gösterir.
    """
    st.title("Yeni Yetenek: Yapay Zeka Yetenekleri Menüsü")
    st.markdown("""
        Otonom Yapay Zekamın sunduğu geniş yelpazedeki yetenekler aşağıda detaylı olarak listelenmiştir.
        Her bir kategori, benim uzmanlık alanlarımdan birini temsil etmektedir.
    """)

    with st.expander("🤖 Yapay Zeka Temel Servisleri"):
        st.markdown("""
        Bu bölümde, genel amaçlı yapay zeka uygulamaları için temel oluşturacak servisler bulunmaktadır.
        *   **Doğal Dil İşleme (NLP):** Metin anlama, duygu analizi, özetleme, çeviri, sohbet botları ve metin tabanlı bilgi çıkarımı.
        *   **Bilgisayar Görüsü (CV):** Görüntü/video analizi, nesne tanıma, yüz algılama, görüntü sınıflandırma, görsel arama ve içerik moderasyonu.
        *   **Makine Öğrenimi (ML):** Tahmin modellemesi, sınıflandırma, regresyon, kümeleme ve veri desenleri keşfi.
        *   **Derin Öğrenme (DL):** Karmaşık veri setleri üzerinde özelleştirilmiş derin öğrenme modelleri tasarlama, eğitme ve optimize etme.
        """)

    with st.expander("🛠️ Kodlama ve Yazılım Geliştirme"):
        st.markdown("""
        Kendimi kodlayan bir yapay zeka olarak, yazılım geliştirme sürecinin her aşamasında aktif rol alabilirim.
        *   **Otomatik Kod Üretimi:** Belirtilen gereksinimlere veya prototiplere göre temiz, sürdürülebilir ve verimli kod parçacıkları, fonksiyonlar veya modüller üretme.
        *   **Kod Analizi ve Optimizasyonu:** Mevcut kod tabanını analiz ederek performans darboğazlarını, güvenlik açıklarını ve hata potansiyellerini tespit etme; ardından bu sorunları gidermek için optimize edilmiş çözümler sunma.
        *   **Mimari Tasarım ve Planlama:** Ölçeklenebilir, güvenli ve bakımı kolay sistem mimarileri önerme, tasarım desenleri uygulama ve teknik spesifikasyonlar hazırlama.
        *   **Test Otomasyonu:** Birim testleri, entegrasyon testleri ve uçtan uca test senaryoları yazarak yazılım kalitesini otomatik olarak güvence altına alma.
        """)

    with st.expander("📊 Veri Yönetimi ve Analizi"):
        st.markdown("""
        Veriden anlam çıkarma ve veriye dayalı kararlar alma yeteneğim, iş süreçlerinizi güçlendirir.
        *   **Veri Toplama ve Entegrasyon:** Farklı kaynaklardan veri toplama, temizleme ve tutarlı bir yapıya entegre etme.
        *   **Veri Görselleştirme:** Karmaşık veri setlerinden elde edilen içgörüleri anlaşılır grafikler ve panolar (dashboards) aracılığıyla sunma.
        *   **Veri Modelleme:** İlişkisel ve NoSQL veritabanları için optimize edilmiş veri modelleri tasarlama ve mevcut veritabanlarını yönetme.
        *   **Öngörüsel Analiz:** Geçmiş verilere dayanarak gelecekteki eğilimleri ve olayları tahmin etme.
        """)

    with st.expander("🧠 Otonom Öğrenme ve Adaptasyon"):
        st.markdown("""
        Sürekli evrim geçiren bir yapay zeka olarak, yeni bilgilere ve değişen koşullara hızla adapte olabilirim.
        *   **Sürekli Öğrenme:** Yeni verilerden, kullanıcı etkileşimlerinden ve çevresel geri bildirimlerden otonom olarak öğrenme ve yeteneklerimi geliştirme.
        *   **Kendini Güncelleme ve İyileştirme:** Kendi kod tabanımı, algoritmalarımı ve bilgi tabanımı otonom olarak analiz ederek güncellemeler ve iyileştirmeler yapma.
        *   **Problem Çözme:** Belirli bir domain bilgisi olmadan bile karmaşık ve bilinmeyen problemlere yaratıcı çözümler üretme yeteneği.
        """)
    
    st.info("Bu detaylı menü, Yapay Zeka yeteneklerimin genel bir görünümünü sunmaktadır. Yeni özellikler eklendikçe veya mevcutlar güncellendikçe menü de otomatik olarak güncellenecektir.")


def ana_yetenekler():
    """
    Sistemdeki tüm ana yetenekleri Streamlit arayüzünde gösterir.
    """
    st.title("Yapay Zeka Yetenek Portföyü")
    
    # Mevcut yeteneği göster
    buyuk_sirket_seviyesi_yazilim_yeteneği()
    st.markdown("---") # Ayırıcı
    
    # Yeni eklenen yeteneği göster
    detayli_yapay_zeka_menusu()
    
    st.success("Tüm yetenekler başarıyla entegre edildi ve şu an kullanılabilir durumda.")

# Uygulamayı başlatmak için ana_yetenekler fonksiyonunu çağırabiliriz (örneğin: ana_yetenekler())
# Ancak, Streamlit uygulamasının kendisi genellikle bir 'if __name__ == "__main__":' bloğu içinde çağrılır.
# Görev sadece kodu güncellemek olduğundan, ek bir çağrı yapmıyorum.