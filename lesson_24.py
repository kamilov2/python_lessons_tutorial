# import datetime
# import time
# fayl ochib ichida agar malumot mavjud bolsa ochirib tashlab boshqatdan malumot yozishga
file_path = 'main.py'
content = '''import random

print(random.randint(1,10))'''

file = open(file_path, 'w')
file.write(content)
file.close()

# Fayl qiymatini ichidagi malumotini oqish
file = open(file_path, 'r')
file_content = file.read()
print("Fayl qiymati: ")
print(file_content)
file.close()

# faylni qatorlar boyicha oqish
# file = open(file_path, 'r')
# lines = file.readlines()
# print("fayl qatorlari")
# print(lines)
# for line in lines:
#     print(line.strip())  
# file.close()

# Yozilgan ichida qiymat bor faylga qiymat qoshib ketish
additional_content = '\nimport random'
file = open(file_path, 'a')
file.write(additional_content)
file.close()


# Fayl nusxa olib boshqa fayl ochib kochirib otish

# Faylni boshqa joyga kochirish
# shutil.move(file_path, 'C:/Users/Gnom/Desktop/')
# print("Fayl kochirildi")

# Faylar ni ochirish
# import os

# os.remove(file_path)
# print("Fayl ochirildi!")

# file = open('time1.txt', 'r')

# with open('time1.txt', 'r') as file:
#     print(file.read())
    

# file_path2 = 'time2.txt'
# file1 = open(file_path2, 'w')
# file1.write(s)
# file1.close()

# import shutil

# shutil.copy(file_path, 'main_2.py')
# print("Fayldan nusxa olindi")


client = {
    '65845':{"Ism":"Abubakr", "Familiya":"Odilov","Yosh":18,"Telefon_raqam":+998900000000, 'Royhatdan_otgan_sana':"2024-11-05 14:23:12"},
    '65845':{"Ism":"Abubakr", "Familiya":"Odilov","Yosh":18,"Telefon_raqam":+998900000000, 'Royhatdan_otgan_sana':"2024-11-05 14:23:12"},
}