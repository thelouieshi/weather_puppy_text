# I built this program to text myself whether it will rain or snow in Colorado and also to tell myself to hangout with our dog every two hours.

import requests
import datetime as dt
from text import Text  # Text class created in the text.py file

text = Text()  # to use the attributes and functions declared inside the Text class
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall?" 

# parameters required by the OWM API
weather_params = {
    "lat": 54.04649, # Denver, CO location, change to your desired location here
    "lon": -2.79988,
    "exclude": "current,minutely,daily",
    "appid": "YOUR API ID", # please use your own OWM API ID
}

response = requests.get(OWM_endpoint, params=weather_params)
weather_data = response.json()
hourly_data = weather_data['hourly'] # parsing the JSON response

# 12-hour forecast
weather_id = []
for n in range(0, 12):
    hour_id = hourly_data[n]['weather'][0]['id']
    weather_id.append(hour_id)

# hourly weather IDs can be identical and consecutive,
# and can't use .index to accurately get index with duplicates. To solve this bug:
# Because weather IDs are < 640 and/or 540, so I can add incrementally to the ids to eliminate the duplicates,
# for examples, [501, 501, 501] will become [502, 503, 504]:
add = 1
new_weather_id = []
for d in weather_id:
    d = d + add
    new_weather_id.append(d)
    add = add + 1

# Using list indexing, I can then easily access the start and the end of the weather.
rain_hour_list = []
snow_hour_list = []
for i in new_weather_id:
    if 500 < i < 600:
        rain_hour = new_weather_id.index(i) + dt.datetime.now().hour
        rain_hour_list.append(rain_hour)  # put the rain hours in a list
        text.weather_message = f"It will rain today at {rain_hour_list[0]} and ends at {rain_hour_list[-1]}."  # obtain the first and last element in rain showers.
    elif 600 < i < 700:
        snow_hour = new_weather_id.index(i) + dt.datetime.now().hour
        snow_hour_list.append(snow_hour)  # put the snow hours in a list
        text.weather_message = f"It will snow today at {snow_hour_list[0]} and ends at {snow_hour_list[-1]}."

# Compiling both rain and snow hours into one list also allows me to solve the bug that if it rains and snows on the same day.
# It is also a simple way to ensure the rain and snow hours stays in order.
if len(rain_hour_list) > 0 and len(snow_hour_list) > 0:
    bad_weather_hour = rain_hour_list + snow_hour_list
    text.weather_message = f"It will rain and snow today. Rain starts at {rain_hour_list[0]} and ends at {rain_hour_list[-1]}," \
                           f"snow starts at {snow_hour_list[0]} and ends at {snow_hour_list[-1]}. "

text.weather_text()

# the following code is for puppy text, I want my program start around 6, when I first wake up.
start_program = False
if dt.datetime.now().hour >= 6:
    start_program = True

# Using a while loop to get the program continue to run, set the program to start at 8 am and stop at the 10 pm at night
# you can change change the hour, minute, second, & microsecond to any time you want. Text will only be sent when its an exact match. 
while dt.datetime.now().hour != 22 and start_program:
    if dt.datetime.now().hour % 2 == 0 and dt.datetime.now().minute == 10 and dt.datetime.now().second == 16 and dt.datetime.now().second == 84966:
        text.puppy_text()

# Things you will need to make this code work:
# 1) Download both main.py and text.py which contains the Text class.
# 2) The lattititude and longitude of your desired location. 
# 3) Your own API ID on OWM weather map.
# 4) Your own Twilio credentials. 
# 5) You can also change the frequency and timing of the puppy text as you wish.
# 6) This code is designed to run with PythonAnywhere or other cloud services. 
