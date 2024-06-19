from telebot import TeleBot, types

bot = TeleBot('7293075143:AAHcGWvUmnmK4lo4qxtXcmX6KmfvOTTlWtg')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("assalomu alaykum", callback_data='btn1')
    button2 = types.InlineKeyboardButton("Kanalimizga obuna boling", url='https://kun.uz/')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'btn1':
        bot.send_message(call.message.chat.id, "va alaykum assalom")


bot.polling()