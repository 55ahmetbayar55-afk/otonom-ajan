import streamlit as st
import json
import os

def ana_yetenekler():
    st.subheader("🌐 Otonom Ajan Kontrol Paneli")
    st.markdown("Eski ve çakışan tüm kalıntılar temizlendi. Sistem artık tek bir modern arayüz üzerinden çalışıyor.")

    # Her şeyi tertemiz 3 ana sekme altında topluyoruz (Eski-yeni çakışması yok)
    sekme_mimari, sekme_hafiza, sekme_temizlik = st.tabs([
        "🧬 Otonom Kod Mimarı", 
        "🧠 Kalıcı Hafıza", 
        "🧹 Sistem Temizliği"
    ])

    # --- 1. SEKME: OTONOM KOD MİMARI (Yetenek Geliştirme) ---
    with sekme_mimari:
        st.markdown("### 🚀 Yenilikçi Yetenek Geliştirme")
        st.markdown("Ajanına yeni bir özellik kazandırmak için komutunu gir ve evrimi başlat.")
        
        yetenek_istegi = st.text_area(
            "Ajanın koduna ne eklemesini istiyorsun?", 
            placeholder="Örn: İnternetten veri çeken bir fonksiyon ekle...",
            key="yetenek_giris_kutusu_tekil"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚡ Kodu Üret ve Rafine Et", use_container_width=True, key="kod_uret_btn"):
                if yetenek_istegi:
                    st.success(f"'{yetenek_istegi}' için evrim süreci simüle edildi.")
                else:
                    st.warning("Lütfen bir istek girin.")
                    
        with col2:
            if st.button("📜 Geçmişi Göster", use_container_width=True, key="gecmis_btn"):
                st.info("Üretilen kod geçmişi burada listelenir.")

    # --- 2. SEKME: KALICI HAFIZA ---
    with sekme_hafiza:
        st.markdown("### 📂 JSON Hafıza Yönetimi")
        hafiza_dosyasi = "ajan_hafizasi.json"
        
        if os.path.exists(hafiza_dosyasi):
            with open(hafiza_dosyasi, "r", encoding="utf-8") as f:
                try:
                    hafiza_verisi = json.load(f)
                    st.json(hafiza_verisi)
                except:
                    st.warning("Hafıza dosyası okunamadı veya boş.")
        else:
            st.info("Henüz kayıtlı bir hafıza dosyası yok.")
            
        with st.expander("➕ Hafızaya Yeni Kural Ekle"):
            yeni_kural = st.text_input("Aklında tutması gereken kural:", key="hafiza_kural_input_tekil")
            if st.button("💾 Kaydet", key="hafiza_kaydet_btn_tekil"):
                if yeni_kural:
                    veri = {"genel_kurallar": [], "ogrenilen_stratejiler": []}
                    if os.path.exists(hafiza_dosyasi):
                        with open(hafiza_dosyasi, "r", encoding="utf-8") as f:
                            try:
                                veri = json.load(f)
                            except:
                                pass
                    veri.setdefault("genel_kurallar", []).append(yeni_kural)
                    with open(hafiza_dosyasi, "w", encoding="utf-8") as f:
                        json.dump(veri, f, ensure_ascii=False, indent=4)
                    st.success("Kural başarıyla hafızaya eklendi!")
                    st.rerun()

    # --- 3. SEKME: SİSTEM TEMİZLİĞİ ---
    with sekme_temizlik:
        st.markdown("### 🧹 Sistem Temizliği ve Reset Merkezi")
        st.warning("Eski veya çakışan tüm verileri buradan sıfırlayabilirsiniz.")

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🗑️ Yetenekleri Sıfırla", use_container_width=True, key="temizlik_yet_btn"):
                temiz_kod = 'import streamlit as st\n\ndef ana_yetenekler():\n    st.success("Yetenekler başarıyla sıfırlandı!")'
                with open("yetenekler.py", "w", encoding="utf-8") as f:
                    f.write(temiz_kod)
                st.success("Yetenekler sıfırlandı!")
                st.rerun()
        with c2:
            if st.button("🧹 Hafızayı Sıfırla", use_container_width=True, key="temizlik_haf_btn"):
                bos_hafiza = {"genel_kurallar": [], "ogrenilen_stratejiler": []}
                with open("ajan_hafizasi.json", "w", encoding="utf-8") as f:
                    json.dump(bos_hafiza, f, ensure_ascii=False, indent=4)
                st.success("Hafıza sıfırlandı!")
                st.rerun()

        if st.button("💥 TÜM SİSTEMİ HARD RESET AT", type="primary", use_container_width=True, key="hard_reset_btn"):
            temiz_kod = 'import streamlit as st\n\ndef ana_yetenekler():\n    st.success("Sistem tamamen sıfırlandı!")'
            with open("yetenekler.py", "w", encoding="utf-8") as f:
                f.write(temiz_kod)
            bos_hafiza = {"genel_kurallar": [], "ogrenilen_stratejiler": []}
            with open("ajan_hafizasi.json", "w", encoding="utf-8") as f:
                json.dump(bos_hafiza, f, ensure_ascii=False, indent=4)
            st.success("Komple sistem resetlendi! Sayfa yenileniyor...")
            st.rerun()
