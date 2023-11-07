import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# - BAGAIMANA PENGARUH CUACA TERHADAP JUMLAH PEMINJAMAN SEPEDA?
# - PADA BULAN APA SAJA PEMINJAMAN SEPEDA PALING BANYAK DAN PALING SEDIKIT? 
# - APAKAH ADA POLA BERDASARKAN BULAN DAN JAM DALAM JUMLAH SEWA SEPEDA HARIAN?



# --------------------gathering data--------------------
# ambil source data
hour = pd.read_csv("hour.csv") 
day = pd.read_csv("day.csv")

# menghitung jumlah baris setiap DataFrame
print("Jumlah baris di DataFrame day:", day.shape)
print("Jumlah baris di DataFrame hour:", hour.shape)

# melakukan merge pada kedua dataframe hour dan day
bike_sharing = day.merge(hour, on='dteday', how='inner', suffixes=('_daily', '_hourly'))
print("Jumlah baris di DataFrame bike:", bike_sharing.shape)



# --------------------assessing data--------------------
# pengecekan tipe data
hour.info()
day.info()
bike_sharing.info()

# pengecekan missing data pada bike sharing
print("Jumlah missing data: ", bike_sharing.isnull().sum())

# pengecekan duplicated data pada bike sharing
print("Jumlah duplikasi: ", bike_sharing.duplicated().sum())



# --------------------cleaning data--------------------
#dikarenakan tidak ada data yang missing, duplikat dan tidak ada tipe data yang salah, jadi tahap ini dilewat



# --------------------exploratory data analysis--------------------
# melihat statistik dataframe bikesharing
print(bike_sharing.describe(include="all"))

# menjumlahkan penyewa sepeda perhari berdasarkan musim
print(bike_sharing.groupby(by="season_daily").agg({
    "cnt_daily": "count"
}).sort_values(by="cnt_daily", ascending=False))

# menjumlahkan penyewa sepeda perhari berdasarkan bulan
print(bike_sharing.groupby(by="mnth_daily").agg({
    "cnt_daily": "count"
}).sort_values(by="cnt_daily", ascending=False))

# menjumlahkan penyewa sepeda perhari berdasarkan jam
print(bike_sharing.groupby(by="hr").agg({
    "cnt_hourly": "mean"
}))



# --------------------visualisasi data--------------------
# visualisai penyewa sepeda perhari berdasarkan musim
seasonal_data = bike_sharing.groupby('season_daily')['cnt_daily'].mean()
season_names = ['Spring', 'Summer', 'Fall', 'Winter']
colors1 = ['blue','blue','orange','blue']

plt.bar(season_names, seasonal_data, color=colors1)
plt.xlabel('Season')
plt.ylabel('Average Number of Daily Rentals')
plt.title('Influence of Season on Daily Bicycle Rentals')
plt.show()

# visualisai penyewa sepeda perhari berdasarkan bulan
monthly_data = bike_sharing.groupby('mnth_daily')['cnt_daily'].mean()
month_names = ['January','February','March','April','Mei','June','July','August','September','October','November','December']
colors2 = ['red','blue','blue','blue','blue','orange','blue','blue','blue','blue','blue','blue']

plt.bar(month_names, monthly_data, color=colors2)
plt.xlabel('Month')
plt.ylabel('Average Number of Daily Rentals')
plt.title('Influence of Month on Daily Bicycle Rentals')
plt.xticks(rotation=45)
plt.show()

# visualisai pola penyewa sepeda berdasarkan bulan
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x="mnth_daily", y="cnt_daily", data=bike_sharing, errorbar=None, color='green')
plt.title("Pattern of Daily Bicycle Rental Number by Month")
plt.xlabel("Month")
plt.ylabel("Amount of Daily Rental")
plt.show()

# visualisai pola penyewa sepeda berdasarkan jam
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x="hr", y="cnt_hourly", data=bike_sharing, errorbar=None, color='green')
plt.title("Pattern of Daily Bicycle Rental Number by Hour")
plt.xlabel("Hour")
plt.ylabel("Amount of Daily Rental")
plt.show()



# --------------------dashboard--------------------
st.title('Proyek Analisis Data :sparkles:')
st.write('''"Proyek ini disusun sebagai syarat untuk menyelesaikan kelas Belajar Analisis Data dengan Python Dicoding"''')

st.header('Bike Sharing Dataset')
st.subheader('Raw Dataset hour.csv')
st.dataframe(data=hour, width=500, height=300)
st.subheader('Raw Dataset day.csv')
st.dataframe(data=day, width=500, height=300)
st.write('''
	- instant: record index
	- dteday : date
	- season : season (1=springer, 2=summer, 3=fall, 4=winter)
	- yr : year (0: 2011, 1:2012)
	- mnth : month ( 1 to 12)
	- hr : hour (0 to 23)
	- holiday : weather day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)
	- weekday : day of the week
	- workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
	+ weathersit : 
		- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
		- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
		- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
		- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
	- temp : Normalized temperature in Celsius. The values are divided to 41 (max)
	- atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
	- hum: Normalized humidity. The values are divided to 100 (max)
	- windspeed: Normalized wind speed. The values are divided to 67 (max)
	- casual: count of casual users
	- registered: count of registered users
	- cnt: count of total rental bikes including both casual and registered
 ''')

