# c = ['tosh','qaychi', 'qogoz']
# client_choice = input('Chingal chuks: ').lower()
# computer_choice = random.choice(c)
# print(computer_choice)

# if client_choice == computer_choice:
#     print('Boshqatdan')
# elif (client_choice == 'tosh') and \
#     (computer_choice == 'qaychi') or (client_choice == 'qaychi') and \
#         (computer_choice == 'qogoz') or (client_choice == 'qogoz') and \
#             (computer_choice == 'tosh'):
#                 print('Siz yutdiz!')
# else:
#     print('Siz yutkazdingiz ! ')


# d = random.randint(1, 10)
# print(d)
# c = 0 
# while c != d:
#     c = int(input('Son ni kiriting: '))
#     if c > d:
#         print('Oylangan son kichikrok')
#     elif c < d:
#         print('Oylangan son katarok')

# print("Siz yutdingiz!")
    
import random
    
my_list = ['apple', 'banana', 'cherry']
random.shuffle(my_list)
print(my_list) 
  