import os
from time import sleep

Username="Nurul"
Password="033"
Login_Berhasil= False

for i in range (0,5):
    print("-------------- MENU LOGIN -----------------")
    Y=input("MASUKAN USERNAME:     ")
    U=input("MASUKAN PASSWORD:     ")

    if Y == Username and U == Password:
        print("Login Anda Valid")
        Login_Berhasil = True
        break
    else:
        print("Login Anda Tidak Valid")

if Login_Berhasil == True:
    while True:
        print("------------- MENU UTAMA -------------")
        print("(1) Masuk Ke Program Rental Mobil")
        print("(2) Keluar Dari Program Rental Mobil")

        Pilihan=input("Pilih Menu (1/2):    ")

        if Pilihan == "1":
            print("--- SISTEM RENTAL MOBIL ---")

            Usia = int(input("Masukan Umur Customer: "))
            if Usia < 21:
                hasil = ("Tolak: Usia Tidak Cukup")
            else:
                SIM = input("Masukan Jenis SIM: ").upper()
                if SIM != "A":
                    hasil = ("Tolak: Tidak Memiliki SIM A")
                else:
                    Deposit = int(input("Masukan Besar Deposit Anda: "))
                    if Deposit < 500000:
                        hasil = ("Tolak: Deposit Tidak Cukup")
                    else:
                        Pengalaman = float(input("Masukan Pengalaman Mengemudi (tahun): "))
                        if Pengalaman < 4:
                            hasil =("Setujui Untuk Mobil Standar Saja")
                        else:
                            hasil =("Setujui Untuk Semua Jenis Mobil")

            print("----- HASIL EVALUASI -----")
            print(hasil)
            print("Kembali ke Menu Utama...")

        if Pilihan == "2":
            print("Terima kasih, sampai jumpa kembali")
            break
else:
    print("Anda sudah 5 kali salah. Program berhenti.")
            




sleep(5)
os.system('cls')

