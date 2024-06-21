from telebot import TeleBot, types #kutubxonalarni import qilish 'TeleBot' - doimiy connect ulanishligini ulab turish uchun kerak boladi, types chiqayotgan button lar uchun kerak KeyboardButton bilan InlineButton lar uchun


bot = TeleBot('7293075143:AAHcGWvUmnmK4lo4qxtXcmX6KmfvOTTlWtg') # - doimiy ulanishlikni hosil qilish

@bot.message_handler(commands=['start'])# decorator doimiy kuzatuvchi metod doimiy korsatilgan commandani kuzatadi
def register(message):# register funksiyasi qaconki decorator orqali buyruq kelsa shundagina ishledi 
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)# KeyboardButton larni razmerga solish qurilmaga qarab
    
    contact_button = types.KeyboardButton("Send Contact", request_contact=True)# Button hosil qilish telegram yozish joyidan pastgi qismida
    
    location_button = types.KeyboardButton("Send Location", request_location=True)# Button hosil qilish telegram yozish joyidan pastgi qismida
    
    markup.add(contact_button, location_button)# razmerlagan holatga yaratgan button larni berib yuborish
    
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)# funksiyani tugashi doim bir response bilan tugashi shart malum buyruk kelgandan kegin majbur javob qaytarish kerak

@bot.message_handler(content_types=['contact', 'location'])# decorator malum bir buyruklarni kuzatish 'content_types' doimiy - 'location','contact','media','rasm' va 'matn' shaklidagi buyruklarni korsatish uchun kerak boladi va odimiy 'list' malumot turini qabul qiladi  
def handle_special_content(message):# funksiya doimiy decoratordan malum uyruk kelganda ishledi va message ni qabul qiladi message oz ichiga hamma chatdegi yozuvlarni oziga oladi
    if message.contact:# malumot tekshirish message.contact message ozida contact degan malumot ni qabul qilib tekshirish True yoqi False qiymatini qaytaradi
        
        bot.send_message(message.chat.id, f"Received contact: {message.contact.phone_number}")
    elif message.location:# malumot tekshirish message.location message ozida location degan malumot ni qabul qilib tekshirish True yoqi False qiymatini qaytaradi
        
        bot.send_message(message.chat.id, f"Received location: {message.location.latitude}, {message.location.longitude}") # funksiya tugashi malum bir javob bilan 'message.location.latitude' - kordinat olish hisoblanib yer shari boyiga qarab beriladi, 'message.location.longitude' - kordinat olish hisoblanib yer shari eniga qarab beriladi \
            


@bot.message_handler(commands=['hello'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton("Button 1")
    button2 = types.KeyboardButton("Button 2")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Button 1":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("salom", url="https://kun.uz"), types.InlineKeyboardButton("salom", url="https://kun.uz"))
        bot.send_message(6781413070, "You pressed Button 1!")
    elif message.text == "Button 2":
        bot.send_message(message.chat.id, "You pressed Button 2!")
    elif message.text == "Assalomu alaykum":
        bot.send_message(message.chat.id, "Va alaykum assalom")

bot.polling()# bot polling doimiy boglanishlikni hosil qilib beradi bot. bu ozgaruvchidan chaqiradi



