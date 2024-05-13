# fayl ochib ichida agar malumot mavjud bolsa ochirib tashlab boshqatdan malumot yozishga
file_path = 'example.txt'
content = '1 - chi qator.\n 2 - chi qator.\n3 - chi qator.'
file = open(file_path, 'w')
file.write(content)
file.close()

# Fayl qiymatini ichidagi malumotini oqish
# file = open(file_path, 'r')
# file_content = file.read()
# print("Fayl qiymati:")
# print(file_content)
# file.close()

# faylni qatorlar boyicha oqish
# file = open(file_path, 'r')
# lines = file.readlines()
# print("fayl qatorlari")
# for line in lines:
#     print(line.strip())  
# file.close()

# Yozilgan ichida qiymat bor faylga qiymat qoshib ketish
# additional_content = '\nQoshimcha fubksiya'
# file = open(file_path, 'a')
# file.write(additional_content)
# file.close()

# Fayl ichidagi qiymatni oqish
# file = open(file_path, 'r')
# file_content = file.read()
# print("Fayl oqish")
# print(file_content)
# file.close()

# Fayl nusxa olib boshqa fayl ochib kochirib otish
# import shutil
# shutil.copy(file_path, 'example_copy.txt')
# print("Fayldan nusxa olindi")

# Faylni boshqa joyga kochirish
# shutil.move('example_copy.txt', 'example_directory/example_copy.txt')
# print("Fayl kochirildi")

# Faylar ni ochirish
# import os
# os.remove(file_path)
# os.remove('example_directory/example_copy.txt')
# print("Fayl ochirildi!")