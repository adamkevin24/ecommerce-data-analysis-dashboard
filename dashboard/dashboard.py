import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard E-Commerce", layout="wide")

# 1. Load Data dengan Caching agar cepat
@st.cache_data
def load_data():
    df = pd.read_csv('dashboard/main_data.csv')
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    return df

df = load_data()

# 2. Sidebar Filter
st.sidebar.header("Filter Data")
min_date = df['order_purchase_timestamp'].min()
max_date = df['order_purchase_timestamp'].max()

date_range = st.sidebar.date_input(
    "Rentang Waktu",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Filter Data Berdasarkan Tanggal
start_date, end_date = date_range
mask = (df['order_purchase_timestamp'].dt.date >= start_date) & (df['order_purchase_timestamp'].dt.date <= end_date)
filtered_df = df.loc[mask]

# Judul Utama
st.title("📊 E-Commerce Analysis Dashboard")
st.markdown("Dashboard ini menampilkan tren transaksi, performa kategori, dan segmentasi pelanggan.")

# 3. Tab Dashboard
tab1, tab2, tab3 = st.tabs(["Tren Transaksi & Revenue", "Top Kategori Produk", "Segmentasi RFM"])

# --- TAB 1: Tren ---
with tab1:
    st.subheader("Tren Jumlah Pesanan dan Revenue")
    monthly_data = filtered_df.groupby(pd.Grouper(key='order_purchase_timestamp', freq='ME')).agg({
        'order_id': 'nunique',
        'payment_value': 'sum'
    }).reset_index()

    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax2 = ax1.twinx()
    
    sns.lineplot(data=monthly_data, x='order_purchase_timestamp', y='order_id', ax=ax1, color='blue', marker='o', label='Jumlah Order')
    sns.lineplot(data=monthly_data, x='order_purchase_timestamp', y='payment_value', ax=ax2, color='green', marker='o', label='Revenue')
    
    ax1.set_ylabel('Jumlah Order')
    ax2.set_ylabel('Total Revenue')
    plt.title('Tren Bulanan 2017-2018')
    st.pyplot(fig)

# --- TAB 2: Kategori ---
with tab2:
    st.subheader("Top Kategori Produk")
    top_n = st.slider("Pilih jumlah kategori teratas", 5, 15, 10)
    
    cat_analysis = filtered_df.groupby('product_category_name').agg({
        'price': 'sum',
        'order_id': 'nunique'
    }).sort_values(by='price', ascending=False).head(top_n)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    sns.barplot(data=cat_analysis, x='price', y=cat_analysis.index, ax=ax1, palette='viridis')
    ax1.set_title('Top Kategori by Revenue')
    
    cat_trans = cat_analysis.sort_values(by='order_id', ascending=False)
    sns.barplot(data=cat_trans, x='order_id', y=cat_trans.index, ax=ax2, palette='magma')
    ax2.set_title('Top Kategori by Transaksi')
    
    st.pyplot(fig)

# --- TAB 3: RFM ---
with tab3:
    st.subheader("Segmentasi Pelanggan (RFM)")
    # Kalkulasi RFM on-the-fly
    reference_date = filtered_df['order_purchase_timestamp'].max() + pd.Timedelta(days=1)
    rfm = filtered_df.groupby('customer_id').agg({
        'order_purchase_timestamp': lambda x: (reference_date - x.max()).days,
        'order_id': 'nunique',
        'payment_value': 'sum'
    })
    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    
    # Simple Segmentation Logic
    rfm['Segment'] = 'Regular'
    rfm.loc[rfm['Monetary'] > rfm['Monetary'].median(), 'Segment'] = 'Loyal'
    rfm.loc[rfm['Frequency'] > 1, 'Segment'] = 'High Value'

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.countplot(data=rfm, x='Segment', palette='coolwarm')
    st.pyplot(fig)
