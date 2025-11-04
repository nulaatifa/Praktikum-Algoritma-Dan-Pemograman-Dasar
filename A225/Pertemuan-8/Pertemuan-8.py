
num = int("42") # 42
name = str(123) # "123"
data = list("abc") # ['a', 'b', 'c']
data = dict(a=1, b=2) # {'a': 1, 'b': 2}

angka=20

buah=frozenset({"apel","apel","jeruk","Mangga"})
buahset=list(buah)
print(type(buah))

# abs(-9) # 9
# max([1, 3, 7]) # 7
# min([1, 3, 7]) # 1
# round(3.14159,2) # 3.14
# sum([1, 2, 3]) # 6
# print(sum([1,2,3])) #Kalo cuma print(sum) dia outputnys <built-in function abs> gitu dia karena nilai sum itu menyimpan dirinya sendiri, kalo ngikut print yang print(sum[1,2,3]) dia nanti ngitung  nilainya makanya outputnya 6
# print(round(3.14159,2))

# angka=[1,2,3,4,5]
# angka=-3.2456
# angka=3


# for i, v in enumerate(['a','b']):
#     print(i, v) # 0 a , 1 b

# len([10, 20, 30]) # 3
# list(map(str, [1,2,3])) # ['1', '2', '3']
# sorted([3, 1, 2]) # [1, 2, 3]
# list(zip([1,2],['a','b'])) # [(1,'a'), (2,'b')]
# print(len([10,20,30]))

buah=["apel","pisang","mangga"]

# for i ,item in enumerate(buah):
#     print (i,item)

angka=[1,2,3,4,5,6]
genap=filter(lambda x: x%2 == 0, angka)

angka=[10,20,30]
it=iter(angka)
print(next(it))
print(next(it))

# x = 42
# def fungsi():
#     x = 10
#     y = 20
#     z = 30
#     print(globals()['x']) # mendapatkan isi dari variabel x (global)
#     print(locals()['x']) # mendapatkan isi dari variabel x (lokal)
#     print(locals()) # {'x': 10, 'y': 20, 'z': 30}
# fungsi()

# print ("HELLO".lower()) 
# print("hello".upper())
# print("hi   ".strip())
# print("aku belajar python".replace("belajar", "jago"))
# print("a,b,c".split(","))
# print(",".join(['a','b','c']))
# print("hello".find("e"))
# print("hello".startswith("he"))
# print("hello.py".endswith(".py"))

# nama="DaFFa anak jahat"
# print(nama.lower)
# print(nama.upper)
# print(nama.strip)
# print(nama.replace('jahat','baik'))

# huruf= "a,b,c"
# print(huruf.split(","))
# print(nama.find('Z')) #Kalo engga ada dia muncul -1

import math
from math import sqrt
import math as m

print(m.sqrt(16))
print(m.factorial(5))

import random
print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4

pilih_acak = ["pisang", "rambutan", "manggis"]
acak = "apcb"
print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
print(random.choice(acak)) # memilih 1 karakter acak pada string

# # memasukkan satu persatu nilai dari kumpulan_angka
# # ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
# kumpulan_angka = "1234567890"
# hasil = ""
# for i in range(4):
#     hasil += random.choice(kumpulan_angka)
# print(hasil)

acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang berubah
print(acak_kartu)

from datetime import datetime
print(datetime.now())
waktu = datetime.now()
print(waktu.strftime("%d/%m/%Y, %H:%M:%S"))

# import inquirer
# pertanyaan = [
# inquirer.List(
# 'size',
# message="What size do you need?",
# choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
# ),
# ]
# # mendapatkan jawaban
# answer = inquirer.prompt(pertanyaan)
# print(answer) # Output dalam bentuk Dictionary {'size': 'Large'}
# print(answer['size']) # Ambil value dari key 'size' (Large)


# import inquirer
# # deklarasi struktur dictionary
# data = {
# 'nama': [],
# 'nim': [],
# 'no_hp': []
# }

# def tambahData():
#     questions = [
#         inquirer.Text('nama', message="Input nama mu"),
#         inquirer.Text('nim', message="Input NIM kamu"),
#         inquirer.Text('no_hp', message="Input nomor hp kamu",)
#         # hasil dari semua input diatas adalah:{'name': 'nilai dari input name', 'nim': 'nilai dari input nim','no_hp': 'nilai input no_hp'}
#     ]
    
#     answers = inquirer.prompt(questions) # hasil input akan disimpan ke dalam variabel answer 
    
#     # tambahkan isi dari list, sesuai key nya masing-masing
#     data['nama'].append(answers['nama'])
#     data['nim'].append(answers['nim'])
#     data['no_hp'].append(answers['no_hp'])


# # panggil fungsi
# tambahData()
# # contoh jika ingin melihat isi dari dictionary data dengan key 'nama'
# print(f"List nama:")
# for i, nama in enumerate(data['nama']):
#     print(f"{i+1}. {nama}")
#     print(f"   NIM  : {data['nim'][i]}")
#     print(f"   No HP: {data['no_hp'][i]}")


# #STUDI KASUS 1
# import random

# karakter = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&"
# kata_sandi = ""

# for i in range(12):
#     kata_sandi += random.choice(karakter)

# print(kata_sandi) 

# #Studi Kasus 2
# from datetime import datetime
# waktu = datetime.now()
# print(waktu.strftime("%d/%m/%Y, %H:%M:%S"))














import random
karakter = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&"
kata_sandi = ""
Pilih=it(input("Pilihan"))

for i in range(1,12):
    kata_sandi +=random.choice(karakter)

print(kata_sandi)
