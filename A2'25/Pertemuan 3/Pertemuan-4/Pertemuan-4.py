

#PERULANGAN FOR

# for i in range(10):
#     print(i+1)

#[0,1,2,3,4,5,6,7,8,9]
# for j in range(1,11,2):  #ini dia jadi ganjil #sama kalo tulis  for i in range(1,10), outputnya jadi 1-9, jadi harus kasih 11 atau lebih supaya jadi ke angka yang kita mau
#     print(j)

#for loop untuk list
# nama=('haikal','diftya','anugrah')

# for i in nama:
#     print(i)

# for j in range(5):    #J/i itu variable yang menanmpung banyak perulangan
#     print("Rafi")

#PERULANGAN WHILE
#While loop

# Jawab="ya"
# Hitung=0

# while(Jawab == 'ya'):
#     Hitung+=1
#     Jawab = input("Ulang lagi?  :  ")

# print(f"Total jawab ya {Hitung}")


# cuaca="hujan"

# while(cuaca == "hujan" or  cuaca =="Hujan"):
#     print("Jangan Keluar Rumah")
#     cuaca == input("Apa cuaca hari ini:  ")

# print("Pergi Keluar Rumah")

# angka=10

# while (angka >1):
#     print(angka)
#     angka -=2

# for i in range(1,5):
#     for j in range(1,5):
#         print(f"{i} x {j} = {i*j}")
#     print()


#Control Perulangan
#break

# Angka=[2 ,5 ,8 ,12 ,15 ,7 ,20]

# print("Mencari angka yang lebih besar dari 10.....")

# for i in Angka:
#     print(f"Memeriksa Angka {i}")
#     if i >10:
#         print(f"{i} lebih besar daru 10")
#         break            #ITU kayak memberhentikan terpaksa kalo misalnya dia sudah nemu angka yang lebih besar dari 10/sesuai dengan kondisi yang di mau dia langsung berhenti engga lanjut ke angka selanjutnya

# print("Program Selesai")

# for i in range(1,11):
#     if i % 2 !=0:      #Modulus(%) itu dibagi/pembagian
#             continue    #oo kayak melompat gitu jadi dia langsung balik ke atas engga lanjut ke print,kalo sesuai dia masuk ke continue jadi ulang ulang terus kalo misalnya tidak sesuai dia lanjut ke print, angka ganjil dilewatin
#     print (f'Angak genap ditemukan yaitu : {i}')

# print("Program Selesai")

# for i in range(1,11):
#     if i % 2 ==0:      #Modulus(%) itu dibagi/pembagian
#             continue    #oo kalo misalnya dia sesuai kondisinya dia continue lanjut yang dibawah dilewatin
#     print (f'Angak ditemukan yaitu : {i}')

# print("Program Selesai")

#list comprehension

# kuadrat= [i**2 for i in range(1,6)]
# print(kuadrat)

# angka_genap=[x for x in range(1,11) if x%2==0]   #ini versi pake list comprehension
# print(angka_genap)

# for x in range(1,11):    #ini versi biasa pake if
#     if x%2==0:
#         print(x)

# angka_ganjil=[x for x in range(1,13) if x%2 !=0]
# print(angka_ganjil)

# for i in range(1,6):
#     print('**{i}')

# s
# a=5
# for i in range(1,6):
#     print







