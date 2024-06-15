from telebot import TeleBot, types
bot = TeleBot('7293075143:AAHcGWvUmnmK4lo4qxtXcmX6KmfvOTTlWtg')

@bot.message_handler(commands=['start','salom','register'])
def register(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    contact_button = types.KeyboardButton("Send Contact", request_contact=True)
    location_button = types.KeyboardButton("Send Location", request_location=True)
    markup.add(contact_button, location_button)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.message_handler(content_types=['contact', 'location'])
def handle_special_content(message):
    if message.contact:
        bot.send_message(message.chat.id, f"Received contact: {message.contact.phone_number}")
    elif message.location:
        bot.send_message(message.chat.id, f"Received location: {message.location.latitude}, {message.location.longitude}")
        # bot.send_message(message.chat.id, f"GOOGLE MAP LINK https://www.google.com/maps/@{message.location.latitude},{message.location.longitude},12z?entry=ttu")

bot.polling()