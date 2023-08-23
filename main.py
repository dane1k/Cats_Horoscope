# SQLkiss Cat's Horoscope
import datetime
import random
import telebot
import time
from Zodiac_Signs import funny_forecasts

#bot token
TOKEN = '6692357135:AAGj7Fs2tD8Gah-Bcnj1JMUAVkrFgdGzPa0'
bot = telebot.TeleBot(TOKEN)


keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
forecast_button = telebot.types.KeyboardButton("Forecasts")
keyboard.add(forecast_button)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    random_key = random.choice(list(funny_forecasts.keys()))
    random_value = funny_forecasts[random_key]
    bot.send_message(chat_id, f'Hi, I\'m a bot that can provide you with funny forecasts!')
    bot.send_message(chat_id, f'Here are some things you can do:')
    bot.send_message(chat_id, f'- Press the "Forecasts" button below to get a random forecast.', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == "forecasts")
def send_forecast(message):
    chat_id = message.chat.id
    random_key = random.choice(list(funny_forecasts.keys()))
    random_value = funny_forecasts[random_key]
    bot.send_message(chat_id, f'{random_value}')

    now = datetime.datetime.now()
    if now.hour == 12 and now.minute == 0:
        bot.send_message(chat_id, "Your message there.")


# This line starts the bot polling for updates
bot.polling()
