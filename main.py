# SQLkiss Cat's Horoscope
import datetime
import random
import time
import telebot
from Zodiac_Signs import funny_forecasts
 
#bot token 
TOKEN = '6692357135:AAGj7Fs2tD8Gah-Bcnj1JMUAVkrFgdGzPa0'
bot = telebot.TeleBot(TOKEN)
group_chat_id = 'Cats_Horoscope'


keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
forecast_button = telebot.types.KeyboardButton("Forecasts")
keyboard.add(forecast_button)

keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
post_button = telebot.types.KeyboardButton("/post")
keyboard.add(post_button)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    random_key = random.choice(list(funny_forecasts.keys()))
    random_value = funny_forecasts[random_key]
    bot.send_message(chat_id, f'Hi, I\'m a bot that can provide you with funny forecasts!')
    bot.send_message(chat_id, f'Here are some things you can do:')
    bot.send_message(chat_id, f'- Press the "Forecasts" button below to get a random forecast.', reply_markup=keyboard)


@bot.message_handler(commands=['post'])
def post_message(message):
    chat_id = message.chat.id
    forecast_result = send_forecast(message)
    bot.send_message(chat_id, forecast_result)


@bot.message_handler(func=lambda message: message.text.lower() == "forecasts")
def send_forecast(message):
    chat_id = message.chat.id
    now = datetime.datetime.now()
    if now.hour == 23 and now.minute == 18:
        random_key = random.choice(list(funny_forecasts.keys()))
        random_value = funny_forecasts[random_key]
        bot.send_message(chat_id, f'{random_value}')
    else:
        return "No forecast available at the moment."
    
    return f"Thank you for reading our horoscope"


# This line starts the bot polling for updates
bot.polling()
