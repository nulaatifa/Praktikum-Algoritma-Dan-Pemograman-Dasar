
import Data
from Autentifikasi import countdown
from prettytable import PrettyTable
import os


def tampilkan_kategori():
    print("\nMENU KATEGORI FILM:")
    for i, kategori in enumerate(Data.film_data.keys(), start=1):
        print(f"{i}. {kategori}")


def tampilkan_daftar_film(kategori):
    try:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\nDAFTAR FILM {kategori.upper()}")

        table = PrettyTable()
        table.field_names = ["Kode", "Judul Film", "Status"]
        table.align["Judul Film"] = "l"

        for kode, data in Data.film_data[kategori].items():
            table.add_row([kode, data['judul'], data['status']])
        print(table)

    except KeyError:
        print("Kategori tidak ditemukan!")
        
    input("Tekan Enter untuk kembali...")


def tambah_film(kategori):
    kode = input("Masukkan kode film baru: ")
    if kode in Data.film_data[kategori]:
        print("Kode film sudah ada.")
    else:
        judul = input("Masukkan judul film: ")
        Data.film_data[kategori][kode] = {"judul": judul, "status": "Tersedia"}
        print(f"Film '{judul}' berhasil ditambahkan!")


def hapus_film(kategori):
    kode = input("Masukkan kode film yang ingin dihapus: ")
    if kode in Data.film_data[kategori]:
        judul = Data.film_data[kategori][kode]["judul"]
        del Data.film_data[kategori][kode]
        print(f"Film '{judul}' berhasil dihapus.")
    else:
        print("Kode film tidak ditemukan.")


def menu_utama():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        tampilkan_kategori()
        print("5. Logout")
        pilihan = input("Pilih kategori (1-5): ")

        kategori_keys = list(Data.film_data.keys())
        kategori_dict = {str(i+1): kategori_keys[i] for i in range(len(kategori_keys))}

        if pilihan in kategori_dict:
            kategori = kategori_dict[pilihan]
        elif pilihan == "5":
            countdown(5)
            Data.Role = None
            Data.Username = None
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk lanjut...")
            continue

        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"===== MENU {kategori.upper()} =====")
            print("1. Lihat Daftar Film")
            print("2. Sewa Film")
            print("3. Kembalikan Film")
            if Data.Role == "Admin":
                print("4. Tambah Film")
                print("5. Hapus Film")
                print("6. Kembali")
            else:
                print("4. Kembali")

            pilih_kat = input("Pilih menu: ")

            try:
                if pilih_kat == "1":
                    tampilkan_daftar_film(kategori)

                elif pilih_kat == "2":
                    kode = input("Masukkan kode film: ")
                    if kode in Data.film_data[kategori]:
                        if Data.film_data[kategori][kode]["status"] == "Tersedia":
                            Data.film_data[kategori][kode]["status"] = "Sedang Disewa"
                            print(f"Film '{Data.film_data[kategori][kode]['judul']}' berhasil disewa!")
                        else:
                            print("Film sedang disewa orang lain.")
                    else:
                        print("Kode film tidak ditemukan.")
                    input("Tekan Enter untuk kembali...")

                elif pilih_kat == "3":
                    kode = input("Masukkan kode film: ")
                    if kode in Data.film_data[kategori]:
                        if Data.film_data[kategori][kode]["status"] == "Sedang Disewa":
                            Data.film_data[kategori][kode]["status"] = "Tersedia"
                            print(f"Film '{Data.film_data[kategori][kode]['judul']}' berhasil dikembalikan!")
                        else:
                            print("Film belum disewa.")
                    else:
                        print("Kode film tidak ditemukan.")
                    input("Tekan Enter untuk kembali...")

                elif pilih_kat == "4" and Data.Role == "Admin":
                    tambah_film(kategori)
                    input("Tekan Enter untuk kembali...")

                elif pilih_kat == "5" and Data.Role == "Admin":
                    hapus_film(kategori)
                    input("Tekan Enter untuk kembali...")

                elif pilih_kat in ["4", "6"]:
                    break

                else:
                    print("Pilihan tidak valid.")
                    input("Tekan Enter untuk kembali...")

            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
                input("Tekan Enter untuk kembali...")
