import streamlit as st
from gtts import gTTS
import myqueue

# =========================
# TITLE
# =========================

st.title("🏥 Visualisasi Antrian Rumah Sakit")

# =========================
# SESSION STATE
# =========================

if 'queue' not in st.session_state:
    st.session_state.queue = myqueue.Queue()

# =========================
# INPUT PASIEN
# =========================

st.header("Halaman Depan")

pasien = st.text_input("Masukkan Nama Pasien")

if st.button("Tambah Pasien"):

    if pasien.strip() != "":
        st.session_state.queue.enqueue(pasien)
        st.success(f"{pasien} berhasil ditambahkan")
    else:
        st.warning("Nama pasien tidak boleh kosong")

# =========================
# MENAMPILKAN ANTRIAN
# =========================

st.header("Antrian Saat Ini")

if not st.session_state.queue.is_empty():

    st.write(f"Jumlah Antrian: {st.session_state.queue.size}")

    daftar = st.session_state.queue.display()

    nomor = 1

    for nama in daftar:
        st.write(f"{nomor}. {nama}")
        nomor += 1

else:
    st.info("Belum ada antrian")

# =========================
# PANGGIL PASIEN
# =========================

if st.button("Panggil Pasien Berikutnya"):

    if not st.session_state.queue.is_empty():

        nama = st.session_state.queue.peek()

        teks = f"Pasien atas nama {nama}, silahkan menuju ruang dokter"

        tts = gTTS(text=teks, lang='id')

        tts.save("audio.mp3")

        st.audio("audio.mp3", autoplay=True)

        st.session_state.queue.dequeue()

        st.success(f"Memanggil {nama}")

    else:
        st.warning("Antrian kosong")