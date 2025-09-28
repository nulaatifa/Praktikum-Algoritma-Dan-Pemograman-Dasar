
print("--- SISTEM RENTAL MOBIL ---")

Usia=int(input("Masukan Umur Customer:   "))
if Usia<21:
    hasil=("Tolak: Usia Tidak Cukup")
else:
    SIM=str(input("Masukan Jenis SIM:   ").upper())
    if SIM !="A":
        hasil=("Tolak: Tidak Memiliki SIM A")
    else:
        Deposit=int(input("Masukan Besar Deposit Anda:   "))
        if Deposit<500000:
            hasil=("Tolak: Deposit Tidak Cukup")
        else:
            Pengalaman_Mengemudi=float(input("Masukan Pengalaman Mengemudi Anda:  "))
            if Pengalaman_Mengemudi<4:
                hasil=("Setujui Untuk Mobil Standar Saja")
            else:
                hasil=("Setujui Untuk Semua Jenis Mobil")

print("----- HASIL EVALUASI -----")
print(hasil)