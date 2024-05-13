# import json

# s = open('main.json') 
# print(json.load(s))
# s.close()

# content = {
#     "surname":"Odashev"
# }
# print(content["surname"])
# s = open('main.json', 'a') 

# json.dump(content, s)
# s.close()

















# s = [1,2,3,4,5,6,7,8,9,10,11,12]

# def numbers_2(arr):
#     file_path = "main.txt"
#     file = open(file_path, 'a')
#     for i in arr:
#       if i % 2 == 0:
#          print(i)
#          file.write(f"{str(i)},")
#     file.close()

# numbers_2(s)



# with open("main.txt", "r+") as file:
#     lines = file.readlines()  
#     lines[50:] = "main\n"
#     file.seek(0)  
#     file.writelines(lines)


import datetime
import os


file = open("main.py", 'w')
content = '''
import os

arr = ["hello.py"]

for i in arr:
    os.remove(i)

'''

# os.system("C:/Users/Gnom/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/Gnom/Desktop/python/main.py")
# file.write(content)
# file.close()


import uuid 
s = ""
for i in range(1000):
    s += str(uuid.uuid4())

print(s)
