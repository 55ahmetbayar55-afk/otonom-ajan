import streamlit as st
import os
from github import Github, UnknownObjectException
from beyin import yeni_yetenek_yaz

st.set_page_config(page_title="Tam Otonom Ajan", page_icon="⚡", layout="wide")

# Eğer yetenekler.py yoksa, geçici varsayılan oluştur
if not os.path.exists("yetenekler.py"):
    with open("yetenekler.py", "w", encoding="utf-8") as f:
        f.write("# Ajanın otomatik yazdığı yetenekler buraya eklenecek\nimport streamlit as st\n\ndef ana_yetenekler():\n    st.info('Henüz yeni bir yetenek eklenmedi.')\n")

try:
    from yetenekler import ana_yetenekler
except ImportError:
    def ana_yetenekler():
        st.info("Henüz yeni bir yetenek yüklenmedi.")

st.title("⚡ Tam Otonom Kendi Kendini Kodlayan Ajan")
st.markdown("Ajan senden görevi alır, araştırır, kodu yazar ve **otomatik olarak GitHub'a yükleyerek kendini günceller.**")

with st.sidebar:
    st.header("🔑 Güvenlik ve API'ler")
    api_key = st.text_input("Gemini API Key", type="password")
    github_token = st.text_input("GitHub Access Token (Gerekli!)", type="password")
    repo_adi = st.text_input("GitHub Repo Adı", value="otonom-ajan", help="Örn: kullanici_adin/otonom-ajan")

st.divider()

# Mevcut Yetenekler
st.header("🛠️ Ajanın Mevcut Yetenekleri")
ana_yetenekler()

st.divider()

# Yeni Yetenek Ekleme Modülü (Evrim)
st.header("🧬 Ajana Yeni Bir Yetenek Öğret")
istek = st.text_input("Ajanın kendi koduna ne eklemesini istiyorsun?", placeholder="Örn: İnternetten anlık hava durumunu çeken bir modül yaz...")

if st.button("🚀 Otonom Evrimi Başlat", type="primary"):
    if not api_key or not github_token or not repo_adi:
        st.error("⚠️ Lütfen sol menüden API Key, GitHub Token ve Repo Adı bilgilerini eksiksiz girin.")
    else:
        with st.status("Ajan evrim sürecini başlattı...", expanded=True) as durum:
            try:
                st.write("1. İnternet araştırılıyor ve yeni Python kodu sentezleniyor...")
                if os.path.exists("yetenekler.py"):
                    with open("yetenekler.py", "r", encoding="utf-8") as f:
                        mevcut_kod = f.read()
                else:
                    mevcut_kod = ""
                
                yeni_kod = yeni_yetenek_yaz(api_key, istek, mevcut_kod)
                st.write("2. Kod başarıyla yazıldı! GitHub'a otomatik push ediliyor...")
                
                # Github'a Bağlan
                g = Github(github_token)
                repo = g.get_user().get_repo(repo_adi.split("/")[-1])
                
                # Dosya GitHub'da varsa güncelle, yoksa sıfırdan oluştur!
                try:
                    contents = repo.get_contents("yetenekler.py")
                    repo.update_file(contents.path, f"Otonom Güncelleme: {istek}", yeni_kod, contents.sha)
                except Exception:
                    repo.create_file("yetenekler.py", f"Otonom Oluşturma: {istek}", yeni_kod)

                durum.update(label="✅ Sistem Başarıyla Evrimleşti! Uygulama birazdan kendini yeniden başlatacak.", state="complete")
                st.balloons()
                
            except Exception as e:
                durum.update(label="Evrim sırasında kritik hata!", state="error")
                st.error(f"Hata detayı: {e}")
