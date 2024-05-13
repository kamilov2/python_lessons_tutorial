
# 6 - mavzu
# for va while looplar

#for va while looplar Python dasturlash tilida takrorlashni boshqarish uchun ishlatiladi.

# for loop: 
# for loopi qo'shimcha elementlar (masalan, ro'yxat, tuple yoki  elementlari) orasida takrorlash imkonini beradi.


# Misol:

# fruits = ["apple", "banana", "cherry"]
# for i in fruits:
#     print(i)

# Natija:

# apple
# banana
# cherry

# while loop: while loopi takrorlanuvchi qismni takrorlashni davom ettiradi, toki shart bajarilishi True qiymatga teng bo'lgan holda.
    

# Misol:

# i = 5
# x = 10
# while i != x:
#     print(i)
#     i += 1

# Natija:

# 0
# 1
# 2
# 3
# 4


# for loopi bilan kod oddiyroq va qulayroq ko'rish mumkin, ammo shart bajarilishidagi shart bilmaydigan holatlarda while loopi afzalroq bo'ladi.
# for loopi elementlar ro'yxatida takrorlanadigan holatlar uchun yaxshi, while loopi esa shart bajarilishini tanlash lozim bo'lgan takrorlashlarni boshqarishda foydalaniladi.
    


# 7 - mavzu
# break va continue operatorlari
# break va continue operatorlari Python dasturlash tilida takrorlashdan chiqish va takrorlashni keyingi takrorlashga o'tkazish imkonini beradi.
    
# break operatori:

# break operatori takrorlashdan chiqishga olib keladi. U bajarilgan joyda takrorlashni to'xtatadi va takrorlashdan chiqib kodning keyingi qismiga o'tib boradi.
# Agar shart bajarilishidan oldin takrorlashdan chiqishni talab qilinsa, break operatori ishlatiladi.
    

# Misol:
# for i in range(5):
#     if i == 3:
#         break
#     print(i)

# Natija:

# 0
# 1
# 2
    

# continue operatori:

# continue operatori takrorlashni to'xtatib kodning keyingi qismiga o'tkazadi, lekin takrorlash joriy qismni takrorlashni to'xtatmaydi.
# Agar takrorlash joriy qismni o'tkazish va keyingi takrorlashni boshlashni talab qilinsa, continue operatori ishlatiladi.


# Misol:

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# Natija:

# 0
# 1
# 2
# 4
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]
# y = 0
# for i in x:
#     if i % 2 == 0:
#         print(i)
#         y += i
# print('Qoldiksiz bolinadigon sonlar qiymati: ', y, 'ga teng')

x = ['apple', 'hello', 'world', 'banana', 'ananas']

#list ichida for loop orqali A harfi bilan boshlanadigon sozlarni print qilinsin