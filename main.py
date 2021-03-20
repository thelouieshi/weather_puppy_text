import requests
import datetime as dt
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
latitude = 54.04649
longtitude = -2.79988
api_key = "40fe9d1b9c0b529d69a197d4bce7b177"
account_sid = "ACb1fabd138d7f5575bb001c4712bd4f1d"
auth_token = "e119420d47ae634aa954e21e850e0974"

# enter your location by latitude and longtitude here
weather_params = {
    "lat": 54.04649,
    "lon": -2.79988,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(OWM_endpoint, params=weather_params)
weather_data = response.json()
hourly_data = weather_data['hourly']

# 12-hour forecast
weather_id = []
for n in range(0, 12):
    hour_id = hourly_data[n]['weather'][0]['id']
    weather_id.append(hour_id)

will_rain = False
for i in weather_id:
    if i < 700:
        will_rain = True
print(weather_id)

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain or snow today",
        from_='+15172012350',
        to='+1YOUR NUMBER',
    )

    print(message.status)

elif not will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It won't rain or snow today! Have a nice day!",
        from_='+15172012350',
        to='+1YOUR NUMBER',
    )

    print(message.status)


def puppy_text():
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hang out with the dog!",
        from_='+15172012350',
        to='+1YOUR NUMBER',
    )

    print(message.status)


start_program = False
if dt.datetime.now().hour >= 8:
    start_program = True

# Using a while loop to get the program continue to run, set the program to start at 8 am stop at the 10 pm at night
# you can change change the hour, minute, second, & microsecond to any time you want.
while dt.datetime.now().hour != 22 and start_program:
    if dt.datetime.now().hour % 2 == 0 and dt.datetime.now().minute == 10 and dt.datetime.now().second == 16 and dt.datetime.now().second == 84966:
        puppy_text()

