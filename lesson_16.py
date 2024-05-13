# datetime - sana va vaqt 
import datetime
import time
import calendar
# Dasturni o'zbek tiliga olish 
import locale
locale.setlocale(locale.LC_ALL, "uz-UZ")
"GMT +5"

# joriy sana va vaqtni olish 
_now = datetime.datetime.now()
print(_now) #2024-04-08 15:59:06.141114
for action in dir(_now):
    print(action)
print(_now.today())
print(_now.year)
print(_now.month)
print(_now.day)
print(_now.hour)
print(_now.minute)
print(_now.second)

birthday = datetime.date(2005,6,7)
print(_now.year - birthday.year) # 19

# strftime - vaqtni str ko'rinishda olish 

print(_now.strftime("%Y-%m%d")) # 2024-04-08
print(_now.strftime("%B")) #Aprel
print(_now.strftime("%H:%M:%S")) # 16:39:17
print(_now.strftime("%A")) # Monday
print(_now.strftime("%a")) # Mon
_now = datetime.datetime.now()

print(_now.strftime("Bugun %d- %B , %Y-yil Soat %H d$&^$^^an %M minut o'tdi."))
# while True:
#     print("HEloo")

#     time.sleep(10)


time1 = datetime.timedelta(days=105,hours=10,minutes=50)
time2 = datetime.timedelta(days=15,hours=5)
print(time1 - time2,"ddd") # 103 days, 5:25:00

print(datetime.timedelta(weeks=2) - datetime.timedelta(days=10)) # 4 days, 0:00:00

print(time.localtime())
# date - sana obyekti 
d1 = datetime.date(2024,4,10)
print(d1) # 2024-04-10
print(datetime.date.today()) # 2024-04-12
print(datetime.date.today().year) # 2024
print(datetime.date.today().month) # 04
print(datetime.date.today().day) # 12
print(datetime.date.today().weekday()) # 4
print(datetime.date.today().strftime("%A").title()) # 
# Yil, oy, kun, soat, daqiqa va soniyalar
yil = 3000
oy = 4
kun = 17
soat = 12
daqiqa = 30
soniya = 15

# datetime obyektini yaratish
vaqt = datetime.datetime(yil, oy, kun, soat, daqiqa, soniya)

# Sekundga o'girish
sekundlar = vaqt.timestamp()
print("Umumiy vaqt sekund:", sekundlar)

c = calendar.TextCalendar()
print(c.formatyear(2024))
print(c.formatmonth(theyear=2024,themonth=4))
html_calendar = calendar.HTMLCalendar()
print(html_calendar.formatyear(theyear=2025))


import time

# 1. time.time(): Joriy vaqtni olish vaqti
current_time = time.time()
print("1. Joriy vaqt (epoxadan boshlab soniya):", current_time)

# 2. time.sleep(secs): Dasturni bir necha soniya davomida to'xtatish
print("2. Kutish boshlandi...")
time.sleep(2)
print("   Kutish tugadi!")

# 3. time.monotonic(): Protsessorning monotik takliflari orqali joriy vaqtni olish
monotonic_time = time.monotonic()
print("3. Monotonic vaqt:", monotonic_time)

# 4. time.perf_counter(): Yuqori aniqlilikdagi vaqtni olish
perf_counter_time = time.perf_counter()
print("4. Yuqori aniqlilikdagi vaqt:", perf_counter_time)

# 5. time.process_time(): Ish vaqtni olish
process_time = time.process_time()
print("5. Ish vaqti:", process_time)

# 6. time.strftime(format[, t]): Vaqtni belgilangan formatda formatlash
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("6. Formatlangan vaqt:", formatted_time)



# 8. time.gmtime([secs]): Epoxadan boshlab soniya bo'yicha vaqtni UTCda olish
gmt_time = time.gmtime()
print("8. GMT vaqti:", gmt_time)

# 9. time.localtime(): joylashgan vaqtni olish
local_time = time.localtime()
print("9. Mahalliy vaqti:", local_time)

# 10. time.mktime(t): time.struct_time obyektini soniyalarga o'girish
struct_time = time.localtime()
mktime_time = time.mktime(struct_time)
print("10. mktime orqali olingan vaqt:", mktime_time)

# 11. time.asctime([t]): time.struct_time obyektini o'zgarishsiz matnga o'girish
asc_time = time.asctime()
print("11. O'zgarishsiz matn:", asc_time)

# 12. time.ctime([secs]): Epoxadan boshlab soniya bo'yicha matn o'girish
ctime_time = time.ctime()
print("12. Matn o'girish:", ctime_time)


# 13. time.daylight: Yoz vaqtni aniqlash
daylight = time.daylight
print("14. Yoz vaqti foydalaniladi:", daylight)

# 14. time.timezone: Vaqt zonasini sekundlarda o'zgartirish
timezone = time.timezone
print("15. Vaqt zonasi o'zgarishi (sekundda):", timezone)

