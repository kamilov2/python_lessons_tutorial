import sqlite3

command = {}
conn = sqlite3.connect('main.db')
cursor = conn.cursor()

table_name = input("Tablitsa nomini kiriting: ")
count_table = int(input("Nechta ustuncha bolishini kiriting: "))
command[table_name] = {}
a = {}
for i in range(count_table):
    name = input("{0} chi ustuncha uchun nom kiriting: ".format(i+1))
    type_of_name = input("{0} ustunchasi uchun malumot turini tanlang. Misol: TEXT yoki INTEGER: ".format(name))
    a[name] = type_of_name
    
s = ""
for i in a:
    s += f" {str(i)} {str(a[i]).upper()}, "
command[table_name] = f"({s.strip(', ')})"  
print(command)
     
for i in command:
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {i}{command[i]}''')
    
conn.commit() 
conn.close()
