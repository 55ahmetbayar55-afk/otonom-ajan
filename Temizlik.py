import streamlit as st
import os
import json

def ana_yetenekler():
    st.subheader("🧹 Master Temizlik ve Sistem Resetleme Merkezi")
    st.markdown("Bu modül, ajanınızın geçmişte biriken tüm kalabalık, hatalı veya işlevsiz kodlarını ve gereksiz hafıza kalıntılarını **sıfırlamak** ve sistemi en baştan tertemiz, optimize edilmiş devasa bir mimariyle başlatmak için tasarlanmıştır.")

    # Hafıza dosyasını sıfırlama fonksiyonu
    def hafizayi_komple_sifirla():
        bos_hafiza = {
            "genel_kurallar": ["Sistem tamamen sıfırlandı ve en güncel temiz mimariyle yapılandırıldı."],
            "ogrenilen_stratejiler": ["Temiz kod yazma ve legacy (eski) kod bloklarından arınma prensibi aktif."]
        }
        with open("ajan_hafizasi.json", "w", encoding="utf-8") as f:
            json.dump(bos_hafiza, f, ensure_ascii=False, indent=4)

    # Yetenekler dosyasını sıfırlama/başlangıç haline getirme fonksiyonu
    def yetenekleri_sifirla():
        temiz_kod = '''import streamlit as st

def ana_yetenekler():
    st.success("🚀 Sistem başarıyla sıfırlandı ve tertemiz bir sayfayla yeniden başlatıldı!")
    st.info("Artık bu ekrandan ajanınıza yepyeni, optimize edilmiş ve hatasız yetenekler öğretebilirsiniz.")
    
    with st.expander("✨ Sistem Durumu"):
        st.markdown("- **Eski Çöpler:** Tamamen temizlendi.\\n- **Hafıza:** Sıfırlandı.\\n- **Altyapı:** En güncel Streamlit bileşenlerine (st.rerun, sekmeler, expander) göre optimize edildi.")
'''
        with open("yetenekler.py", "w", encoding="utf-8") as f:
            f.write(temiz_kod)

    # Arayüz tasarımı
    col1, col2 = st.columns(2)

    with col1:
        st.warning("⚠️ **Dikkat:** Bu işlem tüm eski yetenek kodlarını silerek dosyayı varsayılan temiz duruma getirir.")
        if st.button("🗑️ Eski Yetenekleri Kalıcı Olarak Temizle", use_container_width=True):
            yetenekleri_sifirla()
            st.success("✅ Yetenekler dosyası başarıyla temizlendi!")
            st.rerun()

    with col2:
        st.warning("⚠️ **Dikkat:** Bu işlem `ajan_hafizasi.json` dosyasındaki tüm eski kuralları siler.")
        if st.button("🧹 Hafızayı Sıfırla ve Yeniden Başlat", use_container_width=True):
            hafizayi_komple_sifirla()
            st.success("✅ Hafıza başarıyla sıfırlandı!")
            st.rerun()

    st.markdown("---")
    st.error("🚨 **KOMPLE SİSTEM SIFIRLAMA (HARD RESET)**")
    st.markdown("Aşağıdaki butona bastığınızda hem hafıza hem de yetenekler dosyası aynı anda tamamen sıfırlanacak ve sistem ilk günkü tertemiz haline dönecektir.")
    
    if st.button("💥 TÜM SİSTEMİ SIFIRLA VE YENİDEN BAŞLAT", type="primary", use_container_width=True):
        yetenekleri_sifirla()
        hafizayi_komple_sifirla()
        st.success("🎉 Harika! Sistemdeki tüm eski yükler, çöpler ve kalıntılar tamamen temizlendi. Sayfa yenileniyor...")
        st.rerun()
