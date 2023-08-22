# SQLkiss Cat's Horoscope
import datetime
import sqlite3
from Zodiac_Signs import signs_zodiac, funny_forecasts


def insert_data(sign, forecast):
    conn = sqlite3.connect('zodiac.db')
    cursor = conn.cursor()

    try:
        cursor.execute(sign, forecast)
        conn.commit()
        print(f"Forecast for {sign} successful added.")
    except sqlite3.IntegrityError:
        print(f"Прогноз для {sign} уже существует.")

    conn.close()


def get_forecast(sign):
    conn = sqlite3.connect('zodiac.db')
    cursor = conn.cursor()

    cursor.execute('SELECT forecast FROM zodiac WHERE sign = ?', (sign,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    else:
        return f"Forecast for {sign} does not found."


def calculate_moon_phase(year, month, day):
    ages = [18, 0, 11, 22, 3, 14, 25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, 26, 7]
    offsets = [-1, 1, 0, 1, 2, 3, 4, 5, 7, 7, 9, 9]
    description = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
                   "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]

    date = datetime.date(year, month, day)
    days_since_new = (date - datetime.date(2000, 1, 6)).days
    phase_index = (days_since_new + offsets[date.year % 12] + ages[date.year % 19]) % 30

    return description[int((phase_index % 8) / 2)]


today = datetime.date.today()

year = today.year
month = today.month
day = today.day

insert_data('Aries', 'Today will be all cool!') # make a sign and forecast to DataBase

zodiac_sign = 'Leo'
forecast = get_forecast(zodiac_sign)
print(f"Forecast for {zodiac_sign}: {forecast}")

moon_phase = calculate_moon_phase(year, month, day)
print(f"The moon phase on {year}-{month:02d}-{day:02d} is {moon_phase}.")
print(signs_zodiac['leo'])
print(funny_forecasts['leo'])

