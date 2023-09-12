# SQLkiss Cat's Horoscope
import random
import telebot
import sys
import os
import datetime
import openai
from phase_moon import calculate_moon_phase
from Zodiac_Signs import funny_forecasts
from loguru import logger


# ID of groups
log_chat_id = '-1001945815831'
group_chat_id = '-1001760424253' #
                                 # CHAT GROUP ID: how to find this:
                                 #  https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
                                 # Choose the answer with 58's rating ('the simplest way i found using only telegram-web :')
                                 #

# BOT Token
TOKEN = os.environ.get('BOT_TELEGRAM_TOKEN_FOR_CODE', 'nothing')
bot = telebot.TeleBot(TOKEN)
if TOKEN == 'nothing':
    bot.send_message(log_chat_id, 'TOKEN not accept')
    sys.exit("TOKEN not accept")

# API KEY
openai.api_key = os.environ.get('OPENAI_API_KEY', 'notapi')
if openai.api_key == 'notapi':
    bot.send_message(log_chat_id, 'TOKEN not accept')
    sys.exit("API Key not accept")


# Question for the chatGPT *prompt* and choose random funny forecast
random_value = random.choice(list(funny_forecasts.values()))
prompt = f"Rephrase the following sentence, making it sound different but retaining the same meaning and add emoji:\n{random_value}"
response = openai.Completion.create(
    engine="davinci", # Model
    prompt=prompt,
    max_tokens=100
)
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{prompt}"}]) #creating discussion


# fun for checking and updating work of bot into privat messages *this is just for self-debugging*
@bot.message_handler(commands=['start'])
def start(message):
    chat_id =  message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    forecast_button = telebot.types.KeyboardButton("Forecasts")
    keyboard.add(forecast_button)
    bot.send_message(chat_id, f'Hi, I\'m a bot that can provide you with funny forecasts!')
    bot.send_message(chat_id, f'Here are some things you can do:')
    bot.send_message(chat_id, f'- Press the "Forecasts" button below to get a random forecast.', reply_markup=keyboard)

# current Moon phase
current_date = datetime.datetime.now()
current_month = current_date.month
current_day = current_date.day
current_year = current_date.year
current_moon_phase = calculate_moon_phase(current_year,current_month, current_day)

# fun for getting forecasts
@bot.message_handler(func=lambda message: message.text.lower() == "forecasts")
def send_forecast(message):
    chat_id = group_chat_id
    sendforecastvaruable = (f"Purrs and whiskers! It looks like we're in the midst of {current_moon_phase}, so it's time for some serious rub-a-dub forecast, my feline friends!" + f"\n{chat_completion.choices[0].message.content}")
    bot.send_message(chat_id, sendforecastvaruable)
    return f"Thank you for reading our horoscope"

# fun for posting the forecasts to group
def post_forecast():
    chat_id = group_chat_id
    send_forecast(chat_id)

# send logs to another chat with logs
@bot.message_handler(func=lambda message: message.text.lower() == "logs")
def send_logs():
    log_content = ""
    log_content += f"Debug logs🐱: {logger.debug}\n"
    log_content += f"\nInfo logs🐈: {logger.info}\n"
    log_content += f"\nWarning logs🐱: {logger.warning}\n"
    log_content += f"\nError logs🐈: {logger.error}\n"
    log_content += f"\nException logs🐱: {logger.exception}\n"
    
    chat_id = log_chat_id
    bot.send_message(chat_id, log_content)
    
# running script
if __name__ == "__main__":
    post_forecast()
    send_logs()
    