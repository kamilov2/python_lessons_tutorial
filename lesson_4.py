#for loop
# 1. Berilgan oraliqdagi toplamini hisoblash
total = 0
for i in range(1, 11):
    total += i
print("1 dan 10 gacha sonlar yig'indisi:", total)

# 2. Berilgan ro'yxatdagi elementlarni qaysi biri butun son ekanligini tekshirish
# my_list = [1, 2, 3, 'apple', 5, 'banana']
# for item in my_list:
#     if isinstance(item, int):
#         print(item, "butun son")
#     else:
#         print(item, "butun son emas")

# 3. Berilgan ro'yxatdagi juft sonlarni ekranga chiqarish
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if num % 2 == 0:
#         print(num, "juft son")
#     else:
#         print(num, "toq son")


#while loop
# 1. 1 dan 10 gacha bo'lgan butun sonlarni ekranga chiqarish
# num = 1
# while num <= 10:
#     print(num)
#     num += 1

# 2. Berilgan sonni 0 gacha bo'lgan darajalarini ekranga chiqarish
# base = int(input("Butun son kiriting: "))
# power = 0
# result = 1
# while power <= 10:
#     print(base, "ning", power, "darajasi:", result)
#     result *= base
#     power += 1


# print("""Siz qaysi operatsion tizimdan foydalanasiz?
# 1 — Windows 11
# 2 — Windows 10
# 3 — Windows 8.1
# 4 — Windows 8
# 5 — Windows 7
# 6 — Windows Vista
# 7 — Windows XP
# 8 — Mac OS
# 9 — Linux
# 10 — Ubuntu
# 11 — Chrome OS
# 12 — iOS
# 13 — Android
# """)
# variants = {
#     "1": "Windows 11",
#     "2": "Windows 10",
#     "3": "Windows 8.1",
#     "4": "Windows 8",
#     "5": "Windows 7",
#     "6": "Windows Vista",
#     "7": "Windows XP",
#     "8": "Mac OS",
#     "9": "Linux",
#     "10": "Ubuntu",
#     "11": "Chrome OS",
#     "12": "iOS",
#     "13": "Android",
# }
# operatsion_tizim = input("Javobingizni kiriting (raqamni kiriting): ")

# if operatsion_tizim in variants:
#     print(f"Siz {variants[operatsion_tizim]} tizimidan foydalanishingizni tanladingiz.")
# elif not operatsion_tizim:
#     print("Siz raqam kiritmadingiz.")
# else:
#     print("Biz sizning kiritgan tizimni aniqla olmadik.")


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i, count = 0, len(arr)
# while i < count: 
#     arr[i] *= 2
#     i += 1
# print(arr) 