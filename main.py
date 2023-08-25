# SQLkiss Cat's Horoscope
import random
import telebot
from Zodiac_Signs import funny_forecasts
 
#bot token 
TOKEN = '6692357135:AAGj7Fs2tD8Gah-Bcnj1JMUAVkrFgdGzPa0' # You have to add your token of bot there
bot = telebot.TeleBot(TOKEN)
group_chat_id = '-1001760424253' #
                                 #CHAT GROUP ID: how to find this:
                                 #  https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
                                 # Choose the answer with 58's rating ('the simplest way i found using only telegram-web :')
                                 #


keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
forecast_button = telebot.types.KeyboardButton("Forecasts")
keyboard.add(forecast_button)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id =  message.chat.id
    random_key = random.choice(list(funny_forecasts.keys()))
    random_value = funny_forecasts[random_key]
    bot.send_message(chat_id, f'Hi, I\'m a bot that can provide you with funny forecasts!')
    bot.send_message(chat_id, f'Here are some things you can do:')
    bot.send_message(chat_id, f'- Press the "Forecasts" button below to get a random forecast.', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == "forecasts")
def send_forecast(message):
    chat_id = group_chat_id
    random_key = random.choice(list(funny_forecasts.keys()))
    random_value = funny_forecasts[random_key]
    bot.send_message(chat_id, f'{random_value}')

    return f"Thank you for reading our horoscope"


# This line starts the bot polling for updates
bot.polling()
