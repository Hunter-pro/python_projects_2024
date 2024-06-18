##################### Extra Hard Starting Project ######################
import datetime as dt
from operator import le
import random
import smtplib
import os
from dotenv import load_dotenv 

load_dotenv('.env')

import pandas
# 1. Update the birthdays.csv
my_email = os.getenv('my_email')
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
data = pandas.read_csv('./automate_mail/birthdays.csv')
birthdays = data.to_dict(orient='records')

for birthday in birthdays:
    if birthday['day'] == now.day and birthday['month'] == now.month:
        with open(f'./automate_mail/letter_templates/letter_{random.randint(1,6)}.txt') as letter:
            contents = letter.read()
            letter_contents = contents.replace('[NAME]',birthday['name'])
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email,password=os.getenv('app_password'))#type:ignore
            connection.sendmail(from_addr=my_email,to_addrs=birthday['email'],msg=f'subject:Happy Birthday\n\n {letter_contents}')#type:ignore






