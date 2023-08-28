# SQLkiss Cat's Horoscope
import random
import telebot
import sys
import os
from Zodiac_Signs import funny_forecasts

#bot token 
TOKEN = os.environ.get('BOT_TELEGRAM_TOKEN_FOR_CODE', 'nothing')
if TOKEN == 'nothing':
    sys.exit("TOKEN not accept")

bot = telebot.TeleBot(TOKEN)
group_chat_id = '-1001760424253' #
                                 #CHAT GROUP ID: how to find this:
                                 #  https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
                                 # Choose the answer with 58's rating ('the simplest way i found using only telegram-web :')
                                 #


# fun for checking and updating work of bot
@bot.message_handler(commands=['start'])
def start(message):
    chat_id =  message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    forecast_button = telebot.types.KeyboardButton("Forecasts")
    keyboard.add(forecast_button)
    bot.send_message(chat_id, f'Hi, I\'m a bot that can provide you with funny forecasts!')
    bot.send_message(chat_id, f'Here are some things you can do:')
    bot.send_message(chat_id, f'- Press the "Forecasts" button below to get a random forecast.', reply_markup=keyboard)


# fun for getting forecasts from dictionary (from Zodiac_Sighns)
@bot.message_handler(func=lambda message: message.text.lower() == "forecasts")
def send_forecast(message):
    global random_value
    global random_key
    chat_id = group_chat_id
    random_key = random.choice(list(funny_forecasts.keys()))
    random_value = funny_forecasts[random_key]
    bot.send_message(chat_id, f'{random_value}')
    return f"Thank you for reading our horoscope"


# fun for posting the forecasts to group
def post_forecast():
    chat_id = group_chat_id
    send_forecast(chat_id)


# running script
if __name__ == "__main__":
    post_forecast()