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
