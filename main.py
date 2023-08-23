# SQLkiss Cat's Horoscope
import datetime
import random
import telebot
import time
from Zodiac_Signs import funny_forecasts

#bot token
TOKEN = '6692357135:AAGj7Fs2tD8Gah-Bcnj1JMUAVkrFgdGzPa0'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    random_key = random.choice(list(funny_forecasts.keys()))
    random_value = funny_forecasts[random_key]
    bot.send_message(chat_id, f'{random_value}')

    while True:
        now = datetime.datetime.now()
        if now.hour == 12 and now.minute == 0:
            bot.send_message(chat_id, "Your message there.")

        time.sleep(60)  # pause for 1 minute


bot.polling()