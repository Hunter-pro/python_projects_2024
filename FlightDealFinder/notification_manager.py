from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv('.env')
class NotificationManger:
    def __init__(self) -> None:
        self.account_sid = os.getenv('twilio_account_sid')
        self.auth_token = os.getenv('twillo_auth_token')

    def send_msg(self,msg):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
                    from_='+12512201998',
                    to='+917207815194',
                    body=msg,
                    )