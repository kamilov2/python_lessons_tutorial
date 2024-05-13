import datetime
import time
import random


year = int(input("Tugulgan yilingizni kiriting: "))
month = int(input("Tugulgan oyingizni kiriting: "))
day = int(input("Tugulgan sanangizni kiriting: "))


_now = datetime.datetime.now()
n = datetime.date(_now.year, _now.month, _now.day,)
birthday_date = datetime.date(year,month,day)
d = n - birthday_date

print(f"Siz {_now.year - year} yil, {d.days} kun {d.days * 24} soat { d.days * 1440} minut {d.days * 86400} sekund")

# secund = 0
# d = 4

# num = random.randint(1,10)
# for i in range(1,1000):
#     code = int(input("Bombani tohtatish uchun kodini kiriting sizda 1 minut vaqt bor: "))
#     if code != num:
#         d -= 1
#     elif d == 0 or secund >= 60:
#         print("Bomba portladi")
#         break
#     else:
#         print("Siz yutdingiz")



# while True:
#     secund += 1
#     time.sleep(1)
#     print(secund)
#     if secund == 60:
#         break


s = {
    "18:54:12":"2024-04-18",
    "18:54:13":"2024-04-19"

}


# while True:
#     _now = datetime.datetime.now()
#     print(_now.strftime("%H:%M:%S"))
#     time.sleep(1)




