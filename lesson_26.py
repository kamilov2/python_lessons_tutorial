


# def choose_your(p):
#     file_path = "log.txt"
#     if p == 'w':
#         file = open(file_path, "w")
#         content = input("Faylga yozish uchun malumot kiriting va fayl ichidagi malumotlar butunlayin yangilanadi: ") 
#         file.write(content)
#         file.close()
#         file = open(file_path , "r")
#         print("Fayl ichidagi malumotlar shunga ozgardi\n",file.read())
#         file.close()
#     elif p == 'a':
#         file = open(file_path, "a")
#         content = input("malumot kiriting va men uni keyingi qatordan yozib ketaman: ")
#         file.write(content)
#         file.close()
#     elif p == 'r':
#         file = open(file_path, "r")
#         print("Fayl ichidagi malumotlar\n",file.read())
#         file.close()
#     else:
#         print("maksadni togri kiriting: ")
# choose_your("r")


def zyrex(uzb):
    if uzb == "w":
        file = open("example.txt", "w")
        file.write(input(f"Siz faylga ma'umot yozishni tanladingiz \nFaylga istalgan yoziladigan narsa yozing: "))
        file.close()
        return f"Faylga malumotlar yozildi!"
    elif uzb == "a":
        file = open("example.txt", "a")
        file.write(input(f"Siz faylga ma'umot qo'shishni tanladingiz \nFaylga istalgan yoziladigan narsa yozing: "))
        file.close()
        return f"Faylga malumotlar qo'shildi!"
    elif uzb == "r":
        file = open("example.txt", "r")
        file_content = file.read() 
        file.close()
        return f"Fayldagi narsalar: \n{file_content}"
    else:
        return "Siz kiritgan harf ma'lumotlar orasida yo'q !!!"
    
print(zyrex(str(input('''
Harflardan birini tanlang:

w - Faylga ma'lumot yozish
a - Faylga ma'lumot qo'shish
r - Fayldagi ma'lumotni o'qish
''').lower())))