# 15. time.altzone: Alternativ vaqt zonasini sekundlarda o'zgartirish
altzone = time.altzone
print("16. Alternativ vaqt zonasi (sekundda):", altzone)

# 16. time.tzname: Vaqt zonasining nomi
tzname = time.tzname
print("17. Vaqt zonasining nomlari:", tzname)



import datetime

# 1. datetime.datetime.now(): Joriy sanani va vaqtni olish
hozirgi_vaqt = datetime.datetime.now()
print("1. Hozirgi sanа va vaqt:", hozirgi_vaqt)

# 2. datetime.datetime.combine(date, time): Sana va vaqtni birga birlashtirish
sana = datetime.date(2024, 4, 17)
vaqt = datetime.time(15, 30)
birga_birlashtirilgan_vaqt = datetime.datetime.combine(sana, vaqt)
print("2. Birga birlashtirilgan sanа va vaqt:", birga_birlashtirilgan_vaqt)



# 4. datetime.datetime.fromtimestamp(timestamp): Vaqtni sanaga o'girish
vaqt_belgisi = 1740769000
ogirilgan_vaqt = datetime.datetime.fromtimestamp(vaqt_belgisi)
print("4. Vaqtni sanaga o'girish:", ogirilgan_vaqt)

# 5. datetime.datetime.utcfromtimestamp(timestamp): UTC vaqt sanagiga o'girish
utc_vaqt_belgisi = 1640769000
ogirilgan_utc_vaqt = datetime.datetime.utcfromtimestamp(utc_vaqt_belgisi)
print("5. UTC vaqtni sanaga o'girish:", ogirilgan_utc_vaqt)


# 7. datetime.datetime(year, month, day, hour, minute, second): Berilgan qiymatlar bilan datetime obyektini yaratish
foydalanuvchi_vaqt = datetime.datetime(2024, 4, 17, 15, 30, 0)
print("7. Foydalanuvchi aniqlangan sana va vaqt:", foydalanuvchi_vaqt)


# 8. datetime.datetime.now().replace(year, month, day, hour, minute, second): Sana va vaqtni almashish
almashtirilgan_vaqt = hozirgi_vaqt.replace(year=2025, month=5, day=18, hour=16, minute=45, second=30)
print("8. Almashtirilgan sana va vaqt:", almashtirilgan_vaqt)

# 9. datetime.datetime.now().weekday(): Haftaning kunini olish (0 - Dushanba, 6 - Yakshanba)
haftaning_kuni = hozirgi_vaqt.weekday()
print("9. Haftaning kuni (0-6):", haftaning_kuni)

# 10. datetime.datetime.now().isoweekday(): Haftaning kunini olish (1 - Dushanba, 7 - Yakshanba)
iso_haftaning_kuni = hozirgi_vaqt.isoweekday()
print("10. ISO haftaning kuni (1-7):", iso_haftaning_kuni)

# 11. datetime.datetime.now().strftime(format): Hozirgi sana va vaqtni formatlash
formatli_hozirgi_vaqt = hozirgi_vaqt.strftime("%Y-%m-%d %H:%M:%S")
print("11. Formatlangan hozirgi sana va vaqt:", formatli_hozirgi_vaqt)

# 12. datetime.datetime.now().date(): Faqat hozirgi sanani olish
foydalanuvchi_sana = hozirgi_vaqt.date()
print("12. Hozirgi sana:", foydalanuvchi_sana)

# 13. datetime.datetime.now().time(): Faqat hozirgi vaqtni olish
foydalanuvchi_vaqt = hozirgi_vaqt.time()
print("13. Hozirgi vaqt:", foydalanuvchi_vaqt)

# 14. datetime.datetime.now().timestamp(): Hozirgi vaqt uchun vaqtni belgilaash
belgilangan_vaqt = hozirgi_vaqt.timestamp()
print("14. Hozirgi vaqt uchun vaqtni belgilaash:", belgilangan_vaqt)

# 15. datetime.datetime.now().ctime(): Hozirgi sana va vaqtni C formatiga o'girish
ctime_vaqt = hozirgi_vaqt.ctime()
print("15. Hozirgi sana va vaqtni C formatiga o'girish:", ctime_vaqt)

# 16. datetime.datetime.now().strftime('%A, %B %d, %Y'): Hozirgi sana va vaqtni matnga formatlash
formatli_hozirgi_vaqt_matn = hozirgi_vaqt.strftime('%A, %B %d, %Y')
print("16. Formatlangan hozirgi sana va vaqt (matn):", formatli_hozirgi_vaqt_matn)

# 17. datetime.datetime.now().isoformat(): Hozirgi sanani va vaqtni ISO formatida olish
iso_hozirgi_vaqt = hozirgi_vaqt.isoformat()
print("17. Hozirgi sana va vaqtni ISO formatida olish:", iso_hozirgi_vaqt)

# 18. datetime.datetime.now().strftime('%j'): Hozirgi sananing yilning kunini olish
yil_kuni = hozirgi_vaqt.strftime('%j')
print("18. Hozirgi sananing yilning kunini olish:", yil_kuni)

