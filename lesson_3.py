# 1 - mavzu

# print() funksiyasi Python dasturlash tili uchun juda muhim va ko'p ishlatiladigan bir funksiya. U bu funksiya orqali ma'lumotlarni konsolga chiqarish uchun ishlatiladi.
# Misol:

print("Hello, World!")

# Bu kod natijada Hello, World! matnini konsolga chiqaradi. print() funksiyasi matnlarni konsolga chiqarishda vaqtincha o'zgaruvchilarni aniqlashda juda qulay va ko'p ishlatiladi.
# print() funksiyasiga ikkita yoki undan ko'p argument (ma'lumot) berishingiz mumkin. Ularning orasida vergul bilan ajratilgan holda bo'lishi kerak. 
# Misol:
name = "John"
age = 30
print("Name:", name, "Age:", age)


# 2 - mavzu 
#O'zgaruvchilarni tog'ri nomlash

# O'zgaruvchini nomlashda quyidagi amallar mumkin:


# Harf, raqam va pastki chiziqchalardan iborat bo'lish.
# Katta harf bilan boshlanish (masalan, Name uchun name).
# Pastki chiziqcha ('_') bilan ajratish (masalan, user_name).
# O'zgaruvchi nomi raqam bilan boshlanmasligi.
# O'zgaruvchining tushunadigan va umuman ishlatiladigan maqsadni ifodalaydigan nom.
# Pythonning maxsus funksiyalarini nomlashda ishlatiladigan so'zlar yoki qisqartmalar (masalan, list, str, int, print kabi) o'zgaruvchi nomiga berilmagan bo'lishi.


# Amal qilmaslik kerak bo'lganlar:

# O'zgaruvchi nomi raqam bilan boshlanishi.
# Pythonning maxsus kalit so'zlari (masalan, if, else, while, for kabi) nomlangan o'zgaruvchilarga berilmagan bo'lishi.
# O'zgaruvchilarni nomlashda chiziqchalarni ichiga olish, raqamlarni o'zgaruvchi nomiga berish.
# O'zgaruvchilar nomi juda uzun bo'lishi yoki juda qisqa bo'lishi.
# O'zgaruvchi nomida xususiy belgilash ('@', '$' kabi) ishlatish.

# 3 - mavzu

#Malumot turlari

# Integer (Butun sonlar): Bu turlar butun sonlarni ifodalaydi. Masalan: 5, -10, 1000.

# Float (O'nlik sonlar): Bu turlar o'nlik sonlarni ifodalaydi. Masalan: 3.14, 2.71828, -0.001.

# String (Matnlar): Bu turlar matnlar yoki qatorlar bo'lib, tirnoqcha (') yoki qo'shimcha (") belgilar bilan yuzaga keladi. Masalan: 'Python', "Hello, world!", '123'.

# Boolean (Mantiqiy qiymatlar): Bu turlar True (rost) va False (yolg'on) qiymatlarni ifodalaydi.

# List (Ro'yxatlar): Bu turlar ro'yxatlarni ifodalaydi va qavs ochilgan ko'p elementlar ro'yxatini qamrab olish imkonini beradi. Masalan: [1, 2, 3], ['apple', 'banana', 'orange'].


# Tuple (O'zgarmas Ro'yxatlar): Bu turlar ro'yxatlar kabi bo'lib, lekin bir marta yaratilganda o'zgarmasdir va qavs ochilmaydi. Masalan: (1, 2, 3), ('red', 'green', 'blue').

# Dictionary (Luq'atlar): Bu turlar kalit so'zlar va unga mos keladigan qiymatlar juftligini ifodalaydi. Masalan: {'name': 'John', 'age': 30, 'city': 'New York'}.



# Misol:

# Integer (Butun sonlar)
age = 25

# Float (O'nlik sonlar)
temperature = 26.5

# String (Matnlar)
name = "John Doe"

# Boolean (Mantiqiy qiymatlar)
is_student = True

