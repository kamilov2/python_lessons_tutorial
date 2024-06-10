# import sqlite3

# command = {}
# conn = sqlite3.connect('main.db')
# cursor = conn.cursor()

# table_name = input("Tablitsa nomini kiriting: ")
# count_table = int(input("Nechta ustuncha bolishini kiriting: "))
# command[table_name] = {}
# a = {}
# for i in range(count_table):
#     name = input("{0} chi ustuncha uchun nom kiriting: ".format(i+1))
#     type_of_name = input("{0} ustunchasi uchun malumot turini tanlang. Misol: TEXT yoki INTEGER: ".format(name))
#     a[name] = type_of_name
    
# s = ""
# for i in a:
#     s += f" {str(i)} {str(a[i]).upper()}, "
# command[table_name] = f"({s.strip(', ')})"  
# print(command)
     
# for i in command:
#     cursor.execute(f'''CREATE TABLE IF NOT EXISTS {i}{command[i]}''')
    
# conn.commit() 
# conn.close()



import sqlite3

command = {}
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

table_name = input("Enter table name for add data: ").lower()
enter_data_tables = input(f"{table_name} Enter tables name in db example( name,surname,age ): ").split(',')
count_table = int(input("enter count for "))
print(enter_data_tables)

command[table_name] = {}
a = {}
for i in range(count_table):
    name = input("enter {0} for  {1} user : ".format(enter_data_tables[0], i+1))
    surname = input("enter {0} for {1}".format(enter_data_tables[1], name))
    age = int(input("enter {0} for {1} {2}".format(enter_data_tables[2], name, surname)))
    
    a[i+1] = {"name":name, "surname":surname, "age":age}
    
print(a)
s = ""
for i in a:
    s += f"{str(a[i])}, "
command[table_name] = a 

d = 1
for i in command:
    print(command[i][d])
    d += 1
    
    
     
# for i in command:
#     cursor.execute(f'''INSERT INTO TABLE ''')
    
# conn.commit() 
# conn.close()