st.subheader('Pertanyaan Bisnis?')
st.write('''- Bagaimana Pengaruh Musim Terhadap Jumlah Peminjaman Sepeda?
- Pada Bulan Apa Saja Peminjaman Sepeda Paling Banyak Dan Paling Sedikit?
- Apakah Ada Pola Berdasarkan Bulan Dan Jam Dalam Jumlah Sewa Sepeda Harian?''')

st.subheader('Hasil Analisis')
tab1, tab2, tab3 = st.tabs(["Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3"])
 
with tab1:
    st.header("Bagaimana Pengaruh Musim Terhadap Jumlah Peminjaman Sepeda?")

    # Membuat bar chart dengan Matplotlib
    fig, ax = plt.subplots()
    ax.bar(season_names, seasonal_data, color=colors1)
    ax.set_ylabel("Average Number of Daily Rentals")
    ax.set_xlabel("Season")
    ax.set_title("Influence of Season on Daily Bicycle Rentals", loc="center")

    # Menampilkan grafik dalam aplikasi Streamlit
    st.pyplot(fig)

    with st.expander("Conlusion"):
        st.write('''Berdasarkan grafik diatas dapat diketahui bahwa jumlah sewa sepeda paling banyak terdapat pada musim gugur/fall season.''')
 
with tab2:
    st.header("Pada Bulan Apa Saja Peminjaman Sepeda Paling Banyak Dan Paling Sedikit?")
              
    # Membuat bar chart dengan Matplotlib
    fig, ax = plt.subplots()
    ax.bar(month_names, monthly_data, color=colors2)
    ax.set_ylabel("Average Number of Daily Rentals")
    ax.set_xlabel("Month")
    ax.set_title("Influence of Month on Daily Bicycle Rentals", loc="center")
    ax.tick_params(axis='x', labelrotation= 45)

    # Menampilkan grafik dalam aplikasi Streamlit
    st.pyplot(fig)

    with st.expander("Conlusion"):
        st.write('''Berdasarkan grafik diatas dapat diketahui bahwa jumlah sewa sepeda paling banyak terdapat pada bulan Juni dan jumlah sewa sepeda paling sedikit terdapat pada bulan Januari.''')
 
with tab3:
    st.header("Apakah Ada Pola Berdasarkan Bulan Dan Jam Dalam Jumlah Sewa Sepeda Harian?")

    # Membuat bar chart dengan Matplotlib
    fig, ax = plt.subplots()
    sns.lineplot(x="mnth_daily", y="cnt_daily", data=bike_sharing, ci=None, color='blue',ax=ax)
    ax.set_ylabel("Amount of Daily Rentals")
    ax.set_xlabel("Month")
    ax.set_title("Pattern of Daily Bicycle Rental Number by Month", loc="center")

    # Menampilkan grafik dalam aplikasi Streamlit
    st.pyplot(fig)

    # Membuat bar chart dengan Matplotlib
    fig, ax = plt.subplots()
    sns.lineplot(x="hr", y="cnt_hourly", data=bike_sharing, ci=None, color='blue',ax=ax)
    ax.set_ylabel("Amount of Daily Rentals")
    ax.set_xlabel("Hour")
    ax.set_title("Pattern of Daily Bicycle Rental Number by Hour", loc="center")

    # Menampilkan grafik dalam aplikasi Streamlit
    st.pyplot(fig)

    with st.expander("Conlusion"):
        st.write('''Jika berdasarkan bulan, jumlah sewa sepeda meningkat pada bulan ke-9 dan ke-6. Jika berdasarkan jam, jumlah sewa sepeda meningkat dikisaran jam 8 pagi dan dikisaran jam 5 atau 6 sore.''')

st.caption('Dewo Kanirogo (c) 2023')

# - Berdasarkan grafik diatas dapat diketahui bahwa jumlah sewa sepeda paling banyak terdapat pada musim gugur/fall season.
# - Berdasarkan grafik diatas dapat diketahui bahwa jumlah sewa sepeda paling banyak terdapat pada bulan Juni dan jumlah sewa sepeda paling bsedikit terdapat pada bulan Januari.
# - Jika berdasarkan bulan, jumlah sewa sepeda meningkat pada bulan ke-9 dan ke-6. Jika berdasarkan jam, jumlah sewa sepeda meningkat dikisaran jam 8 pagi dan dikisaran jam 5 atau 6 sore.
