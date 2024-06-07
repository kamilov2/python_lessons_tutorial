import sqlite3

# Bazaga ulanish
# Ba'zilar bazaga ulinish bo'yicha ma'lumotlarni olish uchun bazaga ulinish kiritish

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

command = {
    "location":"(id INTEGER PRIMARY KEY, ip_adress TEXT, region TEXT)",
    "users":"(id INTEGER PRIMARY KEY, name TEXT, surname TEXT, password TEXT, email TEXT)",
    "news":"(id INTEGER PRIMARY KEY, title TEXT, image TEXT, text TEXT, like INTEGER)"
}

for i in command:
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {i}{command[i]}''')
    
conn.commit()  # O'zgarishlarni saqlash
conn.close() 
# Jadvallarni yaratish
# Ma'lumotlar bazasidagi jadvalni yaratish
# conn = sqlite3.connect('mydatabase.db')
# cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Ba'zilar bazaga qo'shilgan ma'lumotlar o'zgartirishlaridan oldin saqlanishini talab qilish uchun ba'zi kodlar
conn.commit()  # O'zgarishlarni saqlash
conn.close()   # Uzoqilash

# Ma'lumot qo'shish
# import uuid
# s = str(uuid.uuid4()).split('-')[4]
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute(f"""INSERT INTO users (name, surname, password, email) VALUES ('Alice', 'Jackson', 'helloworld', 'main@gmail.com')""")

# # cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

conn.commit()
conn.close()

# Ma'lumotlarni olish
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Jadvallardan ma'lumotlarni tanlash
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
# print(rows)
# Natijalarni chop etish
for row in rows:
    print(row)

# Ma'lumotlar bazasiga qo'shilgan ma'lumotlarni olish va ulanishni yopish
conn.close()
