
from Data import Akun, Role, Username
import os 
from time import sleep


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
                    import Data
                    Data.Role = Role
                    Data.Username = Username
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