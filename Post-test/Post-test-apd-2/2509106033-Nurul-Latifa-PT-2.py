
#Tugas Postes APD 2
#Membuat Program Biodata Diri

print("Biodata Diri")
print("Nama Lengkap:")
Nama_Lengkap = input()
print("Umur:")
umur = int(input())
print("Jenis Kelamin:")
Jenis_Kelamin = input()
print("Tinggi Badan(cm):")
Tinggi_Badan = float(input() )
print("Berat Badan(kg):")
Berat_Badan = float(input())
print("Status Mahasiswa Aktif:")
Status_Mahasiswa_Aktif = (input().lower() == 'true')
print("Status Mahasiswa Aktif:" + str(Status_Mahasiswa_Aktif))
print("MengikutiOrganisasi:")
Mengikuti_Organisasi = (input().lower() == 'true')
print("Mengikuti Organisasi:" + str(Mengikuti_Organisasi))
print("Asal Daerah:")
Asal_Daerah = input()
print("Program Studi:")
Program_Studi = input()
print("Makanan Kesukaan:")
Makanan_Kesukaan = input()
print("Warna Kesukaan:")
Warna_Kesukaan = input()
print("Zodiak:")
Zodiak = input()
print("Biodata Selesai, Terimakasih Telah Mengisi Biodata")





#Hasil Output Biodata Diri

print("(-----------------------------------------------------------  )")
print("            BIODATA DIRI           ")
print("(-----------------------------------------------------------)")

print(f" {'Nama Lengkap':15}      : {Nama_Lengkap:25} ")
print(f" {'Umur':15}        : {umur:<25} ")
print(f" {'Jenis Kelamin':15}      : {Jenis_Kelamin:<25} ")
print(f" {'Tinggi Badan(cm)':15}      : {Tinggi_Badan:<25} ")
print(f" {'Berat Badan(kg)':15}      : {Berat_Badan:<25} ")
print(f" {'Status Mahasiswa':15}   : {Status_Mahasiswa_Aktif:<25} ")
print(f" {'Mengikuti Organisasi':15} = {Mengikuti_Organisasi:<25} ")
print(f" {'Asal Daerah':15}       = {Asal_Daerah:25} ")
print(f" {'Program Studi':15}      = {Program_Studi:25} ")
print(f" {'Makanan':15}       = {Makanan_Kesukaan:25} ")
print(f" {'Warna':15}       = {Warna_Kesukaan:25} ")
print(f" {'Zodiac':15}       = {Zodiak:25} ")
print("---------------------------------------------------------------")
print("   Biodata selesai, terimakasih!   ")


