import streamlit as st

st.title("🚀 Word Count Application 🚀")
textInput = st.text_area("Input your Paragraph here")

if st.button("Count Words"):
    words = textInput.lower().split()
    # masing masing kata dipisah menggunakan split()
    # lalu dihitung menggunakan len()
    # disimpan di dalam dictionary
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
    st.subheader("word total")
    st.write(counts)

    st.bar_chart(counts)
    