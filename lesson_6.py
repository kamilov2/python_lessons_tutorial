text = input('Matni kiriting: ')
if text.startswith('a') and text.count('a') >= 3:
    print(text.replace('a' , 'e'))
elif text.count('a'):
    print(text.count('a'))
else:
    print("Matn ichida A harfi mavjud emas")
    
