from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Dashboard Penjualan", layout="wide")
st.title("Dashboard Penjualan")
st.caption("Contoh untuk pembelajaran HCI dan visualisasi data. Data bersifat simulasi.")

df = pd.read_csv(Path(__file__).parent / "data" / "sales_dashboard.csv")
df["pendapatan"] = df["jumlah"] * df["harga"]
total_revenue = df["pendapatan"].sum()
total_units = df["jumlah"].sum()
top_product = df.groupby("produk")["jumlah"].sum().idxmax()

c1, c2, c3 = st.columns(3)
c1.metric("Total pendapatan", f"Rp{total_revenue:,.0f}")
c2.metric("Unit terjual", f"{total_units:,}")
c3.metric("Produk terlaris", top_product)

st.subheader("Pendapatan per produk")
by_product = df.groupby("produk", as_index=False)["pendapatan"].sum()
fig = px.bar(by_product, x="produk", y="pendapatan",
             labels={"produk": "Nama produk", "pendapatan": "Pendapatan (Rp)"},
             title="Perbandingan pendapatan")
st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

st.subheader("Data transaksi")
st.dataframe(df, use_container_width=True, hide_index=True)
st.info("Desain: judul dan label eksplisit, ringkasan KPI, tabel pendukung, serta satu grafik utama agar mudah dipindai.")
