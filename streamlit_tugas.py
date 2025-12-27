import streamlit as st
import pandas as pd

st.title("Sistem Informasi Penjualan")

st.header("Dashboard Penjualan")

st.subheader("Informasi Produk dan Harga")
st.write(
    "Aplikasi web ini dibuat menggunakan Streamlit untuk menampilkan "
    "informasi penjualan produk. Website ini berisi daftar produk, "
    "harga, serta visualisasi data sederhana."
)

st.caption("Tugas Pertemuan 12 – Pengenalan Streamlit")

st.subheader("Contoh Potongan Kode Streamlit")
st.code("""
st.title("Sistem Informasi Penjualan")
st.dataframe(data_produk)
st.bar_chart(data_produk)
""", language="python")

st.subheader("Tabel Produk")
data_produk = {
    "Produk": ["Laptop", "Mouse", "Keyboard", "Headset"],
    "Harga (Rp)": [7000000, 150000, 300000, 250000]
}

df = pd.DataFrame(data_produk)
st.dataframe(df)

st.subheader("Grafik Harga Produk")

st.bar_chart(df.set_index("Produk"))
