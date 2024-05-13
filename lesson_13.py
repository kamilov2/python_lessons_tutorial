# # my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]

# # # new_list = []
# # # for i in my_list:
# # #     if i % 2 == 0:       
# # #         new_list.append('A')
# # #     new_list.append(i)
# # # print(new_list)


# my_dict = {'ism': 'Ali', 'yosh': 25, 'kasb': 'muhandis'}

# # # 1. get() - berilgan kalitni qidirib topish
# print(my_dict.get('ism'))  # Natija: Ali
# print(my_dict['ism'])

# # # 2. keys() - lug'atdagi barcha kalitlarni olish
# print(my_dict.keys())  # Natija: dict_keys(['ism', 'yosh', 'kasb'])

# # # 3. values() - lug'atdagi barcha qiymatlarni olish
# print(my_dict.values())  # Natija: dict_values(['Ali', 25, 'muhandis'])

# # # 4. items() - lug'atdagi barcha juftliklarni olish
# print(my_dict.items())  # Natija: dict_items([('ism', 'Ali'), ('yosh', 25), ('kasb', 'muhandis')])

# # # 5. pop() - berilgan kalitni lug'atdan o'chirish
# my_dict.pop('yosh')
# print(my_dict)  # Natija: {'ism': 'Ali', 'kasb': 'muhandis'}

# # # 6. update() - biror lug'atni boshqa lug'atga qo'shish
# additional_info = {'tuman': 'Yunusobod', 'viloyat': 'Toshkent'}
# my_dict.update(additional_info)
# print(my_dict)  # Natija: {'ism': 'Ali', 'kasb': 'muhandis', 'tuman': 'Yunusobod', 'viloyat': 'Toshkent'}



f = {
    "karta":"Livik",
    "name":1,
    "name2":2,
    "name3":3
    }
a = {
    "Event":1,
    "surname":1,
    "surname1":2,
    "surname2":3
}
f.update(a)
print(f)
b = {
    "Event":2,
    "surname":3,
    "surname1":4,
    "surname2":5
}
for i in b:
    f[i] = b[i]
print(f)

# # 7. clear() - lug'atdagi barcha elementlarni o'chirish
# my_dict.clear()
# print(my_dict)  # Natija: {}


# number = {
#     1:'bir',2:'ikki',3:'uch',4:'tort',5:'besh',6:'olti',7:'yetti',8:'sakiz',9:'tokiz',10:'on'
# }
# #get ishlatish
# # print(number.get(int(input('Son ni kiriting: '))))

# #keys ishlatish
# #1 variant standart metodlari bilan
# key_value = number.keys()
# for i in key_value:
#     print(number.get(i), 'metodlar bilan')   
    
    
# #2 metodsiz 
# for i in number:
#     print(number[i], 'metodsiz')
    
    
# #values
# print(number.values())    


# client = {
#     'client_1':{ 'ism': 'Ali','yosh':19, 'kasb': 'programist' },
#     'client_2':{ 'ism': 'Gani','yosh':17, 'kasb': 'biznesmen'},
#     'client_3':{ 'ism': 'Qani','yosh':10, 'kasb': 'apple_asoschisi' },
#     'client_4':{ 'ism': 'Abdurahmon','yosh':16, 'kasb': 'Microsoft_asoschisi' },
#     'client_5':{ 'ism': 'Ismoiljon','yosh':16, 'kasb': 'SpaceX_asoschisi' },    
#     }

# key_client = client.keys()
# for i in key_client:
#     if client.get(i).get('yosh') < 18:
#         x = client.get(i)
#         x['kasb'] = 'Yolginchi'
        
          
# for i in range(1,6):      
#     print(client[f'client_{i}']['kasb'])
    
        