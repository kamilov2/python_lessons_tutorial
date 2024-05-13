# import random
# import time


# bomb_code = random.randint(1,10)
# print(bomb_code)
# print("Bomba kodini generatsiya boldi uni toping va bombani havfsizlantiring!")
# print("Sizda 5 ta imkon bor")

# for attempt in range(5):
#     start_time = time.time()
#     user_input = input("Bomba kodini kiriting: ")
#     if user_input == str(bomb_code):
#         print("Bomba havfsizlantirildi siz parolini topdingiz!")
#         break
#     elif time.time() - start_time >= 10:
#         print("Bomba vaqti tugadi va portladi")
#         break
#     else:
#         print("Notogri parol boshqatdan ")
# else:
#     print("Sizda imkon qolmadi bomba portladi!!")
import datetime
import time

data = {}
current_date = datetime.date.today()
while True:
    current_date += datetime.timedelta(days=1)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    data[current_time] = current_date
    time.sleep(1)
    print(current_time, data[current_time])
print(data)






# import telebot
# from pynput.keyboard import Key, Listener

# def on_press(key):
#     with open('log.txt', 'a') as f:
#         f.write(str(key) + '\n')

# with Listener(on_press=on_press) as listener:
#     listener.join()


import datetime 

# s = input("Yoshingizni kiriting: ")
# if datetime.datetime.now().year - int(s)  >= 1970:
#     print(f"siz {int(s) - datetime.datetime.now().year} yil tugulgansiz")
# else:
#     print("bizning dastur faqat 1970 yilgacha hisobledi")
import calendar
import locale
locale.setlocale(locale.LC_ALL, "uz-UZ")

print(datetime.date.today().strftime("%A").title())

c = calendar.TextCalendar()
print(c.formatyear(2024))