import sqlite3

# Bazaga ulanish
# Ba'zilar bazaga ulinish bo'yicha ma'lumotlarni olish uchun bazaga ulinish kiritish
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Jadvallarni yaratish
# Ma'lumotlar bazasidagi jadvalni yaratish
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Ba'zilar bazaga qo'shilgan ma'lumotlar o'zgartirishlaridan oldin saqlanishini talab qilish uchun ba'zi kodlar
conn.commit()  # O'zgarishlarni saqlash
conn.close()   # Uzoqilash

# Ma'lumot qo'shish
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Ma'lumotlar bazasiga ma'lumot qo'shish
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# Ma'lumotlarni saqlash va ulanishni yopish
conn.commit()
conn.close()

# Ma'lumotlarni olish
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Jadvallardan ma'lumotlarni tanlash
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Natijalarni chop etish
for row in rows:
    print(row)

# Ma'lumotlar bazasiga qo'shilgan ma'lumotlarni olish va ulanishni yopish
conn.close()
