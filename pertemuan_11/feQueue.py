from queue import Queue
from gtts import gTTS
from ipython.display import Audio
import streamlit as st

st.title("Queue Visualizer")
def generate_audio(text):
    tts = gTTS(text=text, lang='en')
    tts.save("audio.mp3")
    return Audio("audio.mp3", autoplay=True)

if 'queue' not in st.session_state:
    st.session_state.queue = Queue()
    st.session_state.counter = 1

st.header("halaman depan")

if st.button("Tambah pasien"):
    st.session_state.queue.enqueue(f"Data {st.session_state.counter}")
    st.session_state.counter += 1
    
