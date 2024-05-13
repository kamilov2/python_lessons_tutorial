# 1 chi - Abdumajidov Islombek
# socol={
#     'diqat 1 savol ingilis tilida nechta zamon bor? ': '16',
#     'diqat 2 savol qaysi davlat qogan davlatlardan kora koproq kofe chiqaradi? ': 'brazilya',
#     'diqat 3 savol kim telefondi oylab topgan? ': 'Aleksandr grem bell',
#     'diqat 4 savol zemmifobiya kasaligiga uchragan odam nimadan qorqadi? ':'krisa',
#     'diqat 5 savol qaysi biri birinchi paydo bogan tovuq-tuxum ? ': 'to'
# }
# ball=0
# for i in socol.keys():
#     javo=input('{0}'.format(i))
#     if javo == socol[i]:
#         ball += 1
#     elif javo == socol[i].upper():
#         ball += 1
#     elif javo == socol[i].upper():
#         ball += 1
#     elif javo == socol[i].upper():
#         ball += 1
#     elif javo == socol[i].upper():
#         ball += 1
# print("sizz yig'gan ballaringiz:",ball)

# (ChatGPT)
# A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,
# 37,38,39,40,41,42,43,44,45,46,47,48,49,50,50,50,2,12,3,14,14,14,50]
# dublikatlar = {}
# for elem in A:
#     dublikatlar[elem] = dublikatlar.get(elem, 0) + 1

# norma = {element: count for element, count in dublikatlar.items() if count > 1}

# print(norma)
# print(dublikatlar)

#_____________________________________________________________________________________________
# 1- chi Bahodirov Muhammadamin
# print("Assalomu alekum! Bu ZYREX tomonidan yaratilgan dastur")
# print()
# user=input("Ismingizni kiriting: ").capitalize()
# savollar = { "savol_1":"O'zbek tilining asoschisi kim?", "javob_1": "Navoiy",
#       "savol_2":"2x2= nechchiga teng?", "javob_2": "4",
#       "savol_3":"Nyutonning boshiga qaysi meva tushib ketgan?", "javob_3": "Olma",
#       "savol_4":"100 yil qisqa qilib nima deb ataladi?", "javob_4": "Asr",
#       "savol_5":"Pavel Durov qaysi messengerni yaratgan", "javob_5": "Telegram"
# }
# sum=0
# for i in range(1,6):
#     a=input(savollar[f'savol_{i}']).capitalize()
#     if a == savollar[f'javob_{i}']:
#         sum+=1
#         print("To'g'ri topdingiz :)")
#     else:
#         print("Noto'g'ri topdingiz :)")
# print()
# for i in range(1,6):
#     print("Javoblar:", savollar[f'javob_{i}'])
# print(f"Siz {sum} ball to'pladingiz,",
#       f"Ishtirokingiz uchun rahmat {user}!")

#_________________________________________________________________________________________________

# 2-chi Abdumajidov Islombek (ChatGPT)
# from datetime import datetime, timedelta
# import time

# s = {
#     "18:54:12": "2024-04-18",
#     "18:54:13": "2024-04-19"
# }

# for time_str, date_str in s.items():
#     dt = datetime.strptime(date_str + ' ' + time_str,'%Y-%m-%d %H:%M:%S')
#     while True:
#         dt += timedelta(seconds=1)
#         dt += timedelta(days=1)
        
#         print(dt.strftime('%H:%M:%S %Y-%m-%d'))
        
#         time.sleep(1)

# _______________________________________________________________________________________________________


# 1-chi Yoldashmirzayev Shoyatbek (ChatGPT)
# def pro(soz):
#     return soz[::-1]
# soz = input("so'z kiriting: ")
# print("Teskari holati:", pro(soz))



#3-chi Bahodirov Muhammadamin
# num1=[45,1,2,3,4,5,10]
# num2=[5,6,7,8,4,10,45]
# new_list=[]
# def hi(num12):
#     for i in num1:
#         if i in num2:
#             num12.append(i)
#     return num12
# print(hi(new_list))