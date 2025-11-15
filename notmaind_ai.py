import streamlit as st
import pandas as pd

st.title("NoteMind AI - MVP Prototype")
st.write("Selamat datang di NoteMind AI!")

# Baca Excel
try:
    notes_df = pd.read_excel("notes.xlsx")
except FileNotFoundError:
    notes_df = pd.DataFrame(columns=["id","judul","isi"])

try:
    users_df = pd.read_excel("users.xlsx")
except FileNotFoundError:
    users_df = pd.DataFrame(columns=["id","nama","email"])

# Input user
user_name = st.text_input("Masukkan nama Anda:")
user_email = st.text_input("Masukkan email Anda:")

if st.button("Daftar / Login"):
    if user_name and user_email:
        if not ((users_df['nama']==user_name) & (users_df['email']==user_email)).any():
            new_user = pd.DataFrame([[len(users_df)+1, user_name, user_email]], columns=["id","nama","email"])
            users_df = pd.concat([users_df, new_user], ignore_index=True)
            users_df.to_excel("users.xlsx", index=False)
        st.success(f"Selamat datang, {user_name}!")

# Input catatan
st.subheader("Buat Catatan Baru")
note_input = st.text_area("Masukkan materi catatanmu:")

if st.button("Generate Note"):
    if note_input:
        new_note = pd.DataFrame([[len(notes_df)+1, "Catatan Baru", note_input[:100]+"..."]], columns=["id","judul","isi"])
        notes_df = pd.concat([notes_df, new_note], ignore_index=True)
        notes_df.to_excel("notes.xlsx", index=False)
        st.success("Catatan berhasil dibuat!")

# Tampilkan catatan
st.subheader("Daftar Catatan")
st.dataframe(notes_df)


