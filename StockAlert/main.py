
import requests
import datetime as dt
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv('.env')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv('STOCK_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')


today = dt.date.today()
yesterday = today - dt.timedelta(days=4)
day_before_yesterday = today - dt.timedelta(days=5)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':STOCK_API_KEY

}

parameters2 = {
    'q':'tesla',
    'apikey': NEWS_API_KEY
}


response = requests.get(url='https://www.alphavantage.co/query',params=parameters)
response2 = requests.get(url='https://newsapi.org/v2/everything',params=parameters2)

response.raise_for_status()
response2.raise_for_status()

data = response.json()['Time Series (Daily)']
today_stock_data = data[str(yesterday)]
yesterday_stock_data = data[str(day_before_yesterday)]

    
today_close_price = float(today_stock_data['4. close'])
yesterday_close_price = float(yesterday_stock_data['4. close'])

percentage = (yesterday_close_price - today_close_price)/yesterday_close_price * 100 
if percentage > 5 or percentage < 5:
    articles = response2.json()['articles']
    titles = [articles[i]['title'] for i in range(3)]
    descriptions = [articles[i]['description'] for i in range(3)]
    
    account_sid = os.getenv('twilio_account_sid')
    auth_token = os.getenv('twilio_auth_token')
    client = Client(account_sid, auth_token)

    msg=f'{STOCK}'+'🔺' if percentage > 5 else '🔻'+f'\n Headline:{titles[0]} \nBrief:{descriptions[0]}'

    message = client.messages.create(
    from_='+12512201998',
    body=msg,
    to='+917207815194'
    )

    print(message.status)





    

   








