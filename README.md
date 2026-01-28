UAS Teknik Optimasi

**Genetic Algorithm (GA) & Ant Colony Optimization (ACO)**

## 👤 Identitas Mahasiswa

* **Nama** : Ridho Nur Rohmanudin
* **NIM** : 2300018042
* **Mata Kuliah** : Teknik Optimasi
* **Program Studi** : Informatika

---

## 📖 Deskripsi Proyek

Repository ini berisi penyelesaian **Ujian Akhir Semester (UAS) Teknik Optimasi** yang mencakup dua algoritma optimasi berbasis populasi:

1. **Genetic Algorithm (GA)** untuk penentuan paket parcel lebaran.
2. **Ant Colony Optimization (ACO)** untuk penentuan rute terpendek ziarah Wali Songo.

---

## 🧠 Soal 1 — Genetic Algorithm (GA)

**Permasalahan:**
Menentukan kombinasi paket parcel lebaran dengan **selisih kembalian terkecil** dari budget Rp125.000.

### 🔧 Parameter GA

* Jumlah kromosom : 25
* Crossover rate : 0.23
* Mutation rate : 0.1
* Maksimum generasi : 55
* Budget : Rp125.000

### ⚙️ Representasi Solusi

* Kromosom direpresentasikan dalam bentuk **biner (0/1)**
* `1` = produk dipilih
* `0` = produk tidak dipilih

### 🎯 Fungsi Objektif

Meminimalkan:

```
Sisa Budget = Budget − Total Harga Parcel
```

Jika total harga melebihi budget, maka diberikan penalti.

### 📊 Output Program

* Tabel nilai minimum tiap iterasi
* Nilai minimum global/akhir
* Daftar produk parcel terbaik
* Total harga dan sisa budget

📄 **File program:**
`GA parcel.py`

---

## 🧠 Soal 2 — Ant Colony Optimization (ACO)

**Permasalahan:**
Menentukan rute terpendek perjalanan **ziarah Wali Songo** dengan titik awal dan akhir dari kos mahasiswa.

### 🔧 Parameter ACO

* Q : 100
* ρ (rho) : 0.05
* Jumlah semut : 17
* Iterasi maksimum : 35

### 📍 Rute Ziarah

Kos → Sunan Gresik → Sunan Ampel → Sunan Giri → Sunan Bonang →
Sunan Drajat → Sunan Muria → Sunan Kudus → Sunan Kalijaga →
Sunan Gunung Jati → Kos

Total jarak perjalanan: **1377 km**

### 🎯 Fungsi Objektif

Meminimalkan total jarak perjalanan.

### 📊 Output Program

* Nilai minimum tiap iterasi
* Nilai minimum global
* Rute terpilih

📄 **File program:**
`ACO ziarah.py`

---

## ▶️ Cara Menjalankan Program

Jalankan masing-masing file menggunakan Python:

```bash
python "GA parcel.py"
```

```bash
python "ACO ziarah.py"
```

---

## ✅ Kesimpulan

* Genetic Algorithm berhasil menentukan paket parcel dengan sisa budget minimum.
* Ant Colony Optimization menghasilkan rute ziarah dengan jarak terpendek.
* Seluruh parameter dan output telah disesuaikan dengan ketentuan UAS Teknik Optimasi.

---


kerja bagus bro 👏 sekarang tinggal **submit** 😎
