# import datetime
# import locale
# locale.setlocale(locale.LC_ALL, "uz-UZ")
# def birthday_convertor(year,month,day):
#     _now = datetime.datetime.now()
#     n = datetime.date(_now.year, _now.month, _now.day)
#     birthday_date = datetime.date(_now.year,month,day)
#     d = birthday_date - n
#     return f"Siz {d.days}, kundan keyin {_now.year - year}, yoshga kirasiz"

# print(birthday_convertor(int(input('Tugulgan yilingizni kiriting: ')),int(input('Tugulgan oyingizni kiriting: ')), int(input("Tugulgan kuningizni kiriting: "))))

import random

def random_list():
    arr = []
    while len(arr) < 50000:
        s = random.randint(1000, 100000)
        print(s)
        if s not in arr:
            arr.append(s)
    return arr
print(random_list())