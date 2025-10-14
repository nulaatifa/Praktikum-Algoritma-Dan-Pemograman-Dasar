#Membuat List
# Mata_Kuliah=["APD","KALKULUS","ORSIKOM"]
# Mata_Kuliah1=[]

# #Membaca List

# # print(Mata_Kuliah[1:3])

# print(Mata_Kuliah[0])

# # print(Mata_Kuliah[1:3:2])

# Mata_Kuliah.append("Matematika") 

# print(Mata_Kuliah)



# # list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# # Tambahkan Web
# studyclub.append("Web")
# print(studyclub)
# # output
# ['Data Science', 'Robotics', 'Multimedia', 'Network', 'Web']

# # list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# # Tambahkan Web
# studyclub.insert(2,"Web")
# print(studyclub)

# # list awal
# studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# print(studyclub)

# studyclub[2] = "AI"
# print(studyclub)



# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
# # print(matakuliah)     

# # # del matakuliah[2]
# # print(matakuliah)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']

# for index,i in enumerate(matakuliah):
#     print(index,i)

# for i in matakuliah:
#     print(f"Print Mata Kuliah {i}")
# print(matakuliah)
# # print(matakuliah)

#  matakuliah.remove('Kalkulus')
# matakuliah.pop(3)

# hapus=matakuliah.pop(3)
# print(matakuliah)

# list=[1,2,3]

# print(sum(list)/len(list))

# print()

# list=[1,2,3]
# nilai=[4,5,6]

# hasil=list+nilai
# kali=list*3
# print(hasil)

# print(f"Ini hasil penjumlahan list {hasil}")
# print(f"ini hasil Perkalian list {kali}")

# kelas = [
#     ["Ridho", "Lian", "Nabil"],
#     ["Daffa", "Dante", "Santoso"],
#     ["Pernanda", "Riyadi", "Ahnaf"],
# ]

# for i in kelas:
#     for nama in i:
#         print(nama)

# kelas[1].insert(1,"Bakil")
# print(kelas[1])

#TUPLE

# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))

# print(anggota[4][0])
# print(anggota[5][0])
# print(anggota[-1])


# studyclub = ("Data Science", "Robotics", "Multimedia", "Network")

# liststudy=list(studyclub)

# liststudy[1]= "Web"

# tuplestudy=tuple(liststudy)

# print(f"ini tuple :{studyclub}")
# print(f"ini list = {liststudy}")
# print(f"ini tuple = {tuplestudy}")

#STUDY KASUS 

# keranjang=["Brokoli","Apel","Jamur","Nanas","Wortel","kiwi","kol","sawi","Lobak"]

# for i in keranjang:
#     for keranjang in i:
#         print(keranjang)