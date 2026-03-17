import random
import os
import json

angka_awal = 50
tambah_angka_per_level = 10
percobaan_awal = 10
files_skor = "skor.txt"

def lebar_terminal():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80

def tengah(teks):
    return teks.center(lebar_terminal())

def cetak(teks):
    print(tengah(teks))

def baca_leaderboard():
    try:
        with open(files_skor, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def simpan_leaderboard(data):
    with open(files_skor, 'w') as f:
        json.dump(data, f, indent=4)

def tambah_skor(nama, skor, level):
    leaderboard = baca_leaderboard()
    leaderboard.append({"nama": nama, "skor": skor, "level": level})
    leaderboard.sort(key=lambda x: x['skor'], reverse=True)
    leaderboard = leaderboard[:5]
    simpan_leaderboard(leaderboard)

def tampilkan_leaderboard():
    leaderboard = baca_leaderboard()
    cetak("=== LEADERBOARD TOP 5 ===")
    if not leaderboard:
        cetak("Belum ada skor yang tercatat.")
    else:
        for idx, entry in enumerate(leaderboard[:5], start=1):
            cetak(f"{idx}. {entry['nama']} - Skor: {entry['skor']} (Level {entry['level']})")
    cetak("=" * 40)

def setup_level(nomor_level):
    angka_maksimal = angka_awal + (nomor_level - 1) * tambah_angka_per_level
    angka_rahasia = random.randint(1, angka_maksimal)
    percobaan = percobaan_awal + nomor_level
    return angka_maksimal, angka_rahasia, percobaan

def hitung_skor(level_pemain, sisa_percobaan):
    return (level_pemain * 100) + (sisa_percobaan * 10)

def pengambilan_input(angka_maksimal):
    while True:
        try:
            tebakan = int(input(tengah(f"Masukkan tebakan Anda (1-{angka_maksimal}): ")))
            if 1 <= tebakan <= angka_maksimal:
                return tebakan
            else:
                cetak("Angka di luar jangkauan!")
        except ValueError:
            cetak("Input tidak valid. Masukkan angka.")

def pengecekan_tebakan(tebakan, angka_rahasia):
    if tebakan < angka_rahasia:
        cetak("Tebakan terlalu rendah!")
        return False
    elif tebakan > angka_rahasia:
        cetak("Tebakan terlalu tinggi!")
        return False
    else:
        cetak("Selamat! Tebakan Anda benar!")
        return True

def tampilkan_skor(skor_total, level_pemain):
    cetak("=" * 40)
    cetak(f"Level    : {level_pemain}")
    cetak(f"Skor     : {skor_total}")
    cetak("=" * 40)

def tanyakan_lanjut(pertanyaan):
    while True:
        jawaban = input(tengah(pertanyaan)).strip().lower()
        if jawaban in ['y', 'n']:
            return jawaban == 'y'
        else:
            cetak("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")

def tebak_angka():
    cetak("Selamat datang di permainan Tebak Angka!")
    nama_pemain = input(tengah("Masukkan nama Anda: ")).strip() or "anonim"
    level_pemain = 1
    skor_total = 0

    while True:
        angka_maksimal, angka_rahasia, percobaan = setup_level(level_pemain)
        cetak(f"Level {level_pemain}: Tebak angka antara 1 dan {angka_maksimal}.")
        cetak(f"Anda memiliki {percobaan} percobaan.")
        tampilkan_skor(skor_total, level_pemain)

        berhasil = False
        for i in range(percobaan):
            sisa = percobaan - i
            cetak(f"Sisa percobaan: {sisa}")
            tebakan = pengambilan_input(angka_maksimal)
            if pengecekan_tebakan(tebakan, angka_rahasia):
                berhasil = True
                sisa_percobaan = sisa - 1
                break

        if not berhasil:
            cetak(f"Maaf, kehabisan percobaan! Angka rahasia adalah {angka_rahasia}.")
            cetak("Skor tidak bertambah karena gagal.")
            tampilkan_skor(skor_total, level_pemain)
            cetak("1. Ulangi level ini")
            cetak("2. Berhenti bermain")
            pilihan = input(tengah("Pilihan Anda (1/2): ")).strip()

            if pilihan == '1':
                cetak("Baik, mengulang level ini...")
                continue
            else:
                tambah_skor(nama_pemain, skor_total, level_pemain)
                cetak(f"Game Over! Skor akhir Anda: {skor_total}")
                tampilkan_leaderboard()
                break

        else:
            skor_ronde = hitung_skor(level_pemain, sisa_percobaan)
            skor_total += skor_ronde
            cetak(f"+{skor_ronde} poin! (Level {level_pemain} x100 + {sisa_percobaan} sisa percobaan x10)")
            tampilkan_skor(skor_total, level_pemain)

            lanjut = tanyakan_lanjut("Lanjut ke level berikutnya? (y/n): ")
            if not lanjut:
                tambah_skor(nama_pemain, skor_total, level_pemain)
                cetak(f"Terima kasih! Skor akhir Anda: {skor_total}")
                tampilkan_leaderboard()
                break
            level_pemain += 1

def menu_utama():
    while True:
        cetak("=" * 40)
        cetak("=== TEBAK ANGKA 2.0 ===")
        cetak("=" * 40)
        cetak("1. Mulai Permainan")
        cetak("2. Lihat Leaderboard")
        cetak("3. Keluar")
        pilihan = input(tengah("Pilihan Anda (1/2/3): ")).strip()

        if pilihan == '1':
            tebak_angka()
        elif pilihan == '2':
            tampilkan_leaderboard()
        elif pilihan == '3':
            cetak("Terima kasih telah bermain!")
            break
        else:
            cetak("Pilihan tidak valid. Silakan coba lagi.")

menu_utama()