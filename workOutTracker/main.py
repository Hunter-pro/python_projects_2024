
import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv('.env')

NUTRINIX_APP_ID = os.getenv('NUTRINIX_APP_ID')
NUTRINIX_API_KEY = os.getenv('NUTRINIX_API_KEY')
nutrinix_endpoint= os.getenv('nutrinix_endpoint')
sheety_endpint = os.getenv('sheety_endpint')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

headers = {

    'x-app-id':NUTRINIX_APP_ID,
    'X-app-key':NUTRINIX_API_KEY
}

parameters = {
    'query':input('tell me exercise you did?:')
}


response = requests.post(url=nutrinix_endpoint,headers=headers,json=parameters) # type: ignore

response.raise_for_status()

output = response.json()


headers = {
    'Authorization':SHEETY_TOKEN
}
for exercise2 in output['exercises']:
    date = dt.date.today().strftime('%d/%m/%Y')
    time = dt.datetime.now().time().strftime('%H:%M:%S')
    exercise = exercise2['name'].title()
    duration = exercise2['duration_min']
    calories = exercise2['nf_calories']

    sheety_input = {
        'workout':{
                'date':date,
                'time':time,
                'exercise':exercise,
                'duration':duration,
                'calories':calories  
                }
        
    }

    response2 = requests.post(url=sheety_endpint,json=sheety_input,headers=headers) # type: ignore

response2.raise_for_status()



