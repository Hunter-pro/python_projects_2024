import smtplib
import string
from turtle import pos
import requests
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv('.env')

MY_LAT = 17.385044 # Your latitude
MY_LONG = 78.486671# Your longitude

ISS_ENDPONT= os.getenv('iss_url')
SUN_ENDPOINT = os.getenv('sun_url')

def position():
    response = requests.get(url=ISS_ENDPONT) # type: ignore
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if (MY_LAT-5,MY_LONG-5) <= (iss_latitude,iss_longitude) <= (MY_LAT+5,MY_LONG+5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(SUN_ENDPOINT, params=parameters) # type: ignore
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset and time_now <= sunrise:
        return False


if position() and is_night():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user='kushalcherukula@gmail.com',password='bhzf uhhg mlod hlks')
        connection.sendmail(from_addr='kushalcherukula@gmail.com',to_addrs='kushalcherukula@gmail.com',msg='subject:remider\n\n Look up the international space station is above you')
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