# List (Ro'yxatlar)
fruits = ["apple", "banana", "orange"]

# Tuple (O'zgarmas Ro'yxatlar)
coordinates = (42.365, -71.102)

# Dictionary (Luq'atlar)
person = {"name": "John", "age": 30, "city": "New York"}




# 4 - mavzu 
# Malumotlarni turini aniqlash
# type() funksiyasi Python tilidagi obyektlarning (masalan, o'zgaruvchilar yoki qiymatlar) turini aniqlaydi. Misol uchun, agar siz type() funksiyasini bir o'zgaruvchiga (masalan, son, matn yoki ro'yxat) yuborsangiz, u o'zgaruvchining turini ko'rsatuvchi klass obyektini qaytaradi.



# Misol:


# Integer (Butun sonlar)
age = 25
print(type(age))  # <class 'int'>

# Float (O'nlik sonlar)
temperature = 26.5
print(type(temperature))  # <class 'float'>

# String (Matnlar)
name = "John Doe"
print(type(name))  # <class 'str'>

# Boolean (Mantiqiy qiymatlar)
is_student = True
print(type(is_student))  # <class 'bool'>

# List (Ro'yxatlar)
fruits = ["apple", "banana", "orange"]
print(type(fruits))  # <class 'list'>

# Tuple (O'zgarmas Ro'yxatlar)
coordinates = (42.365, -71.102)
print(type(coordinates))  # <class 'tuple'>

# Dictionary (Luq'atlar)
person = {"name": "John", "age": 30, "city": "New York"}
print(type(person))  # <class 'dict'>



# 5 - mavzu
#Matematik amallar

# Qo'shish (+): Ikki sonni qo'shish amali operatori bilan bajariladi.
a = 5
b = 3
c = a + b # Natija: 8

# Ayirish (-): Ikki sonni ayirish amali operatori bilan bajariladi.
a = 5
b = 3
c = a - b  # Natija: 2

# Ko'paytirish (*): Ikki sonni ko'paytirish amali operatori bilan bajariladi.
a = 5
b = 3
c = a * b  # Natija: 15

# Bo'lish (/): Ikki sonni bo'lish amali operatori bilan bajariladi.
a = 5
b = 3
c = a / b  # Natija: 1.6666666666666667


# Ko'paytma (//): Ikki sonni qoldiqli bo'lish amali operatori bilan bajariladi.
a = 5
b = 3
c = a // b  # Natija: 1


# Kattasini (**) amali operatori bilan bajariladi.
a = 5
b = 3
c = a ** b  # Natija: 125


# Modul olish (%): Bir sonning boshqa son bilan bo'linishi natijasida qoladi.
a = 7
b = 3
c = a % b  # Natija: 1

# Python tilida ko'p turdagi amal yoki mantiqiy operatorlar mavjud. Bu operatorlar, misol uchun, tenglik (==), katta (>), kichik (<), teng emas (!=), katta teng (>=), kichik teng (<=) va boshqalar. Bu operatorlarni ishlatib, qo'shimcha mantiqiy amallar (if, else, while, for) bilan shartlar yaratish mumkin.

# 6 - mavzu
# if va else operatorlari, shartlarni tekshirish va shartlarga bog'liq ravishda amallar bajarish uchun ishlatiladi.

# if operatori:

# if operatori shartni tekshiradi. Agar shart bajarilishi to'g'ri bo'lsa, shartni izohlab ketuvchi bo'lagi ishga tushadi.
# Agar shart bajarilishi to'g'ri bo'lmagan bo'lsa, if bloki o'tkaziladi va keyingi kodlar bajarilmaydi.

# Misol:

# x = 10
# y = 10
# if x == y:
#     print("hello")
# else:
#     print("salom")
    
x = input('x - Son kiriting: ')
y = input('y - Son kiriting: ')
if x < y:
    print("salom")
    
#elif operatori

# elif operatori if dan kegin keluvchi operator hisoblanib agar if dan otolmasa shartimiz elif operatoriga tushadi 



