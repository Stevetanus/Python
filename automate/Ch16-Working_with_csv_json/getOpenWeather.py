#! python3
# Prints the current weather for a location from the command line.

import json
import requests
import sys
import os

APPID = "6d0ba0f4fb360589aff2691e82ae58e5"

# Compute location from command line arguments
# 只要該城市名字並非重複，可以只輸入城市
if len(sys.argv) < 1:
    print('Usage: quickweather.py city_name, 2-letter_country_code')
    sys.exit()
location = ''.join(sys.argv[1:])
print(location)

# Download the JSON data from openweathermap.org's API
# 我將網址修改成當前天氣結果/weather並加入&units=metric將溫度轉成攝氏
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s&units=metric' % (
    location, APPID)
response = requests.get(url)
response.raise_for_status()
url_2 = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s&units=metric' % (
    location, APPID)
response_2 = requests.get(url_2)
response_2.raise_for_status()

# Load JSON data into Python variable.
weatherData = json.loads(response.text)
forecastData = json.loads(response_2.text)

# print(response.text)
coord = weatherData['coord']
print(f'longitude of {location} is {coord["lon"]}')
print(f'latitude of {location} is {coord["lat"]}')
w = weatherData['weather']
w[0]["description"]
main = weatherData['main']
print(f'Current weather in {location}:\n'
      f'{w[0]["main"]}-{w[0]["description"]}, '
      f'temperature is {main["temp"]}\N{DEGREE SIGN}C, and feels like {main["feels_like"]}\N{DEGREE SIGN}C')
# probability of precipitation
for i in range(15):
    data = forecastData['list'][i]
    print(
        f"{data['dt_txt']} {data['weather'][0]['description']}/pop: {str(data['pop'])}")
