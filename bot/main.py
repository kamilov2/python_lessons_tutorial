import telebot
import datetime
import time
from telebot import types
bot_token = "7293075143:AAHcGWvUmnmK4lo4qxtXcmX6KmfvOTTlWtg"

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['hello','start','salom'])
def start_command(message):   
   
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="salom")
    button1 = types.KeyboardButton(text="salom")
    
    keyboard.add(button,button1)
    
 
    bot.send_message(message.chat.id, "Assalomu alaykum! ", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_message(message):
    if str(message.text).startswith('https://'):
        bot.send_message(message.chat.id, 'reklama tarkatma')
        

bot.polling()