import datetime

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

moon_phase = calculate_moon_phase(year, month, day)
print(moon_phase)