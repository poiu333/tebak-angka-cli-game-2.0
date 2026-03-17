# 🎯 Tebak Angka 2.0

Game tebak angka berbasis terminal dengan sistem level, skor, dan leaderboard.

---

## 📋 Deskripsi

Tebak Angka 2.0 adalah game sederhana di terminal di mana pemain harus menebak angka rahasia dalam batas percobaan tertentu. Setiap level, rentang angka dan jumlah percobaan bertambah, membuat tantangan semakin sulit.

---

## 🚀 Cara Menjalankan

Pastikan Python 3 sudah terinstall, lalu jalankan:

```bash
python3 tebak.py
```

---

## 📁 Struktur File

```
tebak angka 2.0/
├── tebak.py      # File utama game
└── skor.txt      # Leaderboard (dibuat otomatis saat pertama kali bermain)
```

---

## 🎮 Cara Bermain

1. Masukkan nama pemain saat diminta
2. Tebak angka sesuai rentang yang ditampilkan
3. Program akan memberi petunjuk **terlalu tinggi** atau **terlalu rendah**
4. Tebak angka yang benar sebelum percobaan habis

---

## ⚙️ Sistem Level

| Level | Rentang Angka | Jumlah Percobaan |
|-------|--------------|-----------------|
| 1     | 1 - 50       | 11              |
| 2     | 1 - 60       | 12              |
| 3     | 1 - 70       | 13              |
| ...   | +10 tiap level | +1 tiap level |

---

## 🏆 Sistem Skor

Skor dihitung berdasarkan level dan sisa percobaan:

```
Skor per ronde = (Level × 100) + (Sisa Percobaan × 10)
```

**Contoh:** Menang di Level 2 dengan sisa 5 percobaan = (2×100) + (5×10) = **250 poin**

> Menebak lebih cepat = skor lebih tinggi!

---

## 📊 Leaderboard

- Top 5 skor tertinggi disimpan di `skor.txt`
- Leaderboard ditampilkan di akhir setiap sesi bermain
- Format penyimpanan: JSON

---

## 🔄 Alur Game

```
Mulai → Input nama → Tampil leaderboard
           ↓
        Main game
           ↓
      Berhasil? ──── Ya ──→ Tanya naik level atau berhenti
           │
          Tidak
           ↓
      Pilih: Ulangi level / Berhenti
           ↓
      Game selesai → Simpan skor → Tampil leaderboard
```

---

## 🛠️ Dependensi

- Python 3.x (tidak perlu library tambahan)
- Module bawaan: `random`, `os`, `json`

---

## 📝 Catatan

- File `skor.txt` dibuat **otomatis** saat pertama kali game selesai
- Jika `skor.txt` dihapus, leaderboard akan mulai dari awal
- Nama pemain kosong akan otomatis diisi **"anonim"**
