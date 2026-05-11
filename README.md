# Proyek Analisis Data E-Commerce

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data transaksi e-commerce guna memahami perilaku pelanggan, tren penjualan, serta kategori produk yang paling berkontribusi terhadap revenue.

Analisis dilakukan menggunakan Python melalui tahapan data wrangling, exploratory data analysis (EDA), visualisasi data, serta analisis lanjutan menggunakan metode RFM (Recency, Frequency, Monetary).

---

## Pertanyaan Bisnis
1. Bagaimana segmentasi pelanggan berdasarkan nilai Recency, Frequency, dan Monetary selama periode 2017–2018, serta segmen mana yang paling berkontribusi terhadap total revenue?

2. Kategori produk apa yang memiliki kontribusi tertinggi terhadap total revenue dan jumlah transaksi selama periode 2017–2018?

3. Bagaimana tren jumlah transaksi dan total revenue per bulan selama periode 2017–2018, serta apakah terdapat pola musiman dalam aktivitas pembelian pelanggan?

---

## Insight Utama
- Tren penjualan mengalami peningkatan signifikan sejak 2017 dan cenderung stabil di 2018.
- Kategori seperti cama_mesa_banho, beleza_saude, dan informatica_acessorios menjadi penyumbang utama revenue.
- Mayoritas pelanggan termasuk dalam segmen Loyal berdasarkan analisis RFM.

---

## Struktur Direktori
submission/
├── dashboard/
│ ├── main_data.csv
│ └── dashboard.py
├── data/
├── notebook.ipynb
├── README.md
├── requirements.txt


## Cara Menjalankan Dashboard
1. Setup Environment:

Gunakan virtual environment :

bash
python -m venv venv

Aktifkan environment:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

2. Install Dependencies
pip install -r requirements.txt

3. Jalankan Streamlit:

streamlit run dashboard.py

## Dataset
Dataset yang digunakan merupakan data e-commerce yang mencakup informasi pelanggan, pesanan, produk, dan pembayaran.

## Live Dashboard
Berikut aku lampirkan link yang bisa mengarah kan ke live dashboard

https://ecommerce-data-analysis-dashboard-gncqekegs9cn3tm7gr4tup.streamlit.app/
