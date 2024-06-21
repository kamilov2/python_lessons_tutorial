import json
from telebot import types, TeleBot


bot = TeleBot("7293075143:AAHcGWvUmnmK4lo4qxtXcmX6KmfvOTTlWtg")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button = types.KeyboardButton("Kontakt yuborish: ", request_contact=True)
    markup.add(button)
    print(message.from_user)
    full_name = message.from_user.full_name
    username = message.from_user.username

    if username:
        user_link = f"<a href='https://t.me/{username}'>{full_name}</a>"
    else:
        user_link = full_name
  

    bot.send_message(message.chat.id, f"Assalomu alaykum {user_link}", reply_markup=markup, parse_mode='HTML')
    
bot.polling()
