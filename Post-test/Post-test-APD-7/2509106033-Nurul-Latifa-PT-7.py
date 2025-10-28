
import os
from time import sleep


Akun = {
    "Admin" : {"Password" : "0090", "Role" : "Admin"},
    "User" : {"Password" : "8809", "Role" : "User"}
}

film_data = {
    "Studio Ghibli": {
        "F001": {"judul": "My Neighbor Totoro", "status": "Sedang Disewa"},
        "F002": {"judul": "Howl The Moving Castle", "status": "Tersedia"},
        "F003": {"judul": "The Wind Rises", "status": "Tersedia"},
        "F004": {"judul": "Spirited Away", "status": "Sedang Disewa"},
        "F005": {"judul": "Grave Of The Fireflies", "status": "Sedang Disewa"},
    },
    "Marvel Studio": {
        "F006": {"judul": "Spider-Man: Across The Spider-Verse", "status": "Sedang Disewa"},
        "F007": {"judul": "Captain America: Civil War", "status": "Tersedia"},
        "F008": {"judul": "The Amazing Spider-Man", "status": "Tersedia"},
        "F009": {"judul": "Iron Man 1", "status": "Tersedia"},
        "F010": {"judul": "Doctor Strange", "status": "Sedang Disewa"},
    },
    "Pixar": {
        "F011": {"judul": "UP!", "status": "Tersedia"},
        "F012": {"judul": "Cars", "status": "Sedang Disewa"},
        "F013": {"judul": "Inside Out!", "status": "Tersedia"},
        "F014": {"judul": "Monster, INC", "status": "Tersedia"},
        "F015": {"judul": "Ratatouille", "status": "Tersedia"},
    },
    "Disney": {
        "F016": {"judul": "Wish", "status": "Tersedia"},
        "F017": {"judul": "Zootopia", "status": "Sedang Disewa"},
        "F018": {"judul": "Frozen 1", "status": "Tersedia"},
        "F019": {"judul": "Moana", "status": "Sedang Disewa"},
        "F020": {"judul": "Tangled", "status": "Sedang Disewa"},
    }
}

Role = None
Username = None



def tampilkan_kategori():
    print("\nMENU KATEGORI FILM:")
    for i, kategori in enumerate(film_data.keys(), start=1):
        print(f"{i}. {kategori}")

def tampilkan_daftar_film(kategori):
    try:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\nDAFTAR FILM {kategori.upper()}")
        print("Kode\tJudul Film\t\t\tStatus")
        print("-------------------------------------------")
        for kode, data in film_data[kategori].items():
            print(f"{kode}\t{data['judul']:25}\t{data['status']}")
    except KeyError:
        print("Kategori tidak ditemukan!")
    input("Tekan Enter untuk kembali...")

def tambah_film(kategori):
    global film_data
    kode = input("Masukkan kode film baru: ")
    if kode in film_data[kategori]:
        print("Kode film sudah ada.")
    else:
        judul = input("Masukkan judul film: ")
        film_data[kategori][kode] = {"judul": judul, "status": "Tersedia"}
        print(f"Film '{judul}' berhasil ditambahkan!")

def hapus_film(kategori):
    global film_data
    
    kode = input("Masukkan kode film yang ingin dihapus: ")
    if kode in film_data[kategori]:
        judul = film_data[kategori][kode]["judul"]
        del film_data[kategori][kode]
        print(f"Film '{judul}' berhasil dihapus.")
    else:
        print("Kode film tidak ditemukan.")

def countdown(n):  
    if n == 0: 
        print("Logout berhasil!\n")
        return
    print(f"Logout dalam {n} detik...")
    sleep(1)
    countdown(n - 1)

def login():
    global Username, Role
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            print("\n====== Selamat Datang Di Toko Penyewaan Film ======")
            print(" 1. Login")
            print(" 2. Register")
            print(" 3. Keluar")
            pilihan = input("Pilih Menu (1-3): ")

            if pilihan == "1":
                Username = input("Masukkan Username: ")
                Password = input("Masukkan Password: ")
                if Username in Akun and Akun[Username]["Password"] == Password:
                    Role = Akun[Username]["Role"]
                    print(f"\nLogin berhasil! Selamat datang, {Username} ({Role})")
                    sleep(2)
                    return
                else:
                    print("\nUsername atau Password salah!")
                    input("Tekan Enter untuk coba lagi...")

            elif pilihan == "2":
                Username_Baru = input("Masukkan username baru: ")
                if Username_Baru in Akun:
                    print("Username sudah terdaftar.")
                    sleep(2)
                    continue
                Password_Baru = input("Masukkan Password baru: ")
                Akun[Username_Baru] = {"Password": Password_Baru, "Role": "User"}
                print("Akun berhasil dibuat. Silakan login ulang.")
                sleep(2)

            elif pilihan == "3":
                print("Terima kasih telah datang !!")
                sleep(2)
                os.system("cls" if os.name == "nt" else "clear")
                exit()

            else:
                raise ValueError("Pilihan tidak valid!") 

        except ValueError as e:
            print(f"Error: {e}")
            input("Tekan Enter untuk lanjut...")


def menu_utama():
    global Role
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        tampilkan_kategori()
        print("5. Logout")
        pilihan = input("Pilih kategori (1-5): ")

        kategori_keys = list(film_data.keys())
        kategori_dict = {str(i+1): kategori_keys[i] for i in range(len(kategori_keys))}

        if pilihan in kategori_dict:
            kategori = kategori_dict[pilihan]
        elif pilihan == "5":
            countdown(5)
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
            if Role == "Admin":
                print("4. Tambah Film")
                print("5. Hapus Film")
                print("6. Kembali")
            else:
                print("4. Kembali")

            pilih_kat = input("Pilih menu: ")
            
            kode = ""
            judul = ""

            try:
                if pilih_kat == "1":
                    tampilkan_daftar_film(kategori)

                elif pilih_kat == "2":
                    kode = input("Masukkan kode film: ")
                    if kode in film_data[kategori]:
                        if film_data[kategori][kode]["status"] == "Tersedia":
                            film_data[kategori][kode]["status"] = "Sedang Disewa"
                            print(f"Film '{film_data[kategori][kode]['judul']}' berhasil disewa!")
                        else:
                            print("Film sedang disewa orang lain.")
                    else:
                        print("Kode film tidak ditemukan.")
                    input("Tekan Enter untuk kembali...")

                elif pilih_kat == "3":
                    kode = input("Masukkan kode film: ")
                    if kode in film_data[kategori]:
                        if film_data[kategori][kode]["status"] == "Sedang Disewa":
                            film_data[kategori][kode]["status"] = "Tersedia"
                            print(f"Film '{film_data[kategori][kode]['judul']}' berhasil dikembalikan!")
                        else:
                            print("Film belum disewa.")
                    else:
                        print("Kode film tidak ditemukan.")
                    input("Tekan Enter untuk kembali...")

                elif pilih_kat == "4" and Role == "Admin":
                    tambah_film(kategori)
                    input("Tekan Enter untuk kembali...")

                elif pilih_kat == "5" and Role == "Admin":
                    hapus_film(kategori)
                    input("Tekan Enter untuk kembali...")

                elif (pilih_kat == "4" and Role == "User") or (pilih_kat == "6" and Role == "Admin"):
                    break

                else:
                    print("Pilihan tidak valid.")
                    input("Tekan Enter untuk kembali...")
            
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")
                input("Tekan Enter untuk kembali...")


if __name__ == "__main__":
    login()
    menu_utama()

    sleep(1)
    os.system("cls" if os.name == "nt" else "clear")