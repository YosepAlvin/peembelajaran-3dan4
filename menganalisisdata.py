import matplotlib.pyplot as plt

# Daftar pemain yang mengalami cedera
data_cedera = [
    {"nama": "Marcus Rashford", "posisi": "Penyerang", "jenis_cedera": "Cedera Betis", "durasi": "6-8 Minggu"},
    {"nama": "Luke Shaw", "posisi": "Bek Kiri", "jenis_cedera": "Cedera Paha", "durasi": "4-6 Minggu"},
    {"nama": "Paul Pogba", "posisi": "Gelandang", "jenis_cedera": "Cedera Engkel", "durasi": "3-5 Minggu"},
    {"nama": "Mason Greenwood", "posisi": "Penyerang", "jenis_cedera": "Cedera Lutut", "durasi": "2-4 Minggu"}
    # Tambahkan data cedera pemain lain jika diperlukan
]

# Analisis frekuensi cedera berdasarkan posisi
frekuensi_cedera = {}
for pemain in data_cedera:
    posisi = pemain["posisi"]
    frekuensi_cedera[posisi] = frekuensi_cedera.get(posisi, 0) + 1

# Tren cedera selama musim (contoh data dummy)
tren_cedera = [3, 5, 7, 4, 6, 2, 1, 2, 4, 5, 6, 7]  # Jumlah cedera per bulan

# Plot tren cedera
bulan = [f"Bulan-{i+1}" for i in range(len(tren_cedera))]
plt.plot(bulan, tren_cedera)
plt.title("Tren Cedera selama Musim")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Cedera")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Analisis penyebab cedera (contoh data dummy)
penyebab_cedera = {
    "Intensitas Latihan Tinggi": 10,
    "Jumlah Pertandingan Banyak": 8,
    "Jenis Lapangan Buruk": 5,
    # Tambahkan faktor penyebab lain jika diperlukan
}

# Durasi rata-rata cedera
durasi_cedera = [6, 5, 4, 3]  # Durasi rata-rata cedera untuk setiap jenis cedera (contoh data dummy)
rata_rata = sum(durasi_cedera) / len(durasi_cedera)
print("Durasi Rata-rata Cedera:", rata_rata, "Minggu")

# Efek cedera terhadap kinerja tim (analisis subyektif)

# Strategi pengurangan cedera (analisis subyektif)
