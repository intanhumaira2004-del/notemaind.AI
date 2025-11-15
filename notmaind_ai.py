import pandas as pd
import streamlit as st

# Baca data Excel
notes_df = pd.read_excel("notes.xlsx")
users_df = pd.read_excel("users.xlsx")

st.title("NoteMind AI - Prototype")
st.write("Selamat datang di NoteMind AI!")

# Input materi catatan
user_input = st.text_area("Masukkan materi catatanmu:")
if st.button("Generate Note"):
    # Simulasi ringkasan
    st.write(user_input[:100] + "...")
    # Simpan ke Excel
    new_note = pd.DataFrame([[len(notes_df)+1, "Catatan Baru", user_input[:100]+"..."]],
                            columns=["id","judul","isi"])
    notes_df = pd.concat([notes_df, new_note], ignore_index=True)
    notes_df.to_excel("notes.xlsx", index=False)
