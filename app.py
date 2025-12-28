import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Air Quality Analysis - Changping Station", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("dataset/PRSA_Data_Changping_20130301-20170228.csv")
    df['Datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    df = df.dropna().copy()
    return df

df = load_data()

# Sidebar
st.sidebar.header("Filter Data")
year_range = st.sidebar.slider("Pilih Rentang Tahun", 2013, 2017, (2013, 2017))
df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Main Page
st.title("📊 Changping Air Quality Analysis")
st.markdown("Dashboard ini menyajikan analisis konsentrasi PM2.5 berdasarkan data historis 2013-2017.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Rata-rata PM2.5", round(df_filtered['PM2.5'].mean(), 2))
with col2:
    st.metric("Konsentrasi Tertinggi", df_filtered['PM2.5'].max())
with col3:
    st.metric("Rata-rata Suhu (TEMP)", round(df_filtered['TEMP'].mean(), 2))

st.subheader("📈 Tren Konsentrasi PM2.5 Seiring Waktu")
fig_time = plt.figure(figsize=(12, 4))
plt.plot(df_filtered['Datetime'], df_filtered['PM2.5'], color='#2ca02c', linewidth=0.5)
plt.xlabel("Waktu")
plt.ylabel("PM2.5")
st.pyplot(fig_time)

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("⏰ Rata-rata Polusi per Jam")
    hourly_avg = df_filtered.groupby('hour')['PM2.5'].mean()
    fig_hour = plt.figure(figsize=(8, 5))
    sns.barplot(x=hourly_avg.index, y=hourly_avg.values, palette="viridis")
    plt.xlabel("Jam (0-23)")
    plt.ylabel("Rata-rata PM2.5")
    st.pyplot(fig_hour)

with col_b:
    st.subheader("📉 Distribusi Tren PM2.5")
    df_filtered['pm25_trend'] = df_filtered['PM2.5'] - df_filtered['PM2.5'].shift(3)
    fig_dist = plt.figure(figsize=(8, 5))
    sns.histplot(df_filtered['pm25_trend'].dropna(), bins=30, kde=True, color='orange')
    plt.xlabel("Perubahan PM2.5 (3 Jam Terakhir)")
    st.pyplot(fig_dist)

st.markdown("---")
st.subheader("Kesimpulan Analisis Lanjutan")
st.write("""
Berdasarkan model klasifikasi risiko, ditemukan bahwa faktor **Waktu (Jam)** dan **Tren Kenaikan 3 Jam Terakhir** adalah prediktor paling akurat untuk mendeteksi potensi polusi berbahaya (PM2.5 > 75) dalam 24 jam ke depan.
""")

st.caption("Data Source: PRSA Data Station Changping (2013-2017)")