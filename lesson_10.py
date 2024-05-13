import random
# Yoki, agar modul nomi uzun bo'lsa:

import random as l
# Bunday, siz modulga o'z nomi orqali murojaat qilishingiz mumkin.

# Agar faqatgina bazi funksiyalarni yoki o'zgaruvchilarni import qilmoqchi bo'lsangiz:


# from random import funksiya_nomi, ozgaruvchi_nomi
# Shuningdek, agar barcha narsalarni moduldan import qilmoqchi bo'lsangiz:


from random import *
# Bu, modulning barcha narsalarini o'z ichiga oladi, lekin bundan foydalanishni tavsiya etilmaydi, chunki u o'zgaruvchilarni, funksiyalarni yoki klasslarni yozuvi qotib ketishi mumkinligi uchun kodni qiyinchilikka solishi mumkin.

# Python standart kutubxonasi katta vaqt bo'ylarida o'z ichiga ko'plab modullarni o'z ichiga oladi, misol uchun math, random, os, sys va hokazo.

import random
# randint(a, b): A va B orasidagi tasodifiy butun sonni qaytaradi (A va B o'z ichiga kirishi mumkin)

print(random.randint(0, 9999))  # Masalan, 0 dan 9999 gacha tasodifiy son

# random(): 0 va 1 orasidagi tasodifiy sonni qaytaradi.

print(random.random())  # Masalan, 0 dan 1 gacha tasodifiy son

# choice(seq): Berilgan ro'yxatdan tasodifiy bir elementni tanlaydi.

my_list = ['+998902225561', '+982656565', '+656565911']
print(random.choice(my_list))  # Ro'yxatdan tasodifiy element tanlash


my_list = ['apple', 'banana', 'cherry']
random.shuffle(my_list)
print(my_list)  # Ro'yxatni tasodifiy tartibda tartiblash

# sample(population, k): Berilgan ro'yxatdan k ta tasodifiy elementni qaytaradi.

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(random.sample(my_list, 2))  # 2 ta tasodifiy elementni tanlash

