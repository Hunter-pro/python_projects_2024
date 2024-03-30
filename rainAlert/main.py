
from twilio.rest import Client
import requests
from math import floor
import os
from dotenv import load_dotenv

load_dotenv('.env')

API_KEY = os.getenv('opw_api_key')
ACCOUNT_SID = os.getenv('twilio_account_sid')
AUTH_TOKEN = os.getenv('twilio_auth_token')

api_key = API_KEY
account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN


parameters = {
    'lat': '17.385044',
    'lon': '78.486671',
    'appid': "81a20aecc0ab7ba5632ec0be2332e3e0",
    'cnt':'4'
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast',params=parameters)

response.raise_for_status()

data = response.json()
status_code = data['cod']
description =""
temp = str(floor(data['list'][2]['main']['temp']-273.15))

print(f'Status code: {status_code}')

weather_description = [i['weather'] for i in data['list']]


for i in range(len(weather_description)):
    weather_forcast = weather_description[i][0]['id']
    if 200 <= int(weather_forcast) <=299 :
        description = 'thunderstorm'
    elif 300 <= int(weather_forcast) <=399:
        description = 'drizzel'
    elif 500 <= int(weather_forcast) <=599:
        description = 'rain'
    else:
        description = 'be clear'
    

msg = 'GOOD MORINIG🌞\ntoday it is going to '+description+'\ntemp:' + temp

client = Client(account_sid,auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=msg,
  to='whatsapp:+917207815194'
)

    
print(message.status)





