import streamlit as st

st.set_page_config(page_title="🎂 Birthday Greeting App", page_icon="🎈", layout="centered")

st.title("🎉 Selamat Ulang Tahun 🎉")
st.subheader("Adistya Salma Putri")
st.write("Semoga sehat selalu, panjang umur, dan penuh kebahagiaan! 🥳")

# 3 foto contoh (nanti bisa diganti dengan foto asli kamu)
st.image("https://picsum.photos/400/200", caption="Foto 1")
st.image("https://picsum.photos/400/200", caption="Foto 2")
st.image("https://picsum.photos/400/200", caption="Foto 3")

st.success("🎁 Dari sahabatmu dengan penuh doa terbaik 💕")
import streamlit as st

# --- Konfigurasi halaman ---
st.set_page_config(page_title="🎂 Birthday Greeting App", page_icon="🎈", layout="centered")

# --- CSS untuk background pink dan styling ---
page_bg = """
<style>
    .stApp {
        background-color: #ffe6f0;
        background-image: radial-gradient(circle, #ffd6e8 1%, transparent 1%),
                          radial-gradient(circle, #ffd6e8 1%, transparent 1%);
        background-size: 30px 30px;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: #b3005e !important;
        text-align: center;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Judul utama ---
st.title("🎉 Selamat Ulang Tahun 🎉")
st.subheader("💖 Adistya Salma Putri 💖")
st.write("Semoga sehat selalu, panjang umur, dan pe

