
# # Membuat set
# buah = {"apel", "jeruk", "mangga", "apel"}
# print(buah)

# for i in buah:
#     print (i , end='')

# angka =[1,1,2,5,2,3,6]
# unik=set(angka)
# print(unik)

# Daftar_Buku={
#     "Buku1":"Bumi Manusia",
#     "Buku2": "Laut Bercerita"
# }

# print(Daftar_Buku["Buku1"])

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {"Instagram" : "daffahrhap"}
# }

# print(Biodata)

#Print (Biodaya)
# for i,j in Biodata.items(): 
#     print(i)  #Karena i itu indeks (Nama,NIM DLL)
#     print(j) #Karena J itu valuenya , dengan catatan harus pake biodata.items


# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get('Nama'))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"}

# # del Film['The Conjuring']
# # print(Film)

# Hapus=Film.pop["The Conjuring"]
# print(Film)
# print(Hapus)

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# Film.update({"Big Man": "Action"})
# #Setelah Ditambah
# print(Film)


# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][0])

# angka=set()  #Kalo mau bikin set kosong
# angka={1,2,3} #dia jadi ditch karena dia pake kurung kurawal

# print(type(angka))

# a={10,11,12}
# b={11,13,14}
# c= a | b #& ini irisan jadi dia ngeprint angka yang sama
# print(c)

#SET DEFAULT

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }


# print(Nilai)
# print("")

# print("Nilai : ", Nilai.setdefault("Kimia", 70))








