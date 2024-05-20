# import datetime


# def year_convertor(year, month , day):
#     _now = datetime.datetime.now()
#     n = datetime.date(_now.year, _now.month, _now.day,)
#     birthday_date = datetime.date(year,month,day)
#     d = n - birthday_date

#     return f"Siz {_now.year - year} yil, {d.days} kun {d.days * 24} soat { d.days * 1440} minut {d.days * 86400} sekund"

# year = int(input("Tugulgan yilingizni kiriting: "))
# month = int(input("Tugulgan oyingizni kiriting: "))
# day = int(input("Tugulgan sanangizni kiriting: "))



# print(year_convertor(year, month, day))



# num = [20,2,3,4,3,6,5,4,2,8,9,10]
# def hello(list_argument):
#     new_num_list = []    
#     for i in list_argument:
#         if i not in new_num_list:
#             new_num_list.append(i)
#     new_num_list.sort()
#     return new_num_list

# print(hello(num))


def pubg_id_name(player_id):
 
    player_name = {}
    username = ['grinch','krinch','beatch','knyaz','uniqie','kapitan','bot','lord']
    for i in range(8):
        player_name[i] = username[i]

    print(player_name)
    print(player_id)
    return player_name[player_id]


print(pubg_id_name(int(input("Pubg ID sini kiriting va men uni username ni qaytaraman: "))))
     

num1 =  [1,2,3,4,5]
num2 = [5,6,7,8,4]
new_list = [5,4]



