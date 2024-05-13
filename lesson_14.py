# client = {
#     'client_1':{ 'ism': 'Ali','yosh':19, },
#     'client_2':{ 'ism': 'Gani','yosh':17, },
#     'client_3':{ 'ism': 'Qani','yosh':10,  },
#     'client_4':{ 'ism': 'Abdurahmon','yosh':16,  },
#     'client_5':{ 'ism': 'Ismoiljon','yosh':16,  },    
# }
# for i in client:
#     if client.get(i).get('yosh') > 18:
#         s = {
#             "status":"Voyaga yetgansiz"
#         }
#         client.get(i).update(s)
#     else:
#         s = {
#             "status":"Voyaga yetmagansiz"
#         }
#         client.get(i).update(s)
#     s = input('{0} uchun kasb qoshing: '.format(client.get(i).get('ism')))
#     if s.isalpha():
#         d = {
#             "kasb":f"{s}"
#         }
#         client.get(i).update(d)
#     else:
#         print("Kasb faqat harflardan iborat bolishi kerak")
        
# for i in range(1,6):
#     print(client.get(f'client_{i}'))              
    
    
budjet = 50
check = {}
product =  {
        "Banana":2,
        "Ananas":5,
        "Mango":4,
        "Gosht":10,
        "Baliq":8,
        "Chips":3,
        "Fanta":4,
        "Cola":4   
}
p = product.keys()
for i in p:
    print(i)

while True:
    a = input("Mahsulot tanlang : ")
    if a == 'stop':
        print("Siz sotib olgan narsalar: ", check)
        break
    
    
    check.update({f"{a}":{
        "narxi":f"{product.get(a)}",
        "soni": 1
        }})
    
    
    
    print("Savatchadagi mahsulotlar: ", check)
    budjet - int(product.get(a))
    print(f'Sizning balansingizda {budjet} $ shuncha qoldi')
    if budjet == 0 or budjet < 0:        
        print("Balansingizda pul qolmadi ")
        break
