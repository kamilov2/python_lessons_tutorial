# x = ['apple', 85, -56, 'banana', 11, -53, 1, 'hello', 5]
# a = []
# b = []
# c = []

# for i in x:
#     if type(i) == str:
#         c.append(i)
#     elif i > 0:
#         a.append(i)
#     else:
#         b.append(i)
        
# s = [a,b,c]
# for f in s:
#     print(f)
#     f.sort()


# basket = []
# fruits = ['apple', 'banana', 'mango', 'ananas']
# code = ['5694', '8541', '4798', '9415']

# for i in code:
#     print(fruits[code.index(i)], 'mahsulot kodi - ', i)
# while True:        
#     c = input('Sotib olmoqchi bolgan mahsulotingiz kodini kiriting: ')
#     if c == 'stop':
#         break   
#     basket.append(fruits[code.index(c)])
# print(basket)
  
  
    
    
# while True:
#     c = input('Kod ni kiriting: ')    

#     if c == 'stop':
#         break
#     basket.append(fruits[int(c)])

# print(basket)
    
        
   
# while True:
#     c = input('Kod ni kiriting: ')
#     if c == '5432':
#         basket.append('apple')
#     elif c == '6895':
#         basket.append('banana')
        
        
s = [12, -89]
a = []
b = []



# Juf sonlarni x list qiymatiga otkazamiz va y list dan ochirib tashlaymiz ohirida y qiymatida qolgan sonlar bilan x qiymatiga otgan sonlarni print qilamiz
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
x = []

for num in y:
    if num % 2 == 0:
        x.append(num)
        y.remove(num)
    