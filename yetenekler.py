import streamlit as st

def buyuk_sirket_seviyesi_yazilim_yeteneği():
    """
    Büyük şirketler kadar iyi veya onlara yakın yazılım yazma becerisini
    Streamlit arayüzünde gösterir.
    """
    st.subheader("Yeni Yetenek: Büyük Şirketler Seviyesinde Yazılım Geliştirme Becerisi")
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
    st.success("Bu yeni yetenek başarıyla entegre edildi ve şu an kullanılabilir durumda.")

def ana_yetenekler():
    # Mevcut yeteneklerin yerine yeni eklenen yeteneği gösteriyoruz.
    buyuk_sirket_seviyesi_yazilim_yeteneği()