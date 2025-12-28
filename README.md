# Analisis Kualitas Udara dan Penerapan Early Warning Classification 

## Deskripsi Singkat
Proyek ini melakukan analisis mendalam terhadap kualitas udara di Stasiun Changping menggunakan dataset PRSA (2013-2017). Tujuan utamanya adalah untuk memahami pola polusi PM2.5 berdasarkan waktu dan membangun sistem klasifikasi peringatan dini (*Early Warning System*) menggunakan Machine Learning untuk memprediksi risiko pemburukan kualitas udara dalam 24 jam ke depan.

## Dataset
Dataset yang digunakan adalah **Air Quality Dataset - Station Changping** yang berisi data konsentrasi polutan (PM2.5, PM10, SO2, NO2, CO, O3) dan parameter meteorologi (Suhu, Tekanan Udara, Titik Embun, Curah Hujan, dan Kecepatan Angin) yang dicatat setiap jam. 

## Cara Menjalankan
### 1. Persiapan Virtual Environment
Disarankan untuk menggunakan virtual environment agar tidak terjadi konflik library:
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Instalasi Library
DGunakan perintah berikut untuk menginstal semua library yang dibutuhkan:
```bash
pip install -r requirements.txt
```

### 3. Menjalankan Notebook
Buka file notebook.ipynb di VS Code atau Jupyter Notebook lalu jalankan cell berurutan (Run All) untuk melihat proses pengolahan data (Wrangling), eksplorasi (EDA), dan pembuatan model Machine Learning.

### 4. Menjalankan Dashboard Streamlit
Jalankan dashboard interaktif secara lokal dengan perintah berikut:
```bash
streamlit run app.py
```

## Ringkasan Insight Hasil Analisis
- Pola Waktu Polusi: Konsentrasi PM2.5 cenderung mencapai titik tertinggi pada jam-jam malam hari (pukul 20:00 - 00:00), yang kemungkinan disebabkan oleh faktor meteorologi seperti penurunan suhu permukaan (inversi).

- Efektivitas Indikator Tren: Tren kenaikan polusi dalam 3 jam terakhir terbukti menjadi indikator kuat untuk memprediksi risiko kualitas udara buruk di masa depan.

- Performa Model: Model Logistic Regression yang dikembangkan berhasil mengklasifikasikan risiko polusi udara (PM2.5 > 75) dalam 24 jam ke depan dengan tingkat akurasi sebesar 68,7%.

## Live Dashboard
Klik di sini untuk mengakses dashboard Streamlit.