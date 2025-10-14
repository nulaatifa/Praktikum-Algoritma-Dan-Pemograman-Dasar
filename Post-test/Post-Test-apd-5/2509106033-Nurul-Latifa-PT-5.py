import os
from time import sleep

Film_List_Studio_Ghibli=[
    ['F001',"My_Neighboor_Totoro","Sedang Disewa"],
    ['F002',"Howl_The_Moving_Castle","Tersedia"],
    ['F003',"The_Wind_Rises","Tersedia"],
    ['F004',"Sprited_Away","Sedang Disewa"],
    ['F005',"Grave_Of_The_Fireflies","Sedang Disewa"]
]

Film_List_Marvel_Studio=[
    ['F006',"Spider-Man:_Across_The_Spider-Verse","Sedang Disewa"],
    ['F007',"Captain_America:_Civil_War","Tersedia"],
    ['F008',"The_Amazing_Spider-Man ","Tersedia"],
    ['F009',"Iron_Man_1","Tersedia"],
    ['F010',"Doctor_Strange","Sedang Disewa"],
]

Film_List_Pixar=[
    ['F011',"UP!","Tersedia"],
    ['F012',"Cars","Sedang Disewa"],
    ['F013',"Inside_Out!","Tersedia"],
    ['F014',"Monster,INC","Tersedia"],
    ['F015',"Ratatouille","Tersedia"]
]

Film_List_Disney=[
    ['F016',"Wish","Tersedia"],
    ['F017',"Zootopia","Sedang Disewa"],
    ['F018',"Frozen 1","Tersedia"],
    ['F019',"Moana","Sedang Disewa"],
    ['F020',"Tangled","Sedang Disewa"]
]

print("======= MENU UTAMA ======")
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("\n ----------------------------------")
    print("\n ======= TOKO PENYEWAAN FILM =======")
    print("\n ----------------------------------")
    print("1. Studio Ghibli")
    print("2. Marvel Studio")
    print("3. Pixar")
    print("4. Disney")
    print("5.Keluar")
    Kategori=input("Pilih Kategori Film (1-5):   ")

    if Kategori == "1":
        Film_List= Film_List_Studio_Ghibli
        Nama_Kategori= "Studio Ghibli"
    elif Kategori == "2":
        Film_List = Film_List_Marvel_Studio
        Nama_Kategori = "Marvel Studio"
    elif Kategori == "3":
        Film_List = Film_List_Pixar
        Nama_Kategori = "Pixar"
    elif Kategori == "4":
        Film_List = Film_List_Disney
        Nama_Kategori = "Disney"
    elif Kategori == "5":
        print("Terimakasih Telah Mengunjungi Toko Kami")
        break
    else:
        print("Maaf Pilihan Tidak Valid, Mohon Coba Lagi")
        print("Tekan Enter Untuk Kembali Ke Menu Utama...")
        continue
    
    print("====== MENU KATEGORI ======")
    
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"------ MENU {Nama_Kategori.upper()} ------")
        print("1. Lihat Daftar Film")
        print("2. Sewa Film")
        print("3. Kembalikan Film")
        print("4. Tambah Film Baru")
        print("5. Hapus Film")
        print("6. Kembali Ke Menu Utama")
        Pilih= input("Pilih Menu Kategori (1-6):  ")
        
        if Pilih == "1":
            print(f"====== DAFTAR FILM {Nama_Kategori.upper()} ======")
            print("Kode\t\tJudul\t\t\tStatus")
            print("----------------------------------------------------------------")
            for Film in Film_List:
                print(f"{Film[0]}\t {Film[1]:25} \t{Film[2]}")
            input("Tekan Enter Untuk Kembali Ke Menu Kategori...")
            
        elif Pilih == "2":
            Kode=input("Masukan Kode Film Yang Ingin Disewa:  ")
            Ditemukan=False
            for Film in Film_List:
                if Film[0] == Kode:
                    Ditemukan = True
                    if Film[2] == "Tersedia":
                        Film[2] = "Sedang Disewa"
                        print (f"Film '{Film[1]}' Berhasil Disewa !!")
                    else:
                        print("Film Sedang Disewa Orang Lain")
                    break
            if Ditemukan == False:
                print("Mohon Maaf Film Tidak Ditemukan")
            input("Tekan Enter Untuk Kembali Ke Menu Kategori...")
            
        elif Pilih == "3":
            Kode = input("Masukan Kode Film Yang Ingin Dikembalikan:  ")
            Ditemukan = False
            for Film in Film_List:
                if Film[0] == Kode:
                    Ditemukan = True
                    if Film[2] == "Sedang Disewa":
                        Film[2] = "Tersedia"
                        print(f"Film '{Film[1]}' Berhasil Dikembalikan !!")
                    else:
                        print("Film Belum Disewa")
                    break
            if Ditemukan == False:
                print("Mohon Maaf Film Tidak Ditemukan")
            input("Tekan Enter Untuk Kembali Ke Menu Kategori...")
                
        elif Pilih == "4":
            Kode=input("Masukan Kode Film Baru:  ")
            Judul=input("Masukan Judul Film Baru :  ")
            Film_List.append([Kode,Judul,"Tersedia"])
            print(f"Film '{Judul}' Berhasil Ditambahkan !!")
            input("Tekan Enter Untuk Kembali Ke Menu Kategori...")
            
        elif Pilih == "5":
            Kode=input("Masukan Kode Film Yang Ingin Dihapus Dari Daftar :  ")
            Ditemukan = False
            for Film in Film_List:
                if Film[0] == Kode:
                    Film_List.remove(Film)
                    Ditemukan = True
                    print(f"Film '{Film[1]}' Berhasil Di Hapus Dari Daftar!!")
                    break
            if Ditemukan == False:
                print("Mohon Maaf Film Tidak Ditemukan")
            input("Tekan Enter Untuk Kembali Ke Menu Kategori...")
                
        elif Pilih == "6":
            break
        else:
            print("Pilihan Tidak Valid")
            print("Tekan Enter Untuk Kembali Ke Menu Kategori...")


sleep(5)
os.system("cls" if os.name == "nt" else "clear")


            
                








