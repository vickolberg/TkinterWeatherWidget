import requests
from pprint import pprint
from datetime import datetime, timedelta
import math
import os
from tkinter import *
from secret import APIKey


APIKey = APIKey
state = input("State: ")
zip_code = int(input("Zip Code: "))
country_code = input("Country: ")

geo_convert = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={APIKey}"

response = requests.get(geo_convert)

data = response.json()
latitude = data["lat"]
longitude = data["lon"]

current_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={APIKey}"

response_2 = requests.get(current_weather_url)
weather = response_2.json()

# pprint(weather)

sunrise_timestamp = weather['sys']['sunrise']
sunset_timestamp = weather['sys']['sunset']

city_name = weather['name']

daily_high = weather['main']['temp_max']
daily_high = math.ceil((daily_high * 1.8) - 459.67)

daily_low = weather['main']['temp_min']
daily_low = math.floor((daily_low * 1.8 ) - 459.67)

current_temp = weather['main']['temp']
current_temp = math.ceil((current_temp * 1.8 ) - 459.67)

est_offset_hours = -5
sunrise_time_utc = datetime.utcfromtimestamp(sunrise_timestamp)
sunset_time_utc = datetime.utcfromtimestamp(sunset_timestamp)
est_offset = timedelta(hours=est_offset_hours)
sunrise_time_est = sunrise_time_utc + est_offset
sunset_time_est = sunset_time_utc + est_offset

os.system('clear')

print("Location:", city_name,",", state)
print("Temperature Now:", current_temp,"°F")
# print("\n")
print("Today's High Temperature:", daily_high,"°F")
print("Today's Low Temperature:", daily_low,"°F")
print("Sunrise:", sunrise_time_est.strftime("%Y-%m-%d %H:%M:%S EST"))
print("Sunset:", sunset_time_est.strftime("%Y-%m-%d %H:%M:%S EST"))


# Widget creation

root = Tk()
root.geometry("300x200")
root.title("Weather Widget")
city_label = Label(root, text=f"{city_name}")
city_label.config(font= ("Arial", 28))
city_label.pack(side= 'top')

now_temp_label = Label(root, text=f"Current Temp: {current_temp}°F")
now_temp_label.config(font= ("Arial", 15))
now_temp_label.pack(side= "top")

todays_high_label = Label(root, text=f"Today's High Temp: {daily_high}°F")
todays_high_label.config(font= ("Arial", 15))
todays_high_label.pack(side= "top")

todays_low_label = Label(root, text=f"Today's Low Temp: {daily_low}°F")
todays_low_label.config(font= ("Arial", 15))
todays_low_label.pack(side= "top")

sunrise_label = Label(root, text=f"Sunrise: {sunrise_time_est}")
sunrise_label.config(font=("Arial", 15))
sunrise_label.pack(side="top")

sunset_label = Label(root, text=f"Sunset: {sunset_time_est}")
sunset_label.config(font=("Arial", 15))
sunset_label.pack(side="top")

mainloop()